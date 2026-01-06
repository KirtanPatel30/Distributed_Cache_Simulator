from sim.node import Node
import hashlib

class Cluster:
    def __init__(self, num_nodes, replication_factor, capacity_per_node, eviction_policy):
        self.nodes = [
            Node(i, capacity_per_node, eviction_policy)
            for i in range(num_nodes)
        ]
        self.n = num_nodes
        self.r = replication_factor

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def _get_nodes(self, key):
        start = self._hash(key) % self.n
        return [self.nodes[(start + i) % self.n] for i in range(self.r)]

    def get(self, key):
        for node in self._get_nodes(key):
            try:
                val = node.get(key)
                if val is not None:
                    return val
            except:
                continue
        return None

    def put(self, key, value):
        for node in self._get_nodes(key):
            try:
                node.put(key, value)
            except:
                continue
