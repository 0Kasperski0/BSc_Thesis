# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator
import numpy as np
import math as m
import seaborn as sns; #sns.set()
import pandas as pd 
import sys
from datetime import datetime
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import re
import os


file1="data/dos.dat"
file2="data/dos2.dat"
file3="data/dos3.dat"


print(file3)

###########################################################################
zoom=True 
linewidth=0.8
offset_l=20
offset_r=1
###########################################################################
data1=np.loadtxt(file1,usecols=np.arange(0,23))
data2=np.loadtxt(file2,usecols=np.arange(0,23))
data3=np.loadtxt(file3,usecols=np.arange(0,23))

x1=data1[offset_l:-offset_r,0]
total1=data1[offset_l:-offset_r,1]
x2=data2[offset_l:-offset_r,0]
total2=data2[offset_l:-offset_r,1]
x3=data3[offset_l:-offset_r,0]
total3=data3[offset_l:-offset_r,1]

fig,ax=plt.subplots()
ax.plot(x1,total1,'red',linewidth=linewidth,label='BZ:420 Im(E): 0,0005',linestyle='--',alpha=1)
ax.plot(x2,total2,'green',linewidth=linewidth,label='BZ:4200 Im(E): 0,00005',linestyle='--',alpha=1)
ax.plot(x3,total3,'blue',linewidth=linewidth,label='BZ:4200 Im(E): 0.00001',linestyle='--',alpha=1)

ax.yaxis.set_major_locator(MultipleLocator(3))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.set_ylim(ymin=0)

if zoom==False:
		#ax.set_xlim(min(x),max(x))
		ax.set_xlim(-0.85,0.85)
		ax.set_ylim(0,25)
		ax.xaxis.set_major_locator(MultipleLocator(0.2))
		ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
		ax.xaxis.set_minor_locator(MultipleLocator(0.02))

else:
	ax.set_xlim(0,0.04)
	ax.set_ylim(0,1.5)
	ax.xaxis.set_major_locator(MultipleLocator(0.02))
	ax.xaxis.set_major_formatter(FormatStrFormatter('%1.2f'))
	ax.xaxis.set_minor_locator(MultipleLocator(0.004))


ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
ax.legend(frameon=False)
ax.tick_params(which='both',direction='in',top=True,right=True)
ax.tick_params(which='major', width=1.5,length=5)
ax.plot([0,0],[-1,10],'magenta',linestyle='--',alpha=0.4)
ax.text(0, 10.5, r'$E_F$', fontsize=10,rotation=0)

plt.xlabel(r'$E-E_F$ [Ry] ',fontsize='large')
plt.ylabel('States/Ry',fontsize='large')
plt.title(u'Porównanie parametrów DOS RCPA')
fig.set_size_inches(12.8,7.2)
plt.savefig('porow_dos.png',dpi=500)