
# coding: utf-8

# In[9]:


import os
cwd = os.getcwd()
print (cwd)


# In[43]:


from PIL import Image
im = Image.open("tmp.jpg")
im=im.convert('L') #greyscale 
im.rotate(45).show()


# In[46]:


#qui sono diverse ! 

from PIL import Image
from PIL import ImageChops

im1 = Image.open("A (1).jpg").convert('L')
im2 = Image.open("A (2).jpg").convert('L')

diff = ImageChops.difference(im2, im1)
diff.show()



# In[154]:


import numpy as np
from PIL import Image, ImageChops


def diff_images():
    im1 = Image.open("E (8).jpg").convert('L')
    im2 = Image.open("E (9).jpg").convert('L')

    diff = ImageChops.difference(im2,im1)
    diffdata = np.asarray( diff, dtype="int32" ) 
    print(diffdata.sum())
    if diffdata.sum()>50000: 
        print('diverse')
    else:
        print('uguali')
   
if __name__ == '__main__' :
    diff_images()


# In[174]:


import numpy as np
from PIL import Image, ImageChops

im1 = Image.open("U (1).jpg").convert('L')
im2 = Image.open("U.jpg").convert('L')

diff = ImageChops.difference(im2,im1)
diffdata = np.asarray( diff, dtype="int32" ) 
print(diffdata.sum())
if diffdata.sum()>50000: 
    print('diverse')
else:
    print('uguali')
   



# In[ ]:


"""
diff.show()
   
diff12 = ImageChops.subtract(im1,im2)
diff21 = ImageChops.subtract(im2,im1)
diff12.save("diff12.jpg")
diff21.save("diff21.jpg")
diff.save("diff.jpg")

im2data = np.asarray( im2, dtype="int32" )
im1data = np.asarray( im1, dtype="int32" )
print(im1data.sum()) 
print(im2data.sum()) 
diff12data = np.asarray( diff12, dtype="int32" )
diff21data = np.asarray( diff21, dtype="int32" )
print(diff12data.sum())
print(diff21data.sum())

 diffdata è la somma esatta degli altri due
 una immagina normale ha una somma di circa 50034162 
 la diff fra due immagini uguali è zero 
 qualche differenze è 797040
"""



# In[164]:


import numpy as np
from PIL import Image, ImageChops
image = Image.new('RGB', (640, 480), (255, 255, 255))
image.save("image.png", "PNG")



# In[170]:


import numpy as np
from PIL import Image, ImageChops
image = Image.new('RGB', (640, 480), (255, 255, 255))
previousphotoname = "comparison.png"
image.save(previousphotoname, "PNG")
previousphoto = Image.open("comparison.png").convert('L')

