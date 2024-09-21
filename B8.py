#line chart and bar chart
import matplotlib.pyplot as plt
import numpy as np
months=['jun','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
temp=np.array([25,14,12,15,23,17,18,26,31,29,11,32])
quarter=['quarter1','quarter2','quarter3','quarter4']
tempquarter=[26,30,18,24]
plt.figure(figsize=(12,8))
plt.subplot(2,1,1)
plt.plot(months,temp,linestyle='-',color='b',marker='o')
plt.xlabel("months")
plt.ylabel("tempreture")
plt.title("line chart showing temprwture month wise")
plt.legend(months)
plt.subplot(2,1,2)
plt.bar(quarter,tempquarter,color='red')
plt.title("piechart showing tempreture quarter wise")
plt.legend(quarter)
plt.grid(True)
plt.tight_layout()
plt.show()