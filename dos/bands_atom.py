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

directory='data/'
for filename in os.listdir(directory):
	if filename.endswith(".dat"):
		print(filename)
		#plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
		###########################################################################
		zoom=False 
		linewidth=1.2
		file=directory+filename
		f_conc= str(re.search('snte_(.*)-(.*).dat', file).group(2))
		f_dop=str(re.search('snte_(.*)-(.*).dat', file).group(1))
		offset_l=20
		offset_r=1
		###########################################################################


		data=np.loadtxt(file,usecols=np.arange(0,23))
		x=data[offset_l:-offset_r,0]		#3-7 1pierw(z30) 8-12 z50 13-17 z30 18-22 z0// total s p d f 
		total=data[offset_l:-offset_r,1]
		p1=data[offset_l:-offset_r,3]
		p2=data[offset_l:-offset_r,8]
		p3=data[offset_l:-offset_r,13]
		p4=data[offset_l:-offset_r,18]



		fig,ax=plt.subplots()
		ax.plot(x,total,'black',linewidth=linewidth,label='Total')
		if f_dop!='Vac':
			ax.plot(x,p1,linewidth=linewidth,label=f_dop)
		ax.plot(x,p2,linewidth=linewidth,label='Sn')
		ax.plot(x,p3,linewidth=linewidth,label='Te')
		#ax.plot(x,p4,linewidth=linewidth,label='Vac')


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
			ax.set_xlim(-0.08,0.08)
			ax.set_ylim(0,21)
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

		if f_dop != "Vac":
			plt.title(u'$Sn_{'+str(1-float(f_conc))+r'}'+f_dop+r'_{'+f_conc+r'}Te$') # numerki z pliku i nazwa domieszki też
		else:
			plt.title(u'$SnTe$'+ r' + '+str(100*float(f_conc))+r"% $Vac_{Sn}$") # numerki z pliku i nazwa domieszki też
		#print(f_conc)

		fig.set_size_inches(12.8,7.2)

		if zoom==True:
			file='zoom/'+'zoom_'+filename
		else:
			file='full/'+filename
		plt.savefig(file[:-4]+".png",
		     pad_inches = 0)
		
		#plt.show()