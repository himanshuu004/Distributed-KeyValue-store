import hashlib

class ConsistentHash:
    def __init__(self, nodes):
        self.nodes = nodes
        self.ring = {}
        for node in nodes:
            hash_val = self._hash(node)
            self.ring[hash_val] = node

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def get_node(self, key):
        if not self.ring:
            return None
        hash_val = self._hash(key)
        sorted_hashes = sorted(self.ring.keys())
        for node_hash in sorted_hashes:
            if hash_val <= node_hash:
                return self.ring[node_hash]
        return self.ring[sorted_hashes[0]]