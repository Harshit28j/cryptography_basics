#affine cipher decryption
# f(x)=Ax+B
# A and B are keys x is plaintext index
#condtions
# 0<=A<=chr_len
# 1<=B<=chr_len
# GCD (key and symbol len)

import sys
txt='Ba16RARuQ1d93LQ1DDARaQGAlXa6'
l='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
key=2894

def gcd(x,y):
	while x!=0:
		x,y=y%x,x
	return(y)

def check_keys(x,y):
	if x==0:
		print('key is weak choose a different key')
		sys.exit()
	if y==1:
		print('key is weak choose a different key')
		sys.exit()
	if x<0 or y<0 or y>len(l)-1:
		print('key must be greater than 0 and between length of symbols')
		sys.exit()
	
	if gcd(x,y)!=1:
		print('Choose a different key this key is not relatively prime to length of symbols')
		sys.exit()

def key_part(key):
	key_A=key//len(l)
	key_B=key%len(l)
	return(key_A,key_B)

def encryption(txt):
	en_txt=''
	index=0
	A,B=key_part(key)
	check_keys(A,B)
	for letters in txt:
		if letters in l:
			index=l.find(letters)
			en_txt+=l[(index*A+B)%len(l)]#f(x)=Ax+B
	return(en_txt)

def findModInverse(a, m): #euler's algo concept
	if gcd(a, m) != 1:
		return None
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2),(u3 - q * v3), v1, v2, v3
	return(u1 % m)

def decryt(message):
	keyA, keyB = key_part(key)
	check_keys(keyA, keyB)
	plaintext = ''
	modInverseOfKeyA = findModInverse(keyA, len(l))
	for symbol in message:
		if symbol in l:
			symbolIndex = l.find(symbol)
			plaintext += l[(symbolIndex - keyB) * modInverseOfKeyA %len(l)]
	return(plaintext)

print(decryt(txt))
