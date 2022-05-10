import random
import hashlib
import time
import json

class Block:
    """initiates Block"""

    def __init__(self, prev_hash, data):
        self.data = data
        self.header = {'prev_hash': prev_hash, 'mkl_root': hashlib.sha256(json.dumps(data).encode()).hexdigest(), 'block_hash': None,
                       'nonce': None, 'timestamp': str(time.time()) }


