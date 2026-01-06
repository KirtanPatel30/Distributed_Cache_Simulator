from collections import OrderedDict, defaultdict
import time

class Cache:
    def __init__(self, capacity, policy):
        self.capacity = capacity
        self.policy = policy
        self.store = OrderedDict()
        self.freq = defaultdict(int)

    def get(self, key):
        if key not in self.store:
            return None
        if self.policy == "lru":
            self.store.move_to_end(key)
        self.freq[key] += 1
        return self.store[key]

    def put(self, key, value):
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key] = value
        self.freq[key] += 1

        if len(self.store) > self.capacity:
            self.evict()

    def evict(self):
        if self.policy == "lru":
            self.store.popitem(last=False)
        else:
            k = min(self.freq, key=lambda x: self.freq[x])
            self.store.pop(k, None)
            self.freq.pop(k, None)
