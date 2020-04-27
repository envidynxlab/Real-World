# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import arcpy 
import pandas as pd
from statistics import mean


urban = pd.read_csv(r'H:\mydocuments\Graphs\urban_analysis.csv')
urban1 = pd.read_csv(r'H:\mydocuments\Graphs\urban.csv')
urban2 = pd.read_csv(r'H:\mydocuments\Graphs\natural.csv')
#trendline function 
def best_fit_slope_and_intercept(x,y):
    m = (((mean(x)*mean(y)) - mean(x*y)) / ((mean(x)*mean(x)) -mean(x*x)))
    
    b = mean(y) - m*mean(x)
    
    return m, b

#scaling laws (urban vs natural)
#length vs area
#plt.scatter(urban['a_ln_u'], urban['l_ln_u'], c='b', marker='x')
#plt.scatter(urban['a_ln_n'], urban['l_ln_n'], c='0.5', marker='o')
#plt.legend(labels=('Urban', 'Natural'), loc='upper left')
#plt.xlabel('ln[area (m^2)]')
#plt.ylabel('ln[length (m)]')
#plt.savefig(r'H:\mydocuments\Graphs\l_vs_a.eps', format='eps')

#area vs perimeter
plt.scatter(urban1['a_ln_u'], urban1['p_ln_u'], c='0', marker='x')

plt.xlabel('ln[area (m^2)]')
plt.ylabel('ln[perimeter (m)]')

x = urban1['a_ln_u']
y = urban1['p_ln_u']
m, b = best_fit_slope_and_intercept(x,y)
regression_line = (m*urban1['a_ln_u']) + b
plt.plot(urban1['a_ln_u'], regression_line)
plt.scatter(urban2['a_ln_n'], urban2['p_ln_n'], c='0.6', marker='o')
x1 = urban2['a_ln_n']
y1 = urban2['p_ln_n']
print(x1,y1)
m2, b2 = best_fit_slope_and_intercept(x1,y1)
print (m2,b2)
regression_line2 = (m2*urban2['a_ln_n']) + b2
plt.plot(urban2['a_ln_n'], regression_line2)
plt.legend(labels=('Urban', 'Natural'), loc='upper left')
plt.savefig(r'H:\mydocuments\Graphs\p_vs_a.eps', format='eps')



#area vs distortion index
#plt.scatter(urban1['a_ln_u'], urban1['DI_u'], c='0', marker='x')
#plt.scatter(urban1['a_ln_n'], urban1['DI_n'], c='0.6', marker='o')
#plt.xlabel('ln[area (m^2)]')
#plt.ylabel('Distortion Index')
#plt.legend(labels=('Urban', 'Natural'), loc='upper left')
#plt.savefig(r'H:\mydocuments\Graphs\di_vs_a.eps', format='eps')




#building density and street length graphs
#mini, maxi = 0, 0.22
#norm = plt.Normalize(mini, maxi)
#plt.scatter(urban['S_ln(a)'], urban['S_DI'], c=urban['S_b_density'], marker='o', norm=norm)
#plt.colorbar(label= 'Building Density')
#plt.scatter(urban['I_ln(a)'], urban['I_DI'], c=urban['I_b_density'], marker='s', norm=norm)
#plt.scatter(urban['N_ln(a)'], urban['N_DI'], c=urban['N_b_density'], marker='*', norm=norm)
#plt.scatter(urban['a_ln_n'], urban['DI'], c='0.5', marker='v')
#plt.xlabel('ln[area (m^2)]')
#plt.ylabel('Distortion Index')
#plt.legend(labels=('Sandy','Irene','Nate'), loc='upper left')
#plt.savefig(r'H:\mydocuments\Graphs\bd_avsdi.eps', format='eps')

#mini, maxi = 0, 7
#norm = plt.Normalize(mini, maxi)
#plt.scatter(urban['S_ln(a)'], urban['S_DI'], c=urban['S_ln(RL)'], marker='o', norm=norm)
#plt.colorbar(label= 'ln[street length (m)]')
#plt.scatter(urban['I_ln(a)'], urban['I_DI'], c=urban['I_ln(RL)'], marker='s', norm=norm)
#plt.scatter(urban['N_ln(a)'], urban['N_DI'], c=urban['N_ln(RL)'], marker='*', norm=norm)
#plt.scatter(urban['a_ln_n'], urban['DI'], c='0.5', marker='v')
#plt.xlabel('ln[area (m^2)]')
#plt.ylabel('Distortion Index')
#plt.legend(labels=('Sandy','Irene','Nate'), loc='upper left')
#plt.savefig(r'H:\mydocuments\Graphs\RL_avsdi.eps', format='eps')







print ("done")