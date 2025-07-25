import requests
from consistent_hash import ConsistentHash

# Define 3 nodes (we'll run these later)
nodes = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002"]
hash_ring = ConsistentHash(nodes)

def put(key, value):
    node = hash_ring.get_node(key)
    url = f"{node}/put"
    response = requests.post(url, json={"key": key, "value": value})
    print(f"PUT {key} → {node}: {response.json()}")

def get(key):
    node = hash_ring.get_node(key)
    url = f"{node}/get/{key}"
    response = requests.get(url)
    print(f"GET {key} → {node}: {response.json()}")

# Test
if __name__ == "__main__":
    put("name", "Praachi")
    put("city", "San Francisco")
    get("name")
    get("city")