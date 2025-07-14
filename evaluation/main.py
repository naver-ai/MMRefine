# CorrBench
# Copyright (c) 2025-present NAVER Cloud Corp.
# Apache-2.0
import argparse
import json
import os

import requests
from prompts import EVAL_PROMPT_CORRECT, EVAL_PROMPT_INCORRECT, PARSING_PROMPT
from tqdm import tqdm

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

argparser = argparse.ArgumentParser()
argparser.add_argument("--evaluation_model", type=str, default="gpt-4o")
argparser.add_argument("--submission_file", type=str, default=None)

args = argparser.parse_args()

try:
    with open(args.submission_file, "r") as f:
        submission_file = json.load(f)
except Exception as e:
    print(f"Error loading submission file: {e}")
    exit(1)


def call_gpt(query, model_name, retry=3):
    for i in range(retry):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OPENAI_API_KEY}",
            }
            content = [
                {"type": "text", "text": query},
            ]
            payload = {
                "model": model_name,
                "messages": [{"role": "user", "content": content}],
            }
            response = requests.post(
                f"https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
            )
            if "choices" in response.json():
                return response.json()["choices"][0]["message"]["content"]
            else:
                raise Exception(f"Error calling GPT: {response.json()}")
        except Exception as e:
            print(f"Error calling GPT: {e}")
    return None


for k in tqdm(submission_file.keys(), desc="Evaluating"):
    result = submission_file[k]
    eval_result = {}
    if result["solution_label"] == "correct":
        query = EVAL_PROMPT_CORRECT.format(response=result["prediction"])
        resp = call_gpt(query, model_name=args.evaluation_model)
        score = int(resp.strip())

        eval_result["solution_correctness"] = score

        if score == 1:
            submission_file[k]["judge"] = "Verification Success"
        else:
            submission_file[k]["judge"] = "False Error Detection"
    else:  # initial solution is incorrect
        query = EVAL_PROMPT_INCORRECT.format(
            initial_solution=result["initial_solution"],
            feedback=result["prediction"],
            reference_feedback=result["reference_feedback"],
        )
        resp = call_gpt(query, model_name=args.evaluation_model)

        error_detection = int(
            call_gpt(
                PARSING_PROMPT.format(target="Error Detection", model_response=resp),
                model_name=args.evaluation_model,
            ).strip()
        )
        error_correction = int(
            call_gpt(
                PARSING_PROMPT.format(target="Error Correction", model_response=resp),
                model_name=args.evaluation_model,
            ).strip()
        )
        solution_correctness = int(
            call_gpt(
                PARSING_PROMPT.format(
                    target="Effectiveness and Correctness of the Feedback",
                    model_response=resp,
                ),
                model_name=args.evaluation_model,
            ).strip()
        )

        eval_result["error_detection"] = error_detection
        eval_result["error_correction"] = error_correction
        eval_result["solution_correctness"] = solution_correctness

        if error_detection == 0:
            submission_file[k]["judge"] = "Refinement Failure"
        else:
            if error_correction == 0:
                submission_file[k]["judge"] = "Error Detection Success"
            else:
                if solution_correctness == 0:
                    submission_file[k]["judge"] = "Error Correction Success"
                else:
                    submission_file[k]["judge"] = "Refinement Success"
    submission_file[k]["result"] = eval_result

with open(args.submission_file.replace(".json", "_eval.json"), "w") as f:
    json.dump(submission_file, f, indent=4)
print(f" [INFO] Results saved to {args.submission_file.replace('.json', '_eval.json')}")

from collections import defaultdict

counter = defaultdict(int)
# Calculate Scores
for k, v in submission_file.items():
    counter[v["judge"]] += 1
    counter[v["solution_label"]] += 1

scores = {
    "Refinement Failure": counter["Refinement Failure"] / counter["incorrect"],
    "Error Detection Success": (
        counter["Error Detection Success"]
        + counter["Error Correction Success"]
        + counter["Refinement Success"]
    )
    / counter["incorrect"],
    "Error Correction Success": (
        counter["Error Correction Success"] + counter["Refinement Success"]
    )
    / counter["incorrect"],
    "Refinement Success": counter["Refinement Success"] / counter["incorrect"],
    "Verification Success": counter["Verification Success"] / counter["correct"],
    "False Error Detection": counter["False Error Detection"] / counter["correct"],
}
scores["RefScore"] = scores["Refinement Success"] - scores["False Error Detection"]
scores["mRecall"] = (
    scores["Error Detection Success"] + scores["Verification Success"]
) / 2

print("Evaluation Results:")
print(scores)

with open(args.submission_file.replace(".json", "_scores.json"), "w") as f:
    json.dump(scores, f, indent=4)
print(
    f" [INFO] Scores saved to {args.submission_file.replace('.json', '_scores.json')}"
)
