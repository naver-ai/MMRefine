# MMRefine
# Copyright (c) 2025-present NAVER Cloud Corp.
# Apache-2.0
REFINEMENT_PROMPT = """
You are a mathematical expert with extensive knowledge across various mathematical fields. Your task is to meticulously evaluate and, if necessary, correct a given mathematical question and its proposed solution. Follow these steps:
1. Carefully read the provided question and solution.
2. Conduct a step-by-step review of the solution, addressing the following for each step:
  - Verify the mathematical correctness and logical flow.
  - Identify any errors including calculation errors, misunderstanding of the problem, or reasoning error. 
  - If an error is found, immediately stop the review process and proceed to step 3.
  - If no error is found, continue to the next step.
3. If an error is found:
  - Provide a brief explanation of the error.
  - Correct the solution starting from the erroneous step.
  - Complete the rest of the solution correctly.
4. If no errors are found in the entire solution, provide a brief confirmation of its correctness.

Output your analysis in the following format:

Review and Correction (if applicable):
Step 1: [Brief assessment of step 1]
Step 2: [Brief assessment of step 2]
...
Step X: [Brief assessment of step X]
Error found in step X: [Brief explanation of the error]
Corrected solution from step X:
Step X: [Corrected step]
Step X+1: [Next correct step]
...
[Final step]
...
Overall Assessment:
Correctness: [Correct / Incorrect]
Explanation: [Concise explanation of the assessment]
Final Answer: [Correct final answer]

Question: {question}
Solution: {initial_solution}
""".strip()
