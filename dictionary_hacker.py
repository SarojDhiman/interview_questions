d1 = {'saroj':1,"sara":2,'tara':5,'anku':7}
d1.update({'dardo':9})
print(d1)
print(max(d1.items()))
def batch(**kwargs):
    for key,values in kwargs.items():
        print(key+values)
print(batch(kwargs='saroj',kwargs1='sara',kwargs2='hfhbaf'))

import pandas as pd
import numpy as np
df = pd.Series(np.random.rand(3))
print(df)
df1 = pd.DataFrame(np.random.rand(4,4))
print(df1)
df1 = pd.DataFrame(np.random.rand(4,4),index=np.arange(0,4))
df1[1][1]='harry'
print(df1)
df1.columns=list('abcd')
print(df1)
arr=list(map(int,input().split()))
print(arr)