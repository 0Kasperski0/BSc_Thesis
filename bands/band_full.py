# -*- coding: utf-8 -*- 
import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
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


file1="data/zn0.0.dat"
file2="data/vac0.02.dat"
file3="data/in0.02.dat"
file4="data/zn0.015.dat"



###########################################################################
zoom=True 
linewidth=0.8
offset_l=0
offset_r=0
###########################################################################
data1=np.loadtxt(file1,usecols=np.arange(0,3))
data2=np.loadtxt(file2,usecols=np.arange(0,3))
data3=np.loadtxt(file3,usecols=np.arange(0,3))
data4=np.loadtxt(file4,usecols=np.arange(0,3))

print(data1)
x1=data1[:,0]
band1=data1[:,1]
err1=data1[:,2]

x2=data2[:,0]
band2=data2[:,1]
err2=data2[:,2]

x3=data3[:,0]
band3=data3[:,1]
err3=data3[:,2]

x4=data4[:,0]
band4=data4[:,1]
err4=data4[:,2]

fig,ax=plt.subplots()
#ax.errorbar(x1,band1,yerr=err1'red',label='0.0',marker='o',linestyle = 'None',alpha=1,markersize=3)




# ax.errorbar(x4,band4,yerr=err4,fmt='.',markersize=1,capsize=2,capthick=1,label=r'$\mathrm{Zn}_{0.032}$')
# ax.errorbar(x3,band3,yerr=err3,fmt='.',markersize=1,capsize=2,capthick=1,label=r'$\mathrm{Zn}_{0.02}$')
# ax.errorbar(x2,band2,yerr=err2,fmt='.',markersize=1,capsize=2,capthick=1,label=r'$\mathrm{Zn}_{0.01}$')
# ax.errorbar(x1,band1,yerr=err1,fmt='.',markersize=1,capsize=2,capthick=1,label=r'$\mathrm{Zn}_{0}$')
# ax.plot(x2,band2,'green',label='0.0',marker='^',linestyle = 'None',alpha=1,markersize=3)
# ax.plot(x3,band3,'blue',label='0.0',marker='P',linestyle = 'None',alpha=1,markersize=3)''
# indexs_to_order_by = band2.argsort()
# x2=x2[indexs_to_order_by]
# band2=band2[indexs_to_order_by]

x1=x1
band1=band1
filename='zn00.pgf'

ax.plot(x1,band1,marker='o',linestyle='none',alpha=1,markersize=1)
ax.plot(x1,x1*0,color='magenta',linestyle='--',alpha=0.4)
ax.set_ylim(ymin=-3.2,ymax=3.2)
#print(max(x1)/454)
mylist = list(set(x1))
# mylist=mylist.sort()
# print(len(mylist))

mylist.sort()
print(mylist)




plt.plot([mylist[79],mylist[79]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[154],mylist[154]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[219],mylist[219]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[259],mylist[259]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[339],mylist[339]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[399],mylist[399]], [-10,10],color='black',linewidth=1)
plt.plot([mylist[454],mylist[454]], [-10,10],color='black',linewidth=1)


plt.text(mylist[0]-0.025, -3.75, r'$\Gamma$', fontsize=14)
plt.text(mylist[79]-0.035, -3.75, 'X', fontsize=14)
plt.text(mylist[156]-0.035, -3.75, 'L', fontsize=14)
plt.text(mylist[219]-0.047, -3.75, 'W', fontsize=14)
plt.text(mylist[259]-0.034, -3.75, 'K', fontsize=14)
plt.text(mylist[339]-0.025, -3.75, r'$\Gamma$', fontsize=14)
plt.text(mylist[399]-0.028, -3.75, 'L', fontsize=14)
plt.text(mylist[454]-0.025, -3.75, r'$\Sigma$', fontsize=14)


ax.set_xlim(xmin=min(x1),xmax=max(x1))
ax.set_xticklabels([])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) 


# ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
# ax.legend(frameon=False)

# plt.text(0.11, 0.05, 'L', fontsize=14, transform=plt.gcf().transFigure)
# plt.text(0.88, 0.05, r'$\Sigma$', fontsize=14, transform=plt.gcf().transFigure)
# plt.text(0.88, 0.05, r'$a)$', fontsize=14, transform=plt.gcf().transFigure)
# plt.text(0.8, 0.8, r'$\textbf{(a)}$', fontsize=12, transform=plt.gcf().transFigure)

# print(0.00622647253*50)
plt.ylabel('Re(E) [eV]',fontsize='large')


# fig.set_size_inches(6.69423/2,4)
scale=1.1
large_scale=1.15
fig.set_size_inches(w=6.69423*large_scale+0.01384,h=6.69423*0.6*large_scale*0.8) #16:9

plt.savefig(filename,
			 pad_inches = 0,
		     bbox_inches='tight',
		     dpi=200)	