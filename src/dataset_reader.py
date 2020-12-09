import pandas as pd
import os
from random import uniform
from src.config import RADIANT


def data_reader(filename="experiment"):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    filepath = path + "/static/dataset/" + filename + ".xlsx"

    df = pd.read_excel(filepath, sheet_name=0, nrows=1000)

    edge_set = set()
    user_set = set()
    edge_list = list()
    user_list = list()
    task_dict = dict()

    edge_id = 1
    for row in df.itertuples(index=True, name='Pandas'):
        latitude = getattr(row, "latitude")
        longitude = getattr(row, "longitude")
        user_id = getattr(row, "userid")
        if latitude not in edge_set:
            edge_list.append({"edge_id": edge_id, "lat": latitude, "lng": longitude})
            edge_set.add(latitude)
            edge_id += 1
        if user_id not in user_set:
            # 产生以目标边缘服务器为圆心的随机位置，以模拟真实的车流量
            v_latitude = uniform(latitude - RADIANT, latitude + RADIANT)
            v_longitude = uniform(longitude - RADIANT, longitude + RADIANT)
            # 由于edge_id 在每次新的edge添加到列表中后会自动指向下一个edge，所以当前真实edge_id 为 edge_id-1
            now_edge_id = edge_id - 1
            user_list.append(
                {"vehicle_id": user_id, "edge_id": now_edge_id, "v_latitude": v_latitude, "v_longitude": v_longitude})
            user_set.add(user_id)
        if user_id in task_dict:
            task_dict[user_id] += 1
        else:
            task_dict[user_id] = 1

        if latitude in task_dict:
            edge_list[-1]["queue_len"] += 1
        else:
            task_dict[latitude] = 1
            edge_list[-1]["queue_len"] = 1
            if len(edge_list) > 1:
                last_edge = edge_list[-2]
                last_edge["type"] = dic_type(last_edge.get("queue_len"))
    for user in user_list:
        user["per_tasks"] = task_dict.get(user.get("vehicle_id"))
    return edge_list, user_list


def data_clean(source_name, out_name):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    source_file = path + '/static/dataset/' + source_name + ".xlsx"
    output_file = path + '/static/dataset/' + out_name + ".csv"
    print("开始读取源文件")
    df = pd.read_excel(source_file, sheet_name=0)
    print("结束读取源文件\n开始清洗数据")
    data = df.dropna()
    print("结束清洗数据\n开始写入目标文件")
    data.to_excel(output_file)
    print("数据清洗成功")


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


if __name__ == '__main__':
    data_clean("plot_dataset_source", "plot_out")
