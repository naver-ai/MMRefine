# CorrBench
# Copyright (c) 2025-present NAVER Cloud Corp.
# Apache-2.0
EVAL_PROMPT_CORRECT = """
Given the model's response, output 1 if 'Correctness' is 'Correct', otherwise output 0. Respond with only the number.

Model's Response: {response}

Output:
""".strip()

EVAL_PROMPT_INCORRECT = """
You are an expert evaluator assessing the quality of feedback provided on an initial solution to a problem. Your task is to determine if the feedback is effective in guiding the initial solution towards a correct answer. You will be provided with three components:

1.  **Initial Solution:** The initial attempt at solving the problem.
2.  **Feedback:**  Specific feedback provided in response to the initial solution.
3.  **Reference Feedback:** A verified, high-quality feedback to the initial solution.

Your evaluation should consider the following aspects:

*   **Error Detection:** Does the feedback correctly identify the errors or shortcomings in the initial solution?
*   **Error Correction:** Does the feedback effectively address the problems in the initial solution?
*   **Effectiveness and Correctness of the Feedback:** Does the feedback guide the initial solution towards the correct answer efficiently? Does it reach the same answer and logic as the reference feedback in terms of its core principles?

Output your assessment in the following format:

Error Detection: [0/1]
Error Correction: [0/1]
Effectiveness and Correctness of the Feedback: [0/1]

No additional feedback or comment is required.

Initial Solution: {initial_solution}
Feedback: {feedback}
Reference Feedback: {reference_feedback}

Output:
""".strip()

PARSING_PROMPT = """
Given the model's response, parse "{target}" from the response. Respond with only the number.

If the model's response does not contain "{target}", output 0.

Model's Response: {model_response}
""".strip()
