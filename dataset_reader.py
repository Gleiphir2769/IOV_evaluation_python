import pandas as pd
import os
from random import uniform
from config import RADIANT


def data_reader():
    df = pd.read_excel('experiment.xlsx', sheet_name=0, nrows=1000)
    path = os.path.dirname(os.path.abspath(__file__))

    edge_set = set()
    user_set = set()
    edge_list = list()
    user_list = list()
    task_dict = dict()
    task_list = list()

    edge_id = 1
    for row in df.itertuples(index=True, name='Pandas'):
        latitude = getattr(row, "latitude")
        longitude = getattr(row, "longitude")
        user_id = getattr(row, "userid")
        if latitude not in edge_set:
            # edge_list.append([edge_id, latitude, longitude])
            edge_list.append({"edge_id": edge_id, "e_latitude": latitude, "e_longitude": longitude})
            edge_set.add(latitude)
            edge_id += 1
        if user_id not in user_set:
            # 产生以目标边缘服务器为圆心的随机位置，以模拟真实的车流量
            v_latitude = uniform(latitude - RADIANT, latitude + RADIANT)
            v_longitude = uniform(longitude - RADIANT, longitude + RADIANT)
            # user_list.append([user_id, edge_id, v_latitude, v_longitude])
            # 由于edge_id 在每次新的edge添加到列表中后会自动指向下一个edge，所以当前真实edge_id 为 edge_id-1
            now_edge_id = edge_id-1
            user_list.append(
                {"vehicle_id": user_id, "edge_id": now_edge_id, "v_latitude": v_latitude, "v_longitude": v_longitude})
            user_set.add(user_id)
        if user_id in task_dict:
            task_dict[user_id] += 1
        else:
            task_dict[user_id] = 1
        # task_list.append({"dis_edge_latitude": latitude, "dis_edge_longitude": longitude, "vehicle_id": user_id})

    for user in user_list:
        # user.append(task_dict.get(user[0]))
        user["per_tasks"] = task_dict.get(user.get("vehicle_id"))
    return edge_list, user_list


if __name__ == '__main__':
    data_reader()
