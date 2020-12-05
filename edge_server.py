from infrastructure import Infrastructure
import config

class EdgeServer(Infrastructure):
    frequency = config.EDGE_FREQUENCY
    waiting_queue = []
    type = "ES"

    def __init__(self, location):
        self.location = location
        self.waiting_queue = list()

    def __repr__(self):
        return "edge_location: %r" % self.location