f=open("data.bin","rb")

# byte_arr=[]

data = f.read()

print(data)
for item in data:
    print(item)

f.close()