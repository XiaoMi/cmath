from utils import *


def evaluate(response_file):
    """
    读取一个jsonl文件中的模型生成结果和标准答案，计算模型准确率。

    Args:
        response_file: str, 包含模型输出内容的jsonl文件路径，每行的json必须包含golden, response字段
    """
    d = read_jsonl_keys(response_file, ["response", "golden"])

    hit = 0    # 计数：正确
    err = 0    # 计数：模型回复异常
    warn = 0   # 计数：未能从模型回复中提取数字

    for g, r in zip(d["golden"], d["response"]):
        predict = extract_digits_prediction(r)
        if len(predict) == 0:
            warn += 1

        if "ERROR" in predict:
            err += 1

        if match_digit_response(g, predict):
            hit += 1

    sample_size = len(d["golden"])
    valid = sample_size - err
    acc = hit / valid
    print("acc={0:.0%}".format(acc))
    return acc
