import sys


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
        best_des.waiting_queue.append(self.task)
        self.task.belong_vehicle.run(min_time)
        self.task.belong_vehicle.refresh_timestamp(min_time)
        return min_time, best_des


def estimate_time(task, infrastructure):
    return task.cal_calculate_time(infrastructure) + task.cal_transmission_time(infrastructure) \
           + task.cal_waiting_time(infrastructure)
    # return task.cal_transmission_time(infrastructure)

