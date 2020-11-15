
from vehicle import Vehicle
from edge_server import EdgeServer
from task import Task
from offloading_strategy import Solution



if __name__ == '__main__':
    v = Vehicle(1)
    edge_server_list = [EdgeServer(loca) for loca in range(0, 200, 25)]
    edge_server_list.append(v)
    print(edge_server_list, v.location)

    while len(v.task_queue):
        s = Solution(v.task_queue.pop(), edge_server_list)
        min_time, best_infra = s.offload_best_infrastructure()
        print("Task %r, min time: %r, infra: %r" % (s.task.id, min_time, best_infra))
    for server in edge_server_list:
        print(server.waiting_queue)
