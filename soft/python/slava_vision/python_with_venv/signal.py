def make_signal(old_c,new_c,installation):
    dif=[0,0]
    signal=[1,0,0,2,0,1] #[0]-1 motor , [3]-2 motor ,[2],[5]-directions
    dif[0]=int(new_c[0])-int(old_c[0])
    dif[1] =int (new_c[1])- int(old_c[1])

    if (dif[0]<0):  #set directions
        signal[2]=1
    if (dif[1]<0):
        signal[5]=0

    if abs(dif[0])<20:
        dif[0]=0
    if abs(dif[1])<20:
        dif[1]=0

    signal[1]=int(abs(dif[0]/3.75/1.1)) #steps for motor 1 3.75 default
    signal[4] = int(abs(dif[1] / 3.2/1.1))  # steps for motor 1 3.2

    signal_string=str(installation)+';'
    for i in range(0,5):
        signal_string+=str(signal[i])+';'
    signal_string+=str(signal[5])
    return signal_string

if __name__=='__main__':
    new_coordinate=[200,200]
    old_coordinate=[100,100]
    signal = make_signal(old_coordinate, new_coordinate)
    print(signal)
    print(type(new_coordinate[0]))