import smbus
import time

bus=smbus.SMBus(1)
SLAVE_ADDRESS=0x04

def request_reading():
	reading=int(bus.read_byte(SLAVE_ADDRESS))
	print(reading)

def send_symbol(symbol):
	bus.write_byte(SLAVE_ADDRESS,symbol)

def send_arr(data):
	bus.write_i2c_block_data(SLAVE_ADDRESS,data[0],data[1:])

if  __name__=='__main__':
	while True:
		data=[]
		for _ in range (3):
			symbol=int(input("enter value: "))
			data.append(symbol)
		print(data)
		send_arr(data)

