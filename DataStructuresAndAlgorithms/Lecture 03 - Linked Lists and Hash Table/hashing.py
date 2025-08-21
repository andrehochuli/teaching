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

	index = hash_str('Abacadabra')
	print(index)
	index = hash_str('Abacadabrasadasdasd')
	print(index)
	
	index = hash_str('AbacadabrA')
	print(index)
