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
folder='in/'
directory='data/'+folder
directory_z='data_zoom/'+folder
print(os.listdir(directory_z))
for filename in sorted(os.listdir(directory_z)):
	if filename.endswith(".dat"):
		print(filename)
		#plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
		###########################################################################
		zoom=True 
		linewidth=1.2

		if zoom==False:
			file=directory+filename
		else:
			file=directory_z+filename

		f_conc= str(re.search('snte_(.*)-(.*).dat', file).group(2))
		f_dop=str(re.search('snte_(.*)-(.*).dat', file).group(1))
		offset_l=20
		offset_r=1
		###########################################################################


		data=np.loadtxt(file,usecols=np.arange(0,23))
		ry_to_ev=13.6
		x=ry_to_ev*data[offset_l:-offset_r,0]		#3-7 1pierw(z30) 8-12 z50 13-17 z52 18-22 z0// total s p d f 
		total=data[offset_l:-offset_r,1]
		p1=data[offset_l:-offset_r,3] # dopant
		p2=data[offset_l:-offset_r,8] # sn
		p3=data[offset_l:-offset_r,13] # te
		p4=data[offset_l:-offset_r,18] # vacancy

		total_sum=float(f_conc)*p1+(1-float(f_conc))*p2+p3+p4*2
		total_sum=1.2*total_sum




		# ax.plot(x,total,'black',linewidth=linewidth,label='Total', linestyle='--',alpha=0.2)

		if f_dop!='Vac':
			ax.plot(x,p1,linewidth=linewidth, linestyle='--',label=(f_dop+" "+str(100*float(f_conc))+r"\%"))
		# ax.plot(x,p2,linewidth=linewidth,label='Sn', linestyle='--')
		# ax.plot(x,p3,linewidth=linewidth,label='Te', linestyle='--')
		#ax.plot(x,p4,linewidth=linewidth,label='Vac')
		# if f_dop != "Vac":
		# 	if f_conc=="0.0":
		# 		ax.plot(x,total_sum,'black',linewidth=linewidth, linestyle='-',label='SnTe',alpha=0.5) # numerki z pliku i nazwa domieszki też	
		# 	else:
		# 		ax.plot(x,total_sum,linewidth=linewidth, linestyle='--',label=(u'$\mathrm{Sn_{'+str(1-float(f_conc))+r'}}'+'\mathrm{'+f_dop+r'_{'+f_conc+r'}}\mathrm{Te}$')) # numerki z pliku i nazwa domieszki też
		# else:
		# 	ax.plot(x,total_sum,linewidth=linewidth, linestyle='--',label=('SnTe +'+str(100*float(f_conc))+r"% $\mathrm{Vac_{Sn}}$"))# numerki z pliku i nazwa domieszki też		


		# ax.plot(x,total_sum,'magenta',linewidth=linewidth,label='Total - sum')

ax.yaxis.set_major_locator(MultipleLocator(3))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.set_ylim(ymin=0)

if zoom==False:
	#ax.set_xlim(min(x),max(x))
	ax.set_xlim(-3.2,3.2)
	ax.set_ylim(0,25)
	ax.xaxis.set_major_locator(MultipleLocator(2))
	ax.xaxis.set_major_formatter(FormatStrFormatter('%1.f'))
	ax.xaxis.set_minor_locator(MultipleLocator(0.5))
	
else:
	ax.set_xlim(-0.32,0.32)
	ax.set_ylim(0,20)
	ax.xaxis.set_major_locator(MultipleLocator(0.1))
	ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
	ax.xaxis.set_minor_locator(MultipleLocator(0.05))
	# ax.xaxis.set_minor_formatter(FormatStrFormatter('%1.1f'))
	#ax.set_xticklabels([])


ax.grid(b=True, which='major', color='k', linestyle='--',alpha=0.1)
ax.legend(frameon=False)
ax.tick_params(which='both',direction='in',top=True,right=True)
ax.tick_params(which='major', width=1.5,length=5)
ax.plot([0,0],[-1,25],'magenta',linestyle='--',alpha=0.4)
ax.text(0, 15.5, r'$E_F$', fontsize=10,rotation=0)

# if zoom!=True:
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
	fig_scale=1
	#fig.set_size_inches(w=6.69423*fig_scale*scale,h=fig_scale*6.69423*0.75*scale)# 4:3
	fig.set_size_inches(w=6.69423*large_scale+0.01384,h=6.69423*0.6*large_scale*0.8) #16:9

if zoom==True:
	file='zoom_'+"dos-summary"
else:
	file="dos-summary"
plt.savefig(file[:-4]+".pgf",
     pad_inches = 0,
     bbox_inches='tight',
     dpi=200)

		#plt.show()