# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 13:04:59 2022

@author: gary6
"""


import matplotlib.pyplot as plt
import numpy as np 
#import pylab as plt
import Data_from_Catalog


data=[]
wrt=open(r'ESSENCEm158(test).txt','w')
data=Data_from_Catalog.fx() #將原先的資料完全貼到此檔案中 (用raw text 不然會當掉)

wl=[]
flux=[]
for i in data:
    for j in i:
        if float(j)>1000:
            wl.append(float(j))
            wrt.write(j) 
            wrt.write(' ') #space 
        else:   
            flux.append(float(j)) 
            F=str(float(j)*1.e15) #calibration to 1.e-15
            wrt.write(F)
            wrt.write('\n')
wrt.close()

plt.plot(wl,flux)
plt.xlim(5500,7000)
plt.title("ESSENCEm158 (Type Ia)2") 
plt.xlabel(r"rest wavelengths($\AA$)")
plt.ylabel(r"relative flux")
#plt.savefig('ESSENCEm158 (Type Ia)2.pdf')
plt.show()