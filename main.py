
import hashlib

NONCE_LIMIT = 100000000
ZEROS = 5

def mining(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_find = hashlib.sha256(base_text.encode()).hexdigest()
        if hashlib.startswith("0" * ZEROS):
            print(f" Found hash with nonce {nonce} ")
            return hash_find
    
    return -1


