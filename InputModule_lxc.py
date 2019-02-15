#Copyright Xiaocheng Liang xcliang@bu.edu
#Input Module

'''
Expecting receive data from monitor devices(blood oxygen, blood pressure, pulse)
Now receive data from other source file(txt file)
Format: float
'''

def readdata(path):
        #Since we do not have data from the sensor now, we assuse that data is already in txt file
        try:
            with open(path, 'r') as f:
                read = f.read().split()

        except Exception:
            print("Reading data error")

        if len(read)==0:
            print("empty data")
        res = [float(i) for i in read]

        return res