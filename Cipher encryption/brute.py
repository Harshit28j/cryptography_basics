import time
import sys
res='Python?'
res=res.upper()

def brute(k):
	key=k
	den=''
	den_index=0
	dencode=''
	char_index=0
	count=4
	initial=0
	txt='Z94RYXJ'
	alpha_num='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .?'
	if '0x' in txt:	#decode hex if true
		print('Decoding hex')
		for i in range(0,len(txt),4):
			txt_4=txt[initial:count]
			initial=count
			count+=4
			char=chr(int(txt_4,16))
			dencode+=char
	else:
		dencode=txt

	for letters in dencode:
		if letters in alpha_num:
			char_index=alpha_num.find(letters)
			den_index=char_index-key

		den+=alpha_num[den_index]

	if den==res:
		print("\nKEy FOUND!",k)
		print(f"Actual text is\n[{den}]")
		sys.exit()
	else:
		print(den)


print('Brute Force HAcking.....')
for key in range(1,40):
	print("Trying key",key)
	brute(key)
	time.sleep(0.7)