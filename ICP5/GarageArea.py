import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv('train.csv')
x= train.GarageArea
y= train.SalePrice
plt.scatter(x,y)
plt.show()

outlier_data= train[(train.GarageArea<850)&(train.SalePrice<450000)]
plt.scatter(outlier_data.GarageArea,outlier_data.SalePrice,color='r')
plt.show()
