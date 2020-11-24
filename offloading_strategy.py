from random import randint

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
        random_des = self.infrastructures[randint(0, len(self.infrastructures)-1)]
        random_time = estimate_time(self.task, random_des)

        return random_time, random_des


def estimate_time(task, infrastructure):
    return task.cal_calculate_time(infrastructure) + task.cal_transmission_time(infrastructure) \
           + task.cal_waiting_time(infrastructure)
    # return task.cal_transmission_time(infrastructure)

