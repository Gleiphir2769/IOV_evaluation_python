import random
from task import Task


class Vehicle:
    frequency = 3000
    speed = 20
    task_queue = []
    capacity = 1
    timestamp = 0

    def __init__(self):
        self.location = random.randint(0, 100)
        for i in range(5):
            task = Task(self, i)
            self.task_queue.append(task)

    def run(self, time):
        self.location = self.location + self.speed*time

    def tackle(self, task):
        return task.data_size/self.frequency

    # def cal_transmission_time(self, task):
    #     come_time = abs(self.location-task.belong_vehicle.location)
    #     self.run(come_time)
    #     back_time = abs(self.location-task.belong_vehicle.location)
    #     return come_time+back_time


    def push_task(self):
        return self.task_queue.pop(0)

    def __repr__(self):
        return "vehicle with frequency %r, speed %r, task queue %r" % (self.frequency, self.speed, self.task_queue)

if __name__ == '__main__':
    v = Vehicle()
    print(v)
