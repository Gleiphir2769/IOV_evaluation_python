import random
from src.task import Task
from src.infrastructure import Infrastructure
from src import config
import math


class Vehicle(Infrastructure):
    frequency = config.VEHICLE_FREQUENCY
    capacity = config.VEHICLE_CAPACITY
    timestamp = config.START_TIMESTAMP
    type = "VE"

    # 成员变量为可变对象时必须万分小心，注意引用的问题
    def __init__(self, id, per_tasks, latitude=random.randint(config.ROAD_START, config.ROAD_LENGTH),
                 longitude=random.randint(config.ROAD_START, config.ROAD_LENGTH), real_dis_edge=None):
        self.latitude = latitude
        self.longitude = longitude
        speed_val = 20
        speed_angel = random.uniform(0, 2 * 3.14)
        self.speed = (speed_val, speed_angel)
        self.id = id
        self.task_queue = list()
        for i in range(per_tasks):
            task = Task(self, i, None, real_dis_edge)
            self.task_queue.append(task)

        self.waiting_queue = list()

    def run(self, time):
        # # 对经纬度取余防止越界
        speed_val, speed_angel = self.speed
        self.latitude = (self.latitude + exchange_dis_to_lat(speed_val, speed_angel, time)) % config.ROAD_LENGTH
        self.longitude = (self.longitude + exchange_dis_to_long(speed_val, speed_angel, time)) % config.ROAD_LENGTH

    def get_after_run_location(self, time):
        speed_val, speed_angel = self.speed
        may_lat = (self.latitude + exchange_dis_to_lat(speed_val, speed_angel, time)) % config.ROAD_LENGTH
        may_long = (self.longitude + exchange_dis_to_long(speed_val, speed_angel, time)) % config.ROAD_LENGTH
        return may_lat, may_long

    def tackle(self, task):
        return task.data_size / self.frequency

    def refresh_timestamp(self, time):
        self.timestamp += time

    def __repr__(self):
        return "vehicle in %r, %r" % (self.latitude, self.longitude)


def exchange_dis_to_lat(speed_val, speed_angel, time):
    return ((speed_val * math.cos(speed_angel)) * time)/10


def exchange_dis_to_long(speed_val, speed_angel, time):
    return ((speed_val * math.sin(speed_angel)) * time)/10
