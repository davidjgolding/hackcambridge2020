#!/usr/bin/env python3
import time
import boto3
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show
import pylab

class Graph:
  def getData(self):
    bucket_name = 'hackathon18012020'
    s3_file_path = 'text.txt'

    save_as = 'data.txt'
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_file_path, save_as)

  def genGraph(self, labels, data, g_title, nme, v=1, id=0):
      vals = [0, 0, 0]
      leave_room = 0;
      for i in range(len(data[0])):
        if not int(data[v][i]):
            vals[0] += 1
        elif not int(data[0][i]) and int(data[v][i]):
            vals[1] += 1
        else:
            vals[2] += 1
        if ((i+1) < len(data[0]) and data[0][i] != data[0][i+1]):
            leave_room = leave_room + 1
      minutes = float((vals[2]*5)/60)
      on = float((vals[1]+vals[2])*5/60)
      figure(id, figsize=(6, 6))

      ax = axes([0.1, 0.1, 0.8, 0.8])

      vals_total = sum(vals)
      fracs = [float(val/vals_total) for val in vals]
      pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)
      title(g_title, bbox={'facecolor': '0.8', 'pad': 5})
      # show()
      pylab.savefig(nme)

      return minutes, on, leave_room


  def getGraphs(self):
    data = [[],[],[],[]]
    with open("data.txt", "r") as f:
        for line in f:
            l = line.replace(" ","")
            l = l.strip("\n")
            for i, char in enumerate(l):
                data[i].append(char)

    labels = 'LIGHTS OFF', 'REASONABLE', 'WASTED'
    a, b, c = self.genGraph(labels, data, "Light Energy Usage By Time", "light.png", id=0)

    labels = 'HEATING OFF', 'HEATING USED', 'WASTED'
    self.genGraph(labels, data, "Heating Usage By Time", "heating.png", v=2, id=1)

    labels = 'AC OFF', 'AC USED', 'WASTED'
    self.genGraph(labels, data, "AC Usage By Time", "ac.png", v=3, id=2)



    plt.figure(3, figsize=(6, 6))
    y = []

    for i in range(len(data[0])):
      if int(data[0][i]) and int(data[1][i]):
        y.append(1)
      else:
        y.append(0)
    x = [i*5 for i in range(len(y))]
    plt.plot(x, y)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Efficiency')
    plt.title('Wastage Over Time')
    plt.savefig('efficiency.png')
    return a, b, c

  def __init__(self):
      self.getData()


def main(test):
    g = Graph()
    x = g.getGraphs()
    print(str(x)[1:-1])
    return str(x)

if __name__ == "__main__":
    x=main(None)
