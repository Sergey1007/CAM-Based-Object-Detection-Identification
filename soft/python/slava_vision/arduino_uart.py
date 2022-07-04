import serial
import time

def turn_motor(my_list):
    res_str=str(my_list[0])+' '+str(my_list[1])+' '+str(my_list[2])
    serialcomm.write(res_str.encode())
    #time.sleep(0.5)  #возможно понадобиться , не убирать
    #print(serialcomm.readline().decode('ascii'))
    #serialcomm.close()

if __name__=='__main__':
    set_port=input("enter your com-port: ")
    serialcomm = serial.Serial(set_port,1000000)
    serialcomm.timeout = 1
    time.sleep(1)
    my_list=[]
    for i in range(0,3):
        my_list.append(input())
    turn_motor(my_list)

