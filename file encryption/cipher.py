import time
import sys

class Cipher(object):
	def decode(self,txt,k):
		print('Decoding....')
		key=k
		den=''
		den_index=0
		dencode=''
		char_index=0
		count=4
		initial=0
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

		return(den)

	def brute(self,txt):
			print('Brute Force HAcking.....')
			for key in range(1,40):
				print("Trying key",key)
				self.decode(txt,key)
				time.sleep(0.7)

	def encoding(self,txt):
		key=int(input('Enter the key to encrypt txt:>'))
		print(f'[Encrypting text...\n {txt}]\n')
		en=''
		txt=txt.upper()
		encode=''
		char_index=0
		en_index=0
		alpha_num='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .?'

		for letters in txt:
			if letters in alpha_num:
				char_index=alpha_num.find(letters)
				en_index=char_index+key

				if en_index>=len(alpha_num):
					en_index=en_index-len(alpha_num)
			en+=alpha_num[en_index]
		return(en)

		# for letters in en:
		# 	encode+=hex(ord(letters))
		# print('\n',encode)

def main():
	my_class=Encode()
