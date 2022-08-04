import os
import time


os.startfile('uart_for_project.exe')
time.sleep(2)


while True:
	mystring=input("enter string: ")
	print(mystring)
	start=time.time()
	file=open('data.txt',mode='w',encoding='utf8')
	#mystring="1 400 1 2 400 1"
	
	file.write(mystring)
	file.close()
	if mystring=="close":
		break



	return_string=""
	while return_string=="" or return_string==mystring:
		file=open('data.txt',mode='r',encoding='utf8')
		return_string=file.readline()
		file.close()
	print(return_string)

	end=time.time()
	print(end-start)

time.sleep(2)


# start=time.time()
# file=open('data.txt',mode='w',encoding='utf8')
# mystring="1 400 1 2 400 0"
# file.write(mystring)
# file.close()

# return_string=""
# while return_string=="" or return_string==mystring:
# 	file=open('data.txt',mode='r',encoding='utf8')
# 	return_string=file.readline()
# 	file.close()
# print(return_string)

# end=time.time()
# print(end-start)

# time.sleep(2)



# file=open('data.txt',mode='w',encoding='utf8')
# mystring="close"
# file.write(mystring)
# file.close()
