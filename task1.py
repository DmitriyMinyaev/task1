import numpy as np
a = np.loadtxt('test1.dat', dtype=np.float)
p = np.percentile(a, 90)
n = 2
template = '{:.' + str(n) + 'f}'
print(template.format(p), end='\n')
b = np.percentile(a, 50)
template = '{:.' + str(n) + 'f}'
print(template.format(b), end='\n')
max = np.max(a)
print (template.format(max), end='\n')
min = np.min(a)
print (template.format(min), end='\n')
avg = np.average(a)
print (template.format(avg), end='\n')
