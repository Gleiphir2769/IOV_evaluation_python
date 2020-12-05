import random
from task import Task
from infrastructure import Infrastructure
import config


class Vehicle(Infrastructure):
    frequency = config.VEHICLE_FREQUENCY
    speed = config.SPEED
    capacity = config.VEHICLE_CAPACITY
    timestamp = config.START_TIMESTAMP
    type = "VE"

    # 成员变量为可变对象时必须万分小心，注意引用的问题
    def __init__(self, id, vehicle_nums):
        self.location = int(random.randint(config.ROAD_START, config.ROAD_LENGTH))
        self.id = id
        self.task_queue = list()
        for i in range(vehicle_nums):
            task = Task(self, i)
            self.task_queue.append(task)
        self.waiting_queue = list()

    def run(self, time):
        self.location += self.speed*time
        # 如果车辆位置越界则回到道路初始位置，模拟环形道路
        self.location = self.location % config.ROAD_LENGTH

    def get_after_run_location(self, time):
        return self.location + self.speed*time

    def tackle(self, task):
        return task.data_size/self.frequency

    def refresh_timestamp(self, time):
        self.timestamp += time

    # def cal_transmission_time(self, task):
    #     come_time = abs(self.location-task.belong_vehicle.location)
    #     self.run(come_time)
    #     back_time = abs(self.location-task.belong_vehicle.location)
    #     return come_time+back_time 


    # def push_task(self):
    #     return self.task_queue.pop(0)

    # def __repr__(self):
    #     return "vehicle with location %r, task queue %r, waiting queue %r" % (self.location, self.task_queue, self.waiting_queue)
    def __repr__(self):
        return "vehicle in %r" % self.location

if __name__ == '__main__':
    v = Vehicle()
    print(v)
