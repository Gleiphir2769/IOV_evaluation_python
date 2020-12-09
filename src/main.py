from src.offloading_strategy import cal_total_time

def work_script(filename):
    print("#"*25, "开始处理%r，结果为：" % filename)
    print("Benchmark:")
    cal_total_time(filename)
    print("real:")
    cal_total_time(filename, "real")
    print("myalgo:")
    cal_total_time(filename, "myalgo")


if __name__ == '__main__':
    # 分组实验问题 + 真实任务流问题
    work_script("data_8.1~8.15_slip_to_1000")
    work_script("data_8.16~8.31_slip_to_1000")
    work_script("data_9.1~9.15_slip_to_1000")
    work_script("data_9.16~9.30_slip_to_1000")
    work_script("data_10.1~10.15_slip_to_1000")
    work_script("data_10.16~10.31_slip_to_1000")
    work_script("data_11.1~11.15_slip_to_1000")
    work_script("data_11.16~11.30_slip_to_1000")

    # print("车辆数为20， 任务数变化区间为5-50的对照试验：")
    # for per_tasks in range(5, 55, 5):
    #     cal_total_time(per_tasks, 20, "myalgo")
    # for per_tasks in range(5, 55, 5):
    #     cal_total_time(per_tasks, 20)
    #
    # print("任务数为20， 车辆数变化区间为5-50的对照实验：")
    # for vehicle_nums in range(5, 55, 5):
    #     cal_total_time(20, vehicle_nums, "myalgo")
    # cal_total_time(1, 20, "myalgo")


