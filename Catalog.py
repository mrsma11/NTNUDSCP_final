# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np 
import Data_from_Catalog


data=[]
wrt=open(r'ESSENCEm158(test).txt','w')
data=Data_from_Catalog.f()  #There are two datas: f and fx 

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
plt.show()
