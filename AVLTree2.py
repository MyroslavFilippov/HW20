from sortedcontainers import SortedDict
import random
import time

class AVLTree:
    def __init__(self):
        self.tree = SortedDict()

    def insert(self, key):
        self.tree[key] = None

    def delete(self, key):
        if key in self.tree:
            del self.tree[key]

    def find(self, key):
        return key in self.tree

# Function to generate random datasets
def generate_random_data(size):
    return random.sample(range(1, size * 10), size)

# Measure time complexity
def measure_time_complexity(tree, data):
    start_time = time.time()
    for item in data:
        tree.insert(item)
    for item in data:
        tree.delete(item)
    return time.time() - start_time

# Generate 100 random datasets and measure time complexity
total_time = 0
for _ in range(100):
    data = generate_random_data(100)
    avl_tree = AVLTree()
    total_time += measure_time_complexity(avl_tree, data)

average_time = total_time / 100
print("Average time complexity for insertion and deletion in AVL tree with 100 random datasets:", average_time)