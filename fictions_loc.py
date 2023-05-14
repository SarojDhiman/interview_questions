# import numpy as np
# from PIL import Image
# image = Image.new('RGB',(500,500),color=(0,0,0))
# image.show()  

# s = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(s)
# import pandas as pd
# df = pd.DataFrame([[1,2,3],[4,5,6],[9,8,7]],columns=['s','a','r'])
# print(df)
# print(df.iloc[[0,2],0])#first row selected so better for selecting rows
# print(df.loc[0:3])# better for selecting columns

# #in i loc we can pass the range and we can even pass the row number

from collections import Counter
string1 = "anvsdrhogidndfhfdhlfgukf"
s = Counter(string1)
# print(s)
# print(max(s,key=s.get))

import cv2
import numpy as np
img = np.ones((500,500,3))
cv2.imshow("empty image",img)
cv2.waitKey(0)



