
from vehicle import Vehicle
from edge_server import EdgeServer
from task import Task

if __name__ == '__main__':
    v = Vehicle()
    edge_server_list = [EdgeServer(loca) for loca in range(0, 200, 25)]
