# MMRefine 💭: Multimodal Refinement Benchmark
> [MMRefine: Unveiling the Obstacles to Robust Refinement in Multimodal Large Language Models](https://arxiv.org/abs/2506.04688)    
> [Gio Paik](http://sites.google.com/view/giopaik), [Geewook Kim](https://geewook.kim/) and [Jinbae Im](https://scholar.google.com/citations?user=RbmA27QAAAAJ)*. *ACL Findings 2025*

[**🌐 Webpage**](https://mmrefine.github.io/) | [**🤗 Dataset**](https://huggingface.co/) | [**📖 Paper**](https://arxiv.org/abs/2506.04688) | [**🏆 Leaderboard**](https://mmrefine.github.io/#leaderboard)

## News
<!-- **[2025.06.10]** 🚀 Our dataset and [evaluation code](https://github.com/naver-ai/MMRefine) are available!     -->
**[2025.06.06]** 📜 We released our paper on [ArXiv](https://arxiv.org/abs/2506.04688)!    
**[2025.06.06]** 🏆 [Leaderboard](https://mmrefine.github.io/#leaderboard) is online!    
**[2025.05.14]** 🥳 MMRefine is accepted by ACL Findings 2025!

## Introduction

<p align="center">
  <img src="figures/1.intro_250213.png" width="500px">
</p>

MMRefine provides a comprehensive analysis of MLLMs' capability to detect and correct errors within a given initial solution across six distinct scenarios and six error types, which is an ability essential for test-time scaling techniques such as self-reflection or multi-agent debate.

## Requirements
To install the required packages:
```sh
pip install -r requirements.txt
```

You need to set your OpenAI API Key as an environment variable for evaluation. You can set it using:
```sh
export OPENAI_API_KEY="<YOUR_API_KEY>"
```

## Evaluation
1. First, you need to make a submission file for evaluation with a MLLM that you want to evaluate.
    - Implement your inference code in [inference code](inference/main.py#L16).
    - Run inference to generate a `submission.json` file. Please refer to [sample_submission_file.json](inference/sample_submission_file.json).
2. Run `evaluation/main.py` with submission file you've made.
```sh
python evaluation/main.py --submission_file <path-to-your-submission-file>
```

## Cite
TBD

## License
```
CorrBench
Copyright (c) 2025-present NAVER Cloud Corp.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
