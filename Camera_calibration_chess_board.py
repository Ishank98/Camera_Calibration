
# coding: utf-8

# # Importing Helper Libraries

# In[111]:


import numpy as np
import glob
import cv2


# *Here, objp are world points and we are assuming that only camera is moving along z axis while our images are at z=0 and we considering are world coordinates to be (1,0),(1,1) etc because we didnt take that images and we cant really say about the size of boxes*

# In[112]:


objp = np.zeros((6*8,3),np.float32)
objp[:,:2] = np.mgrid[0:8, 0:6].T.reshape(-1,2)
#objp


# *objpoints will store objp of every image and imgpoints will store 2D point of corners*

# In[113]:


objpoints = []
imgpoints = []


# *Loading all the image data*

# In[114]:


images = glob.glob('*.jpg')


# In[115]:


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# In[116]:


i=0
for pic in images:
    img = cv2.imread(pic)
    #As Opencv always load an image in 3c mode
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #we are looking are 8*6 pattern that is measured from (left to right and top to bottom)
    ret, corners = cv2.findChessboardCorners(gray,(8,6),None)
    #if pattern is found
    if ret == True:
        #world points are same for every image
        objpoints.append(objp)
        #to improve accuracy we use cornerSubPix
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        
        cv2.drawChessboardCorners(img,(8,6),corners2,ret)
        #cv2.imshow('img',img)
        #cv2.imwrite('mis-aligned points/'+str(i)+'.png',img)
        i=i+1
        cv2.waitKey(500)
        
cv2.destroyAllWindows()        


# *using calibrateCamera to get camera matrix, distortion coefficients, rotationa and translation vectors 
# *

# In[118]:


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)


# *camera matrix*

# In[55]:


mtx


# *distortion coefficients
# *

# In[56]:


dist


# rotational vector
# 

# In[120]:


rvecs


# *translation vectors*

# In[119]:


tvecs


# In[142]:


images_1 = glob.glob("*.jpg")


# Now, using the undistort function and camera matrix and distortion coefficients. we are undistorting those pics in which 8*6 pattern is present

# In[143]:


i=0
for pic in images_1:
    img = cv2.imread(pic)
    #As Opencv always load an image in 3c mode
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #we are looking are 8*6 pattern that is measured from (left to right and top to bottom)
    ret, corners = cv2.findChessboardCorners(gray,(8,6),None)
    if ret==True:
    #using camera matrix and distortion coefficients and undistort function
      dst = cv2.undistort(img,mtx,dist,None,None)
      i=i+1
      cv2.imwrite('undis-images/'+str(i)+'.png',dst)
      

