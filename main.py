from random import shuffle

from vehicle import Vehicle
from edge_server import EdgeServer
from offloading_strategy import Solution

# 总时间
Total_Time = 0

if __name__ == '__main__':
    simulation_task_list = []
    vehicles = [Vehicle(index) for index in range(20)]
    for vehicle in vehicles:
        simulation_task_list += vehicle.task_queue

    # 打乱模拟任务序列顺序以模拟多线程乱序发射任务
    shuffle(simulation_task_list)

    edge_server_list = [EdgeServer(loca) for loca in range(0, 300, 25)]
    edge_server_list += vehicles
    print(edge_server_list)

    while len(simulation_task_list):
        s = Solution(simulation_task_list.pop(), edge_server_list)
        # 使用最优策略卸载任务
        # dur_time, best_infra = s.offload_best_infrastructure()
        # 使用随即策略卸载任务
        dur_time, best_infra = s.offload_random_infrastructure()

        Total_Time += dur_time
        # print("Task %r, min time: %r, infra: %r" % (s.task.id, min_time, best_infra))
    for server in edge_server_list:
        print(server, server.waiting_queue)

    print("*"*10, "总时间为：%r" % Total_Time)
