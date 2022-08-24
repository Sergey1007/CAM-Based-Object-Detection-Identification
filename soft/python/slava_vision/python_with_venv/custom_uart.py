import os
import time
import subprocess

def connect_to_serialport():
    file=open('signal.bin',mode='wb')
    file.close()
    subprocess.Popen('uart_for_project.exe \\\\.\\COM5')
    time.sleep(2)


def transmit_string_with_receive(signal):
    #transmit data
    start=time.time()
    file=open('signal.bin',mode='w')
    file.write(signal)
    file.close()

    #receive data
    return_string=b''
    while True:
        file=open('signal.bin',mode='rb')
        return_string=file.readline()
        if return_string==b'1' or return_string==b'2':
            break
        file.close()
    # print(return_string)

    end=time.time()
    #print(end-start)
    return return_string


def close_port():
    file=open('signal.bin',mode='wb')
    file.write(b'close')
    file.close()



if __name__=='__main__':
    connect_to_serialport()
    mystring = '1;1;0;0;2;200;1'
    return_string=transmit_string_with_receive(mystring)
    print(return_string)
    close_port()

