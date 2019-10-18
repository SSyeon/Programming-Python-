f = open("data.bin", "wb") #wb는 바이트 단위로
byte_arr=bytes([255,0,127])

f.write(byte_arr)
 
f.close()