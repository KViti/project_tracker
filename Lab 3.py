import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from scipy.stats import uniform

# входные данные
N =100

sigma = 1
a = 0.5
m = -1
De= 0.2
Dv= 0.1

ksi=np.empty([N])
eta=np.empty([N])
noise_eps=np.random.uniform(-math.sqrt(3*De),math.sqrt(3*De), N)
noise_v=np.random.uniform(-math.sqrt(3*Dv),math.sqrt(3*Dv), N)
#noise_eps=np.random.normal(0, math.sqrt(De), N)
#noise_v=np.random.normal(0, math.sqrt(Dv), N)


ksi[0]= np.random.normal(m, sigma)
for i in range(1, N):
    ksi[i]=a*ksi[i-1]+noise_eps[i]
    eta[i]=ksi[i]+noise_v[i]

print("белый шум ε")
print([round(i,3) for i in noise_eps])
print("белый шум v")
print([round(i,3) for i in noise_v])
print("ξ")
print([round(i,3) for i in ksi])
print("η")
print([round(i,3) for i in eta])

ksi_sq=np.empty([N])
k=np.empty([N])
ksi_sq[0]=m
k[0]=(sigma**2)/Dv
r=De/Dv
error=np.empty([N])
for i in range(1, N):
    k[i]=(a*a*k[i-1]+r)/(a*a*k[i-1]+r+1)
    error[i] = k[i]*Dv
    ksi_sq[i]=a*ksi_sq[i-1]+k[i]*(eta[i]-a*ksi_sq[i-1])

print("k")
print([round(i,3) for i in k])
print("ошибка фильтра Р")
print([round(i,3) for i in error])
print("оценка ξ")
print([round(i,3) for i in ksi_sq])
MSE=(sum([(ksi[i]-ksi_sq[i])**2 for i in range(N)]))/N
print("Среднеквадратическая ошибка фильтра ", MSE)

plt.figure(0)
x = np.arange (0, N, 1)
plt.plot(x, ksi, 'black', label='ξ')
plt.legend()
1
plt.plot(x, ksi_sq, 'black',linestyle=':', label='оценка ξ фильтр Калмана')
plt.plot(x, error, 'black',linestyle='dashdot', label='ошибка фильтра')
plt.legend()

plt.figure(1)
plt.plot(x, ksi, 'black', label='ξ')
plt.plot(x, eta, 'black',linestyle=':', label='η')
plt.legend()
plt.figure(2)
plt.plot(x, noise_eps, 'black', label='ошибка ε')
plt.plot(x, noise_v, 'black',linestyle='dotted', label='v ошибка наблюдения')
plt.legend()
plt.figure(3)
plt.plot(x, error, 'black', label='ошибка фильтра')
plt.plot(x, [MSE for i in range(N)], 'black',linestyle=':', label='среднеквадратическая ошибка фильтра')
plt.plot(x, [Dv for i in range(N)], 'black',linestyle='dotted', label='дисперсия ошибки наблюдения')
plt.legend()
plt.show()