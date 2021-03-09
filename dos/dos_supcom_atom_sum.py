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


fig,ax=plt.subplots()

folder='supcom/'
directory='data/'+folder
# directory_z='data_zoom/'+folder
for filename in os.listdir(directory):
	if filename.endswith(".dat"):
		print(filename)
		#plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
		###########################################################################
		zoom=True 
		linewidth=1.2

		if zoom==False:
			file=directory+filename
		else:
			file=directory+filename

		f_conc= str(re.search('snte_(.*)-(.*).dat', file).group(2))
		f_dop=str(re.search('snte_(.*)-(.*).dat', file).group(1))
		offset_l=20
		offset_r=1
		###########################################################################


		data=np.loadtxt(file,usecols=np.arange(0,14))
		ry_to_ev=1
		x=ry_to_ev*data[offset_l:-offset_r,0]		#3-7 1pierw(z30) 8-12 z50 13-17 z52 18-22 z0// total s p d f 
		total=data[offset_l:-offset_r,1]
		p1=data[offset_l:-offset_r,2] # dopant
		p2=data[offset_l:-offset_r,6] # sn
		p3=data[offset_l:-offset_r,10] # te
		p4=data[offset_l:-offset_r,10] # vacancy

		total_sum=float(f_conc)*p1+(1-float(f_conc))*p2+p3+p4*2
		total_sum=1.2*total_sum



		# ax.plot(x,total,'black',linewidth=linewidth,label='Total', linestyle='--',alpha=0.2)

		# ax.plot(x,p4,linewidth=linewidth,label='Vac')
		if f_dop != "Vac":
			if f_conc=="0.0":
				ax.plot(x,total,color='black',linewidth=linewidth,label='SnTe') # numerki z pliku i nazwa domieszki też	
			else:
				ax.plot(x,total,color='black',linewidth=linewidth,label=(u'$\mathrm{Sn_{'+str(1-float(f_conc))+r'}}'+'\mathrm{'+f_dop+r'_{'+f_conc+r'}}\mathrm{Te}$')) # numerki z pliku i nazwa domieszki też
		else:
			ax.plot(x,total,color='black',linewidth=linewidth,label=(u'$\mathrm{SnTe}$'+ r' + '+str(100*float(f_conc))+r"% $\mathrm{Vac_{Sn}}$"))# numerki z pliku i nazwa domieszki też
		

		if f_dop!='Vac':
			ax.plot(x,p1,linewidth=linewidth,label=f_dop, linestyle='--')
		ax.plot(x,p2,linewidth=linewidth,label='Sn', linestyle='--')
		ax.plot(x,p3,linewidth=linewidth,label='Te', linestyle='--')

# ax.plot(x,total_sum,'magenta',linewidth=linewidth,label='Total - sum')

ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.set_ylim(ymin=0)

if zoom==False:
	#ax.set_xlim(min(x),max(x))
	ax.set_xlim(-12.1,6.25)
	ax.set_ylim(0,125)
	ax.xaxis.set_major_locator(MultipleLocator(2))
	ax.xaxis.set_major_formatter(FormatStrFormatter('%1.f'))
	ax.xaxis.set_minor_locator(MultipleLocator(0.5))
	ax.text(0, 60, r'$E_F$', fontsize=10,rotation=0)
	
else:
	ax.set_xlim(-1.1,1.1)
	ax.set_ylim(0,70)
	ax.xaxis.set_major_locator(MultipleLocator(0.5))
	ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
	ax.xaxis.set_minor_locator(MultipleLocator(0.125))
	# ax.xaxis.set_minor_formatter(FormatStrFormatter('%1.1f'))
	ax.set_xticklabels([])
	ax.text(0, 30, r'$E_F$', fontsize=10,rotation=0)


ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
ax.legend(frameon=False)
ax.tick_params(which='both',direction='in',top=True,right=True)
ax.tick_params(which='major', width=1.5,length=5)
ax.plot([0,0],[-1,140],'magenta',linestyle='--',alpha=0.4)
# ax.text(0, 120, r'$E_F$', fontsize=10,rotation=0)
if zoom==True:
	plt.text(0.15, 0.8, r'$\textbf{(a)}$', fontsize=12, transform=plt.gcf().transFigure)

if zoom!=True:
	plt.xlabel(r'$\mathrm{E-E_F}$ [eV] ',fontsize='large')
plt.ylabel('DOS [1/eV]',fontsize='large')

# if f_dop != "Vac":
# 	plt.title(u'$\mathrm{Sn_{'+str(1-float(f_conc))+r'}}'+'\mathrm{'+f_dop+r'_{'+f_conc+r'}}\mathrm{Te}$') # numerki z pliku i nazwa domieszki też
# else:
# 	plt.title(u'$\mathrm{SnTe}$'+ r' + '+str(100*float(f_conc))+r"% $\mathrm{Vac_{Sn}}$") # numerki z pliku i nazwa domieszki też
# #print(f_conc)

# fig.set_size_inches(w=6.69423*0.5,h=6.69423*0.5*0.8)

scale=1.1
large_scale=1.15
if zoom==False:
	fig.set_size_inches(w=6.69423*large_scale+0.01384,h=6.69423*0.6*large_scale*0.8) #16:9
else:
	fig_scale=0.5
	fig.set_size_inches(w=6.69423*fig_scale*scale,h=fig_scale*6.69423*0.75*scale)# 4:3

if zoom==True:
	file='zoom/'+'supcom_zoom_'+filename
else:
	file='full/'+'supcom_'+filename
plt.savefig(file[:-4]+".pgf",
     pad_inches = 0,
     bbox_inches='tight',
     dpi=200)

#plt.show()