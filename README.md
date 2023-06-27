# CMATH
## Introduction
We present the Chinese Elementary School Math Word Problems (CMATH) dataset, comprising 1.7k elementary school-level math word problems with detailed annotations, source from actual Chinese workbooks and exams. This dataset aims to provide a benchmark tool for assessing the following question: to what grade level of elementary school math do the abilities of popular large language models (LLMs) correspond? We evaluate a variety of popular LLMs, including both commercial and open-source options, and discover that only GPT-4 achieves success (accuracy >= 60%) across all six elementary school grades, while other models falter at different grade levels.
Furthermore, we assess the robustness of LLMs by augmenting the original problems in the CMATH dataset with distracting information. Our findings reveal that GPT-4 is the sole model that maintains robustness, further distinguishing its performance from competing models. We anticipate that our CMATH dataset will expose limitations in LLMs' capabilities and promote their ongoing development and advancement.

## Datasets
### cmath_dev
Initial release of 600 examples from CMATH dataset, with 100 problems from each elementary school grade.  
We will release the remaining portion of the dataset by the end of the year.


### distractor
To assess the robustness of LLMs against "irrelevant" information, we manually created a small ``distractor dataset'' comprising 60 examples, 10 for each grade level. Each example consists of an original problem and five associated problems augmented with 1 ~ 5 piece(s) of irrelevant information which we refer to as distractor(s). 


## Script
We provide a script `eval.py` that implement automated evaluation.

## License
Licensed under either of
* MIT license
* BSD license

# CMATH
## 介绍
本项目中我们提出了CMATH数据集，包括1.7k个小学水平的数学应用题和详细的注释。本数据集旨在提供一个基准工具来评估以下问题：当前流行的大模型的数学能力对应小学数学几年级的水平？我们评估了各种流行的大模型，发现只有GPT-4能通过所有六个年级的数学考试(准确率>=60%)。此外，我们通过在CMATH数据集中添加干扰信息来评估大模型的稳健性。我们的研究结果表明，GPT-4是唯一保持鲁棒性的模型。

## 数据集
### cmath_dev
我们分两批开源CMATH数据集中的样本。第一批开源600条样本，每个年级100条。首次开源的样本可以视为一个dev集。剩余的样本（可以视为test集）将在年底开源。


### distractor
为了评估大模型面对干扰信息的稳健性，我们创建了一个小型“干扰集”，包含60条样本。每条样本中包含1个原始问题，以及5个由我们手工添加干扰信息后的“增广问题”，共6个问题。


## 代码
我们提供了一个脚本`eval.py`用于对模型生成的回复进行自动化的评估。

## 开源协议
Licensed under either of
* MIT license
* BSD license