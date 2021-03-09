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

folder='zn/'
directory='data/'+folder
directory_z='data_zoom/'+folder
for filename in os.listdir(directory):
	if filename.endswith(".dat"):
		print(filename)
		###########################################################################
		zoom=False 
		linewidth=1.2
		if zoom==False:
			file=directory+filename
		else:
			file=directory_z+filename
		f_conc= str(re.search('snte_(.*)-(.*).dat', file).group(2))
		f_dop=str(re.search('snte_(.*)-(.*).dat', file).group(1))
		ats=[f_dop,'Sn','Te']################################?????????
		offset_l=20
		offset_r=1		
		###########################################################################
		if f_dop=="Vac":
			continue

		data=np.loadtxt(file,usecols=np.arange(0,23))
		for num,i in enumerate([3,8,13]):
			ry_to_ev=13.6
			x=ry_to_ev*data[:,0]		#3-7 1pierw(z30) 8-12 z50 13-17 z30 18-22 z0// total s p d f 
			total=data[:,1]
			p_tot=data[:,i]
			s=data[:,i+1]
			p=data[:,i+2]
			d=data[:,i+3]
			f=data[:,i+4]

			fig,ax=plt.subplots()
			#ax.plot(x,total,'black',linewidth=1,label='Total')
			ax.plot(x,p_tot,'black',linewidth=linewidth,label=ats[num])
			ax.plot(x,s,linewidth=linewidth,label='s', linestyle='--')
			ax.plot(x,p,linewidth=linewidth,label='p', linestyle='--')
			ax.plot(x,d,linewidth=linewidth,label='d', linestyle='--')
			ax.plot(x,f,linewidth=linewidth,label='f', linestyle='--')

			ax.yaxis.set_major_locator(MultipleLocator(3))
			ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
			ax.yaxis.set_minor_locator(MultipleLocator(0.5))
			ax.set_ylim(ymin=0)


			if zoom==False:
				#ax.set_xlim(min(x),max(x))
				ax.set_xlim(-12.7,6.25)
				ax.set_ylim(0,25)
				ax.xaxis.set_major_locator(MultipleLocator(2))
				ax.xaxis.set_major_formatter(FormatStrFormatter('%1.f'))
				ax.xaxis.set_minor_locator(MultipleLocator(0.5))

			else:
				ax.set_xlim(-1.1,1.1)
				ax.set_ylim(0,15)
				ax.xaxis.set_major_locator(MultipleLocator(0.5))
				ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
				ax.xaxis.set_minor_locator(MultipleLocator(0.125))


			ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
			ax.legend(frameon=False)
			ax.tick_params(which='both',direction='in',top=True,right=True)
			ax.tick_params(which='major', width=1.5,length=5)
			ax.plot([0,0],[-1,25],'magenta',linestyle='--',alpha=0.4)
			ax.text(0, 14.5, r'$E_F$', fontsize=10,rotation=0)

			if num!=0:
				plt.xlabel(r'$\mathrm{E-E_F}$ [eV] ',fontsize='large')
			if num==1:
				plt.ylabel('DOS [1/eV]',fontsize='large')
			if num==0:
				ax.set_xticklabels([])
			# #if num==0:
			#	plt.text(0.15, 0.8, r'$\textbf{(b)}$', fontsize=12, transform=plt.gcf().transFigure)
			if num==1:
				plt.text(0.15, 0.8, r'$\textbf{(c)}$', fontsize=12, transform=plt.gcf().transFigure)
			if num==2:
				plt.text(0.15, 0.8, r'$\textbf{(d)}$', fontsize=12, transform=plt.gcf().transFigure)								


			# plt.xlabel(r'$\mathrm{E-E_F}$ [eV] ',fontsize='large')
			# 0-dopant 1 sn 2 te
			# if f_dop != "Vac":
			# 	plt.title(ats[num]+' in '+r'$Sn_{'+str(1-float(f_conc))+r'}'+f_dop+r'_{'+f_conc+r'}Te$') # numerki z pliku i nazwa domieszki też
			# else:
			# 	plt.title(ats[num]+' in '+u'$SnTe$'+ r' + '+str(100*float(f_conc))+r"% $Vac_{Sn}$") 
			#print(f_conc)
			scale=1.1
			fig_scale=0.5
			
			large_scale=1.15
			if zoom==False:
				fig.set_size_inches(w=6.69423*large_scale+0.01384,h=6.69423*0.6*large_scale*0.8) #16:9
			else:
				fig.set_size_inches(w=6.69423*fig_scale*scale,h=fig_scale*6.69423*0.75*scale)# 4:3
			
			if zoom==True:
				file='m_zoom/'+'zoom_'+ats[num]+'_in_'+filename
			else:
				file='m_full/'+ats[num]+'_in_'+filename

			plt.savefig(file[:-4]+".pgf",
			     pad_inches = 0,
			     bbox_inches='tight',
		    	 dpi=200)
			# plt.savefig("ayaya.png", bbox_inches = 'tight',
			#     pad_inches = 0)

			#plt.show()