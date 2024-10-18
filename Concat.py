import pandas as pd
df=pd.read_csv('naukri.com.csv')
df1=pd.read_csv('naukri1.com.csv')
df3=pd.concat([df,df1])
df3.to_csv('naukri.com.csv',index=False)
