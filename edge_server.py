from infrastructure import Infrastructure


class EdgeServer(Infrastructure):
    frequency = 3000
    waiting_queue = []
    location = 0

    def __init__(self, location):
        self.location = location
        self.waiting_queue = list()

    def __repr__(self):
        return "edge_location: %r" % self.location