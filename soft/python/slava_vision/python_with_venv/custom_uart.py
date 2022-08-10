import os
import time

def connect_to_serialport():
    os.startfile('uart_for_project.exe')
    time.sleep(2)

def transmit_string(mystring):

    file = open('data.txt', mode='w', encoding='utf8')
    file.write(mystring)
    file.close()
    if mystring == "close":
        return "close"

def receive_string(mystring):
    return_string = ""
    while return_string == "" or return_string == mystring:
        file = open('data.txt', mode='r', encoding='utf8')
        return_string = file.readline()
        file.close()
    return return_string

def transmit_with_receive(mystring):
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
    return return_string



if __name__=='__main__':
    connect_to_serialport()
    mystring = input("enter string: ")
    print(mystring)
    return_string=transmit_string(mystring)
    print(return_string)

