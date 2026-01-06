from sim.cache import Cache

class Node:
    def __init__(self, node_id, capacity, eviction):
        self.node_id = node_id
        self.cache = Cache(capacity, eviction)
        self.alive = True

    def get(self, key):
        if not self.alive:
            raise Exception("Node down")
        return self.cache.get(key)

    def put(self, key, value):
        if not self.alive:
            raise Exception("Node down")
        self.cache.put(key, value)
