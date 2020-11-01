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

#plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
###########################################################################
bool zoom=True; 
linewidth=1.2
file='fileo21.dat'
###########################################################################


data=np.loadtxt(file,usecols=np.arange(0,23))
x=data[:,0]		#3-7 1pierw(z30) 8-12 z50 13-17 z30 18-22 z0// total s p d f 
total=data[:,1]
p1=0.2*data[:,3]
p2=data[:,8]
p3=data[:,13]
p4=data[:,18]



fig,ax=plt.subplots()
ax.plot(x,total,'black',linewidth=linewidth,label='Total')
ax.plot(x,p1,linewidth=linewidth,label='Zn')
ax.plot(x,p2,linewidth=linewidth,label='Sn')
ax.plot(x,p3,linewidth=linewidth,label='Te')
ax.plot(x,p4,linewidth=linewidth,label='Vac')
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))

ax.yaxis.set_major_locator(MultipleLocator(3))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.set_ylim(ymin=0)

ax.set_xlim(min(x),max(x))
#ax.set_xlim(-0.08,0.08)
ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
ax.legend(frameon=False)
ax.tick_params(which='both',direction='in',top=True,right=True)

ax.plot([0,0],[-1,10],'magenta',linestyle='--',alpha=0.4)
ax.text(0, 10.5, r'$E_F$', fontsize=10,rotation=0)

plt.xlabel(r'$E-E_F$ [Ry] ',fontsize='large')
plt.ylabel('States/Ry',fontsize='large')
plt.title(u'$Sn_{0.98}Zn_{0.02}Te$ + 0.5 $\%$ $Vac_{Sn}$') # numerki z pliku i nazwa domieszki też

fig.set_size_inches(12.8,7.2)

# plt.savefig("ayya.png", bbox_inches = 'tight',
#     pad_inches = 0)

plt.show()