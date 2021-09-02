#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image=cv2.imread(r"pic3.jpeg")
grayimage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayimageinv = 253 - grayimage
grayimageinv = cv2.GaussianBlur(grayimageinv, (21,21),0)
output = cv2.divide(grayimage, 255 - grayimageinv, scale=256.0)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)


# In[3]:


cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)


# In[4]:


cv2.imshow("image",image)
cv2.imshow("pencilsketch",output)


# In[ ]:


cv2.waitKey(0)


# In[ ]:




