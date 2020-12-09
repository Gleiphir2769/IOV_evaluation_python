import json
import os
from random import uniform

import pandas as pd

def get_data_dict():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dataset_filename = "/static/dataset/plot_dataset_clean.xlsx"
    dataset_filepath = path + dataset_filename
    print("*" * 15, "开始读入数据集")
    df = pd.read_excel(dataset_filepath, sheet_name=0)
    print("*" * 15, "读入完毕")
    edge_set = set()
    user_set = set()
    edge_list = list()
    user_list = list()
    task_dict = dict()
    # task_list = list()

    edge_id = 1
    for row in df.itertuples(index=True, name='Pandas'):
        latitude = getattr(row, "latitude")
        longitude = getattr(row, "longitude")
        # user_id = getattr(row, "userid")
        if latitude not in edge_set:
            # edge_list.append([edge_id, latitude, longitude])
            edge_list.append({"edge_id": edge_id, "lat": latitude, "lng": longitude})
            edge_set.add(latitude)
            edge_id += 1

        if latitude in task_dict:
            edge_list[-1]["queue_len"] += 1
        else:
            task_dict[latitude] = 1
            edge_list[-1]["queue_len"] = 1
            if len(edge_list) > 1:
                last_edge = edge_list[-2]
                last_edge["type"] = dic_type(last_edge.get("queue_len"))

    return edge_list


def dic_type(queue_len):
    if queue_len < 10:
        return 1
    elif 10 <= queue_len < 20:
        return 2
    elif 20 <= queue_len < 50:
        return 3
    elif 40 <= queue_len < 100:
        return 4
    else:
        return 5

def make_json():
    edge_list = get_data_dict()

    # 以json格式写入文件
    print("*" * 15, "开始写入JSON")
    with open("../static/plot/data.json", "w") as fp:
        fp.write(json.dumps(edge_list, sort_keys=True, indent=4, separators=(',', ': ')))
    print("*" * 15, "写入JSON完成")

def make_csv():
    edge_list = get_data_dict()
    df = pd.DataFrame(list(edge_list))
    print("*" * 15, "开始写入CSV")
    df.to_csv("../static/plot/data.csv", sep=',', index=False, encoding="utf_8_sig")
    print("*" * 15, "写入CSV完成")


if __name__ == '__main__':
    make_csv()




