import json

#open the files
with open(r'ESSENCEm158.json') as f:
    source=json.load(f) #source is a dict
    
#write data in terms of 2-column ASCII (like Fig. 1)
wrt=open(r'ESSENCEm158_from_json.txt','w')
    
#required data: only spectra, the other information are trivial in my research
spec=source['ESSENCEm158']['spectra'][0]['data']

#another way to arange these data 
for i in spec:
    wrt.write(i[0])
    wrt.write(' ')
    wrt.write(str(float(i[1])*1.e15))
    wrt.write('\n')
wrt.close()

print("The conversion has finished, please check the repository!")