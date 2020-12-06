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
    latitude_list = list()
    longitude_list = list()
    edge_id = 1
    for row in df.itertuples(index=True, name='Pandas'):
        latitude = getattr(row, "latitude")
        longitude = getattr(row, "longitude")
        user_id = getattr(row, "userid")
        if latitude not in edge_set:
            edge_list.append([edge_id, latitude, longitude])
            edge_set.add(latitude)
            edge_id += 1
        if user_id not in user_set:
            # 产生以目标边缘服务器为圆心的随机位置，以模拟真实的车流量
            v_latitude = uniform(latitude-RADIANT, latitude+RADIANT)
            v_longitude = uniform(longitude-RADIANT, longitude+RADIANT)
            user_list.append([user_id, edge_id, v_latitude, v_longitude])
            user_set.add(user_id)
        if user_id in task_dict:
            task_dict[user_id] += 1
        else:
            task_dict[user_id] = 1

    for user in user_list:
        user.append(task_dict.get(user[0]))

    return edge_list, user_list
    # todo: 如何设定车辆的随机位置，计算距离原定服务器的偏移距离。把数据带到主函数初始化


if __name__ == '__main__':
    data_reader()
