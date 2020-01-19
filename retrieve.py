#!/usr/bin/env python3
import time
import boto3
import numpy as np
import math
import matplotlib.pyplot as plt

class Graph:
  def getData(self):
    bucket_name = 'hackathon18012020'
    s3_file_path = 'text.txt'

    save_as = 'data.txt'
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_file_path, save_as)

  def getGraphs(self):
    LightEnergy= 0.05
    HeatEnergy= 2
    ACEnergy= 15
    TimeDur= 100

    f= open("data.txt", "r")


    if f.mode == 'r':
        contents= f.read()

    SizeData= math.floor(len(contents)/8)

    if(SizeData<8000):
        TimeDur= SizeData/178.20
        if(TimeDur<1):
            TimeDur=1
        HeatData= np.array([])
        HeatData.resize((int(SizeData/TimeDur), 2))

        LightData= np.array([])
        LightData.resize((int(SizeData/TimeDur), 2))

        ACData= np.array([])
        ACData.resize((int(SizeData/TimeDur), 2))

        def ElementInFile(i, j):
            return int(contents[8*i+j*2])

        def Energy(i):
            return ((ElementInFile(i, 1)*LightEnergy, ElementInFile(i, 2)*HeatEnergy,ElementInFile(i, 3)*ACEnergy))

        for k in range(int(SizeData/TimeDur)):
            Wast= np.array((0., 0., 0.))
            Total= np.array((0., 0., 0.))
            i= 0
            for i in range(k*TimeDur, (k+1)*TimeDur):
                E= Energy(i)
                if(ElementInFile(i, 0)==0):
                    Wast= Wast+E
                Total= Total+E
            LightData[k], HeatData[k], ACData[k]= np.array((Wast, Total)).T

        fg, ax= plt.subplots()
        ax.plot(LightData)
        ax.set_title('Light Energy Consumption', pad=30.0, size='xx-large')
        ax.set_ylabel('Energy Consumption (in kJ)')
        ax.set_xlabel('Time (in hrs)')
        ax.set_xticklabels(np.arange(0, 25)*SizeData/17280)
        ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
        ax.set_xlim(left= 0, right=SizeData/TimeDur)
        ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
        fg.savefig('LightEnergy.png', bbox_inches='tight')

        fg, ax= plt.subplots()
        ax.plot(HeatData)
        ax.set_title('Heat Energy Consumption', pad=30.0, size='xx-large')
        ax.set_ylabel('Energy Consumption (in kJ)')
        ax.set_xlabel('Time (in hrs)')
        ax.set_xticklabels(np.arange(0, 25)*SizeData/17280)
        ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
        ax.set_xlim(left= 0, right=SizeData/TimeDur)
        ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
        fg.savefig('HeatEnergy.png', bbox_inches='tight')

        fg, ax= plt.subplots()
        ax.plot(ACData)
        ax.set_title('AC Energy Consumption', pad=30.0, size='xx-large')
        ax.set_ylabel('Energy Consumption (in kJ)')
        ax.set_xlabel('Time (in hrs)')
        ax.set_xticklabels(np.arange(0, 25)*SizeData/17280)
        ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
        ax.set_xlim(left= 0, right=SizeData/TimeDur)
        ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
        fg.savefig('ACEnergy.png', bbox_inches='tight')

        fg, ax= plt.subplots()
        ax.plot(LightData + HeatData + ACData)
        ax.set_title('Total Energy Consumption', pad=30.0, size='xx-large')
        ax.set_ylabel('Energy Consumption (in kJ)')
        ax.set_xlabel('Time (in hrs)')
        ax.set_xticklabels(np.arange(0, 25)*SizeData/17280)
        ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
        ax.set_xlim(left= 0, right=SizeData/TimeDur)
        ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
        fg.savefig('TotalEnergy.png', bbox_inches='tight')

    HeatData= np.array([])
    HeatData.resize((int(SizeData/TimeDur), 2))

    LightData= np.array([])
    LightData.resize((int(SizeData/TimeDur), 2))

    ACData= np.array([])
    ACData.resize((int(SizeData/TimeDur), 2))

    def ElementInFile(i, j):
        return int(contents[8*i+j*2])

    def Energy(i):
        return ((ElementInFile(i, 1)*LightEnergy, ElementInFile(i, 2)*HeatEnergy,ElementInFile(i, 3)*ACEnergy))

    for k in range(int(SizeData/TimeDur)):
        Wast= np.array((0., 0., 0.))
        Total= np.array((0., 0., 0.))
        i= 0
        for i in range(k*TimeDur, (k+1)*TimeDur):
            E= Energy(i)
            if(ElementInFile(i, 0)==0):
                Wast= Wast+E
            Total= Total+E
        LightData[k], HeatData[k], ACData[k]= np.array((Wast, Total)).T

    fg, ax= plt.subplots()
    ax.plot(LightData)
    ax.set_title('Light Energy Consumption', pad=30.0, size='xx-large')
    ax.set_ylabel('Energy Consumption (in kJ)')
    ax.set_xlabel('Time (in hrs)')
    ax.set_xticklabels(np.arange(0, 25))
    ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
    ax.set_xlim(left= 0, right=SizeData/TimeDur)
    ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
    fg.savefig('LightEnergy.png', bbox_inches='tight')

    fg, ax= plt.subplots()
    ax.plot(HeatData)
    ax.set_title('Heat Energy Consumption', pad=30.0, size='xx-large')
    ax.set_ylabel('Energy Consumption (in kJ)')
    ax.set_xlabel('Time (in hrs)')
    ax.set_xticklabels(np.arange(0, 25))
    ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
    ax.set_xlim(left= 0, right=SizeData/TimeDur)
    ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
    fg.savefig('HeatEnergy.png', bbox_inches='tight')

    fg, ax= plt.subplots()
    ax.plot(ACData)
    ax.set_title('AC Energy Consumption', pad=30.0, size='xx-large')
    ax.set_ylabel('Energy Consumption (in kJ)')
    ax.set_xlabel('Time (in hrs)')
    ax.set_xticklabels(np.arange(0, 25))
    ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
    ax.set_xlim(left= 0, right=SizeData/TimeDur)
    ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
    fg.savefig('ACEnergy.png', bbox_inches='tight')

    fg, ax= plt.subplots()
    ax.plot(LightData + HeatData + ACData)
    ax.set_title('Total Energy Consumption', pad=30.0, size='xx-large')
    ax.set_ylabel('Energy Consumption (in kJ)')
    ax.set_xlabel('Time (in hrs)')
    ax.set_xticklabels(np.arange(0, 25))
    ax.set_xticks(np.arange(0, 25)*60*12/TimeDur)
    ax.set_xlim(left= 0, right=SizeData/TimeDur)
    ax.legend(['Energy Wasted', 'Energy Consumed'],loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=2, borderaxespad=0, frameon=False)
    fg.savefig('TotalEnergy.png', bbox_inches='tight')

  def __init__(self):
      pass
      # self.getData()


def main(test):
    g = Graph()
    g.getGraphs()
    return "succ"

if __name__ == "__main__":
    x=main(None)
