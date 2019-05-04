import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def main():

    root_dir = "/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData"
    files = os.listdir(root_dir)
    files_csv = list(filter(lambda x: x[-4:]=='.csv', files))

    plt.figure()
    for file in files_csv:
        pH = int(file[-5])
        if file[-6] == '1':
            pH = pH + 10
        print(pH)
        data = pd.read_csv(root_dir + '/' + file, header=None)
        data = np.array(data)
        Vg = data[:, 0]
        Ids = data[:, 1]
        plt.plot(Vg, Ids, label="pH = " + str(pH))

    plt.xlabel('Vg (V)')
    plt.ylabel('Ids (A)')
    plt.title('Transfer characteristics')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
