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

directory='data/'
# print(os.listdir(directory))
# print(sorted(os.listdir(directory)))
delta_e=[]
concent=[]

for filename in sorted(os.listdir(directory)):
	if filename.endswith(".dat"):
		print(filename)

		
		###########################################################################
		zoom=True 
		linewidth=0.8
		file=directory+filename
		f_conc= str(re.search('zn(.*).dat', file).group(1))
		#f_dop=str(re.search('zn_(.*)-(.*).dat', file).group(1))		
		offset_l=0
		offset_r=0

		cut=0.09
		###########################################################################
		data1=np.loadtxt(file,usecols=np.arange(0,3))	
		#print(f_conc)	

		x1=data1[:,0]
		band1=data1[:,1]
		err1=data1[:,2]

		x1_cut=[]
		band1_cut=[]
		err1_cut=[]	



		for i,val in enumerate(x1):
			if band1[i]>-1 and band1[i]<cut:
				x1_cut.append(x1[i])
				band1_cut.append(band1[i])
				err1_cut.append(err1[i])

		band1_cut=band1_cut-band1_cut[0]				



		band1_cut_2=[]
		x1_cut_2=[]
		err1_cut_2=[]	

		for i,val in enumerate(x1_cut):
			if band1_cut[i]<0:
				x1_cut_2.append(x1_cut[i])
				band1_cut_2.append(band1_cut[i])
				err1_cut_2.append(err1_cut[i])	

		band1_top=band1_cut+err1_cut
		band1_bottom=band1_cut-err1_cut	

		concent.append(float(f_conc)*100)
		delta_e.append(band1_cut[0]-band1_cut[-1])


ax.plot(concent,delta_e,marker='o')
# ax.set_ylim(ymin=-7,ymax=3)
#ax.set_ylim(ymin=-0.4,ymax=-0.2)

# ax.plot(x3,x3*0+0.12,color='red')
# ax.plot(x3,x3*0-1,color='red')

#ax.set_xlim(xmin=0,xmax=0.283)
#ax.set_xticklabels([])
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False) 


ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
ax.legend(frameon=False)

# plt.text(0.12, 0.08, 'L', fontsize=14, transform=plt.gcf().transFigure)
# plt.text(0.89, 0.08, r'$\Sigma$', fontsize=14, transform=plt.gcf().transFigure)


plt.xlabel(u'Zawartość Zn [%]',fontsize='large')
plt.ylabel('Re(E) [eV]',fontsize='large')
# plt.title(u'Delta E')
# fig.set_size_inches(7.2,12.8)
fig.set_size_inches(4,3)
plt.savefig('porow_band_delta_e_loop.pgf',
			 pad_inches = 0,
		     bbox_inches='tight',
		     dpi=200)			