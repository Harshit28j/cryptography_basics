import cipher as cp
file=open('file_en.txt',encoding='utf-8')
content=file.read()
cp_obj=cp.Cipher()
den_txt=cp_obj.decode(content,8)
print(den_txt)