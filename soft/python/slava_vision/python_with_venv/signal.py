def make_signal(old_c,new_c):
    dif=[0,0]
    signal=[1,0,0,2,0,1] #[0]-1 motor , [3]-2 motor ,[2],[5]-directions
    dif[0]=new_c[0]-old_c[0]
    dif[1] = new_c[1]- old_c[1]

    if (dif[0]<0):  #set directions
        signal[2]=1
    if (dif[1]<0):
        signal[5]=0

    step=1.8/8
    verticale_angle=41  #set steps
    horizontal_angle=54
    horizontal_koef=640/horizontal_angle
    vetical_koef=480/verticale_angle
    signal[1]=int(abs(dif[0]/horizontal_koef/step)) #steps for motor 1
    signal[4] = int(abs(dif[1] / vetical_koef/step))  # steps for motor 1

    return signal