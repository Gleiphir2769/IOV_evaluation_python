from random import randint
from random import shuffle

from vehicle import Vehicle
from edge_server import EdgeServer
from dataset_reader import data_reader

import config


class Solution:
    infrastructures = []

    def __init__(self, task, infrastructures):
        self.task = task
        self.infrastructures = infrastructures

    def offload_best_infrastructure(self):
        min_time = estimate_time(self.task, self.infrastructures[0])
        best_des = self.infrastructures[0]
        for infrastructure in self.infrastructures:
            if estimate_time(self.task, infrastructure) < min_time:
                min_time = estimate_time(self.task, infrastructure)
                best_des = infrastructure
        # 添加任务到最佳卸载设备等待队列中
        self.task.offload(best_des)
        # 卸载后将该任务所属车辆移动位置
        self.task.belong_vehicle.run(min_time)
        # print("vehicle id:" + str(self.task.belong_vehicle.id) + "  " + str(self.task.belong_vehicle))
        # 改变车辆所属时间戳，修正waiting time的计算
        self.task.belong_vehicle.refresh_timestamp(min_time)
        return min_time, best_des

    def offload_random_infrastructure(self):
        random_des = self.infrastructures[randint(0, len(self.infrastructures) - 1)]
        random_time = estimate_time(self.task, random_des)
        # 添加任务到最佳卸载设备等待队列中
        self.task.offload(random_des)
        # 卸载后将该任务所属车辆移动位置
        self.task.belong_vehicle.run(random_time)
        # print("vehicle id:" + str(self.task.belong_vehicle.id) + "  " + str(self.task.belong_vehicle))
        # 改变车辆所属时间戳，修正waiting time的计算
        self.task.belong_vehicle.refresh_timestamp(random_time)
        return random_time, random_des


# 返回指定卸载设备的预计消耗总时间
def estimate_time(task, infrastructure):
    return task.cal_calculate_time(infrastructure) + task.cal_transmission_time(infrastructure) \
           + task.cal_waiting_time(infrastructure)


def cal_total_time(per_tasks, vehicle_nums, algo="Benchmark"):
    # 读入数据
    edge_list, vehicle_list = data_reader()
    # 任务队列总消耗时间
    Total_Time = 0
    # 总调度队列
    simulation_task_list = []
    # 调度目的地计数器
    offload_des = {"VE": 0, "ES": 0}
    # 车辆队列
    # vehicles = [Vehicle(index, per_tasks) for index in range(vehicle_nums)]
    # vehicle_data说明：0.id 1.edge id 2.latitude 3.longitude 4.per_tasks
    vehicles = [Vehicle(vehicle_data[0], vehicle_data[4], vehicle_data[2], vehicle_data[3]) for vehicle_data in
                vehicle_list]
    # 将车辆队列携带的任务添加到总调度队列中
    for vehicle in vehicles:
        simulation_task_list += vehicle.task_queue

    # 打乱模拟任务序列顺序以模拟多线程乱序发射任务
    shuffle(simulation_task_list)

    # 初始化边缘服务器
    # edge_server_list = []
    # for lat in range(config.ROAD_START, config.ROAD_LENGTH, config.DEPLOY_INTERVAL):
    #     for long in range(config.ROAD_START, config.ROAD_LENGTH, config.DEPLOY_INTERVAL):
    #         edge_server_list.append(EdgeServer(long, lat))
    edge_server_list = [EdgeServer(edge_data[1], edge_data[2], edge_data[0]) for edge_data in edge_list]

    # 合并边缘服务器端和车辆终端
    server_list = edge_server_list + vehicles
    # server_list = edge_server_list

    # 遍历调度队列使用指定的算法计算总时延
    for index in range(len(simulation_task_list)):
        s = Solution(simulation_task_list[index], server_list)
        # 使用最优策略卸载任务
        if algo == "myalgo":
            dur_time, best_infra = s.offload_best_infrastructure()
        # 使用随即策略卸载任务
        elif algo == "Benchmark":
            dur_time, best_infra = s.offload_random_infrastructure()
        else:
            print("算法参数输入错误！")
            return False

        offload_des[best_infra.type] += 1
        Total_Time += dur_time

    # todo:利用率计算尚有问题
    running_server = 0
    for server in edge_server_list:
        if len(server.waiting_queue) != 0 and server.type == "ES":
            running_server += 1
    resource_uti = len(edge_server_list) / running_server

    print("*" * 10, "车辆数：%r，任务数：%r，总时间为：%r, 利用率：%r, 卸载设备情况为：%r"
          % (vehicle_nums, per_tasks, Total_Time, resource_uti, offload_des))

    return True
