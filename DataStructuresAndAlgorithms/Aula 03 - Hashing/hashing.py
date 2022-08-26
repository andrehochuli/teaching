import numpy as np
def hash_str(s):

    p = 31;
    m = 10**9 + 7;
    hash_value = 0;
    p_pow = 1;
    
    for c in s:
        
        hash_value = (hash_value + (1 + ord(c) - ord('a')) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    

    return hash_value;

def module(val,k):
    key = val%k
    return key


if __name__ == '__main__':

    hash_table = [[],[],[],[],[],[],[],[],[],[]]
    val = 12349

    for i in range(100):
        val = np.random.randint(1,10000000)
        hash_key = module(val,10)
        hash_table[hash_key].append(val)


    print(hash_table)
    
