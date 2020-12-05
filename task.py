from datetime import time
import config
from math import sqrt


class Task:
    data_size = config.DATA_SIZE
    # 开始分配时刻
    start_time = 0
    # 任务完成时刻
    end_time = 0
    # 抵达处理机时刻
    ready_time = 0
    # 结束运行时刻
    finish_time = 0

    def __init__(self, vehicle, id=0, solution=None):
        self.belong_vehicle = vehicle
        self.id = id
        self.solution = solution

    def __repr__(self):
        return "task:%r, from:%r ,data size:%r\n" % (self.id, self.belong_vehicle.id, self.data_size)

    def cal_transmission_time(self, infrastructure):
        vehicle = self.belong_vehicle
        length = exchange_distance(vehicle.latitude, vehicle.longitude, infrastructure.latitude,
                                   infrastructure.longitude)
        come_time = length / config.RAY_SPEED
        # 计算预设情况下汽车的接受回传数据时的位置
        after_latitude, after_longitude = self.belong_vehicle.get_after_run_location(come_time)
        length = exchange_distance(after_latitude, after_longitude, infrastructure.latitude, infrastructure.longitude)
        back_time = length / config.RAY_SPEED
        return come_time + back_time

    def cal_come_time(self, infrastructure):
        vehicle = self.belong_vehicle
        length = exchange_distance(vehicle.latitude, vehicle.longitude, infrastructure.latitude,
                                   infrastructure.longitude)
        come_time = length / config.RAY_SPEED
        return come_time

    def cal_waiting_time(self, infrastructure):
        self.start_time = self.belong_vehicle.timestamp
        self.ready_time = self.start_time + self.cal_come_time(infrastructure)

        if len(infrastructure.waiting_queue) > 0:
            waiting_time = infrastructure.waiting_queue[-1].finish_time - self.ready_time
        else:
            waiting_time = 0

        if waiting_time > 0:
            return waiting_time
        else:
            return 0

    def cal_calculate_time(self, infrastructure):
        return self.data_size / infrastructure.frequency

    def offload(self, infrastructure):
        self.finish_time = self.ready_time + self.cal_waiting_time(infrastructure) + self.cal_calculate_time(
            infrastructure)
        infrastructure.waiting_queue.append(self)


def exchange_distance(s_lat, s_long, d_lat, d_long):
    return sqrt(pow(s_lat - d_lat, 2) + pow(s_long - d_long, 2))
