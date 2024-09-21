import numpy as np
salesdata=np.array([2000,1050,1200,1500,2500,3500,3200,1400,2750,3800,1800,2380,3000,1300])
print("14 days sales data is as follows")
for i in range(0,len(salesdata)):
    print(f"Day{i+1}={salesdata[i]}")
firstweek=salesdata[0:7]
totalsdweek1=np.sum(firstweek)
secondweek=salesdata[7:]
totalsdweek2=np.sum(secondweek)
print("first week sales data")
for i in range(0,7):
    print(f"Day{i+1}={salesdata[i]}")
print("second week sales data")
for i in range(7,len(salesdata)):
    print(f"Day{i+1}={salesdata[i]}")
print(f"total sales data of first week={totalsdweek1}")
print(f"total sales data of second week={totalsdweek2}")
avgsd=np.mean(salesdata)
print(f"average sales data is={avgsd}")
sdgt2000=salesdata[salesdata>2000]
print("sales data above 2000")
print(sdgt2000)
print(f"highest sales data={np.max(salesdata)}")
print(f"lowest sales data={np.min(salesdata)}")