import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#source : https://www.omnicalculator.com/physics/absolute-humidity
def sat_vapor(T):
    Pc = 22.064e6 #Pa - critical pressure for water
    Tc = 647.096 #K - critical temperature for water
    a = [-7.85951783,1.84408259,-11.7866497,22.6807411,-15.9618719,1.80122502] #Empirical constants
    
    to = 1 - T/Tc
    Ps = Pc*np.exp(Tc/T*(a[0]*to+a[1]*np.power(to,1.5)+a[2]*np.power(to,3)+a[3]*np.power(to,3.5)+a[4]*np.power(to,4)+a[5]*np.power(to,7.5)))
    return Ps

def abs_hum(T,RH):
    Rw = 461.5 #J/(kg.K) - Specific gas constant for water vapor
    AH = RH*sat_vapor(T)/(Rw*T*100)
    return AH

temperatures = pd.read_csv('data/Mean Temperatures.csv')
humidities = pd.read_csv('data/Mean Humidity.csv')
taht=temperatures['Mean (AHT20)'].to_numpy()
haht=humidities['Mean (AHT20)'].to_numpy()
tsdc=temperatures['Mean (SDC40)'].to_numpy()
hsdc=humidities['Mean (SDC40)'].to_numpy()
tother=temperatures['Mean (Others)'].to_numpy()
hother=humidities['Mean (Other sensors)'].to_numpy()

ahaht=abs_hum(taht+273.15,haht)
ahsdc=abs_hum(tsdc+273.15,hsdc)
ahother=abs_hum(tother+273.15,hother)

plt.plot(1000*ahaht)
plt.plot(1000*ahsdc)
plt.plot(1000*ahother)
plt.legend(['AHT20','SDC40','Others'])
plt.xlabel('Point number')
plt.ylabel('Absolute Humidity (g/m³)')
plt.show()

plt.plot(1000*(ahaht-ahother))
plt.xlabel('Point number')
plt.ylabel('Absolute Humiditiy Difference (g/m³)')
plt.legend(['AHT20-Others'])
plt.show()

plt.plot(1000*(ahsdc-ahother))
plt.xlabel('Point number')
plt.ylabel('Absolute Humiditiy Difference (g/m³)')
plt.legend(['SDC40-Others'])
plt.show()

print('Mean difference AHT20-Others=', 1000*np.mean(ahaht-ahother),'g/m³')
print('Mean difference SDC40-Others=', 1000*np.mean(ahsdc-ahother),'g/m³')

bins=np.arange(-0.8,0.9,0.1)
plt.hist(1000*(ahaht-ahother),bins=bins,alpha=0.5)
plt.hist(1000*(ahsdc-ahother),bins=bins,alpha=0.5)
plt.xlabel('Absolute Humiditiy Difference (g/m³)')
plt.title('Histogram')
plt.legend(['AHT20-Others','SDC40-Others'])
plt.show()