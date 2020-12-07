from infrastructure import Infrastructure
import config


class EdgeServer(Infrastructure):
    frequency = config.EDGE_FREQUENCY
    waiting_queue = []
    type = "ES"

    def __init__(self, latitude, longitude, id=0):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.waiting_queue = list()

    def __repr__(self):
        # return "edge_latitude: %r, longitude: %r" % self.latitude, self.longitude
        return "edge server id: %r" % self.id
