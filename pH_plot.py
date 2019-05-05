import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def main():

    root_GNR = "/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData/GNR_pH"
    files = os.listdir(root_GNR)
    files_GNR = list(filter(lambda x: x[-4:]=='.csv', files))
    plot_GNR(files_GNR, root_GNR)

    root_CNT = "/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData/CNT_pH"
    files = os.listdir(root_CNT)
    files_CNT = list(filter(lambda x: x[-4:]=='.csv', files))
    plot_CNT(files_CNT, root_CNT)

    files_Si_pHVth = "/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData/Si_pH/pH_Vth.csv"
    files_Si_IdVg = "/home/yifu/PycharmProjects/CarbonPrj_Plot/RawData/Si_pH/IdVg.csv"
    plot_Si_pHVth(files_Si_pHVth)
    plot_Si_IdVg(files_Si_IdVg)

def plot_GNR(files_GNR, root_GNR):
    plt.figure()
    i = 1
    data = np.arange(3588).reshape(299, 12)
    data.dtype = np.float
    for file in files_GNR:
        pH = int(file[-5])
        if file[-6] == '1':
            pH = pH + 10
        tmp = pd.read_csv(root_GNR + '/' + file, header=None)
        tmp = np.array(tmp)
        data[:, 0] = tmp [:, 0]
        data[:, pH-1] = tmp[:, 1]

    while i < 12:
        Vg = data[:, 0]
        Ids = data[:, i]
        i = i + 1
        plt.plot(Vg, Ids, label="pH = " + str(i))

    plt.xlabel('Vg (V)')
    plt.ylabel('Ids (A)')
    plt.title('Transfer characteristics')
    plt.legend()
    plt.savefig('GNR_pH_transfer.PNG')
    plt.show()

def plot_CNT(files_CNT, root_CNT):
    plt.figure()
    i = 1
    data = np.arange(3588).reshape(299, 12)
    data.dtype = np.float
    for file in files_CNT:
        pH = int(file[-5])
        if file[-6] == '1':
            pH = pH + 10
        tmp = pd.read_csv(root_CNT + '/' + file, header=None)
        tmp = np.array(tmp)
        data[:, 0] = tmp [:, 0]
        data[:, pH-1] = tmp[:, 1]

    while i < 12:
        Vg = data[:, 0]
        Ids = data[:, i]
        i = i + 1
        plt.plot(Vg, Ids, label="pH = " + str(i))

    plt.xlabel('Vg (V)')
    plt.ylabel('Ids (A)')
    plt.title('Transfer characteristics')
    plt.legend()
    plt.savefig('CNT_pH_transfer.PNG')
    plt.show()

def plot_Si_pHVth(files_Si_pHVth):
    data = pd.read_csv(files_Si_pHVth, header=None)
    data = np.array(data)
    pH = data[:, 0]
    Vth = data[:, 1]
    plt.plot(pH, Vth)
    plt.xlabel('pH')
    plt.ylabel('Vth (V)')
    plt.title('pH - Vth relation')
    plt.savefig('Si_pH_Vth.PNG')
    plt.show()

def plot_Si_IdVg(files_Si_IdVg):
    data = pd.read_csv(files_Si_IdVg, header=None)
    data = np.array(data)
    plt.figure()
    pH = 2
    while pH < 13:
        Vg = data[301*(pH-2):301*(pH-1)-1, 0]
        Ids = data[301*(pH-2):301*(pH-1)-1, 1]
        plt.plot(Vg, Ids, label="pH = " + str(pH))
        pH = pH + 1

    plt.xlabel('Vg (V)')
    plt.ylabel('Ids (A)')
    plt.title('Transfer characteristics')
    plt.legend()
    plt.savefig('Si_pH_transfer.PNG')
    plt.show()

if __name__ == "__main__":
    main()
