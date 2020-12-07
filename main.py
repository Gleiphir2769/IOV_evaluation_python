from random import shuffle

from vehicle import Vehicle
from edge_server import EdgeServer
from offloading_strategy import Solution
from offloading_strategy import cal_total_time

if __name__ == '__main__':
    # todo: 分组实验问题 + 真实任务流问题
    print("车辆数为20， 任务数变化区间为5-50的对照试验：")
    # for per_tasks in range(5, 55, 5):
    #     cal_total_time(per_tasks, 20, "myalgo")
    for per_tasks in range(5, 55, 5):
        cal_total_time(per_tasks, 20)
    #
    # print("任务数为20， 车辆数变化区间为5-50的对照实验：")
    # for vehicle_nums in range(5, 55, 5):
    #     cal_total_time(20, vehicle_nums, "myalgo")
    # cal_total_time(1, 20, "myalgo")
