# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:05:25 2018

@author: Xia Chen
"""
import pandas
import matplotlib.pyplot as plt
city_data=pandas.read_csv("city_data.csv")
city_data['MA']=city_data["avg_temp"].rolling(window=10).mean()
plt.plot(city_data["year"],city_data["MA"], label="Toronto",color="RED")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature °C")
plt.title("Temperature in Toronto")
plt.show()

import pandas
import matplotlib.pyplot as plt
global_data=pandas.read_csv("global_data.csv")
global_data['MA']=global_data["avg_temp"].rolling(window=10).mean()
plt.plot(global_data["year"],global_data["MA"], label="Global",color="BLACK")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature °C")
plt.title(" Global Temperature")
plt.show()


import pandas
import matplotlib.pyplot as plt
plt.plot(city_data["year"],city_data["MA"], label="Toronto",color="RED")
plt.plot(global_data["year"],global_data["MA"], label="Global",color="BLACK")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature °C")
plt.title(" Temperature in Toronto vs.Global Temperature")
plt.show()
