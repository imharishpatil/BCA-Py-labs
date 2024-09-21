#histogram and piechart
import matplotlib.pyplot as plt
import numpy as np
heights=np.random.normal(170,2,100)
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
plt.hist(heights)
plt.xlabel("hieghts of person")
plt.ylabel("no of observed values")
plt.title("hisogram to show the heights of paersons")
plt.subplot(2,1,2)
fruits=['apple','banana','orange']
price=[200,100,300]
plt.pie(price,labels=fruits)
plt.title("pie chart showing fruits and their prices")
plt.grid(True)
plt.tight_layout()
plt.show()