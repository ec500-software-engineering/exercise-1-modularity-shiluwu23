# copyright @Kainan Liu @Wenjie Luo
def read_data(path):
    try:
        with open(path,'r') as f:
            time = []
            value = []
            data = f.readline()
            while data:
                if data:
                    value.append(float(data))
                else:
                    print("Empty data file!\n")
                    return 2
                data = f.readline()
        print("Read data successfully\n")
        return value
    except:
        print("Error:No input data\n")
