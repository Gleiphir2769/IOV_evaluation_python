from datetime import time
Ray_speed = 100000

class Task:
    data_size = 2000

    def __init__(self, vehicle, id, solution=None):
        self.belong_vehicle = vehicle
        self.id = id
        self.solution = solution

    def __repr__(self):
        return "task:%r, data size:%r\n" % (self.id, self.data_size)

    def cal_transmission_time(self, infrastructure):
        length = abs(self.belong_vehicle.location - infrastructure.location)
        come_time = length/Ray_speed
        self.belong_vehicle.run(come_time)
        length = abs(self.belong_vehicle.location - infrastructure.location)
        back_time = length/Ray_speed
        return come_time + back_time

    def cal_waiting_time(self, infrastructure):
        waiting_time = 0 - self.belong_vehicle.timestamp
        for wait_task in infrastructure.waiting_queue:
            waiting_time += wait_task.cal_calculate_time(infrastructure)
        if waiting_time > 0:
            return waiting_time
        else:
            return 0

    def cal_calculate_time(self, infrastructure):
        return self.data_size/infrastructure.frequency

    def offload(self, infrastructure):
        infrastructure.waiting_queue.apeend(self)