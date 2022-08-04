import os
import time

def connect_to_serialport():
    os.startfile('uart_for_project.exe')
    time.sleep(2)

def transmit_string(mystring):
    start = time.time()
    file = open('data.txt', mode='w', encoding='utf8')
    file.write(mystring)
    file.close()
    if mystring == "close":
        return "close"

    return_string = ""
    while return_string == "" or return_string == mystring:
        file = open('data.txt', mode='r', encoding='utf8')
        return_string = file.readline()
        file.close()
    end = time.time()
    print(end - start)
    return return_string




if __name__=='__main__':
    connect_to_serialport()
    mystring = input("enter string: ")
    print(mystring)
    return_string=transmit_string(mystring)
    print(return_string)

