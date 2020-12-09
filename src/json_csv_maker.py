import json
from dataset_reader import data_reader

import pandas as pd


def make_json(source_name="plot_dataset_clean", out_name="data"):
    edge_list, user_list = data_reader(source_name)
    # 以json格式写入文件
    print("*" * 15, "开始写入JSON")
    with open("../static/plot/" + out_name + ".json", "w") as fp:
        fp.write(json.dumps(edge_list, sort_keys=True, indent=4, separators=(',', ': ')))
    print("*" * 15, "写入JSON完成")


def make_csv(source_name="plot_dataset_clean", out_name="data"):
    edge_list, user_list = data_reader(source_name)
    # 以csv格式写入文件
    df = pd.DataFrame(list(edge_list))
    print("*" * 15, "开始写入CSV")
    df.to_csv("../static/plot/" + out_name + ".csv", sep=',', index=False, encoding="utf_8_sig")
    print("*" * 15, "写入CSV完成")
