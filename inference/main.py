# CorrBench
# Copyright (c) 2025-present NAVER Cloud Corp.
# Apache-2.0
"""
Sample Inference Code for MMRefine

You can modify `do_inference()` function to use your own inference pipeline.
"""

import json

import pandas as pd
from prompts import REFINEMENT_PROMPT
from tqdm import tqdm

dataset = pd.read_parquet("data/MMRefine_test.parquet")


def do_inference(text_query, image_bytes=None):
    raise NotImplementedError("You must implement your own inference pipeline")

submission_file = {}
for i in tqdm(range(len(dataset)), desc="Responding"):
    row = dataset.iloc[i]
    if row["image"]:
        image_bytes = row["image"]["bytes"]
    else:
        image_bytes = None

    query = REFINEMENT_PROMPT.format(
        question=row["question"], initial_solution=row["initial_solution"]
    )
    response = do_inference(query, image_bytes=image_bytes)

    submission_file[f"{row['id']}_{row['solution_source']}"] = {
        "id": row["id"],
        "solution_source": row["solution_source"],
        "question": row["question"],
        "answer": row["answer"],
        "initial_solution": row["initial_solution"],
        "solution_label": row["solution_label"],
        "reference_feedback": row["reference_feedback"],
        "error_type": row["error_type"],
        "prediction": response,
    }

with open("submission.json", "w") as f:
    json.dump(submission_file, f, indent=4)
print(f" [INFO] Responses saved to submission.json")
