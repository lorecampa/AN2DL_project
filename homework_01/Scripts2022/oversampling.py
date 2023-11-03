import os
from os import listdir
from os.path import isfile, join
import random
import shutil

dir = 'train'     #specify the directory of the set to oversample

directories = os.listdir(dir)
random.seed(21)

size_spec1 = 200
size_spec6 = 200

#oversample only the two minority classes drawing and duplicating samples with replacement as specified above
for item in directories:
   if item == "Species1" or item == "Species6":
        list_images = [image for image in os.listdir(dir + "/" + item)]
        if item == "Species1":
           for num in range(size_spec1):
                i = random.randint(0, len(list_images) - 1)
                print(i)
                shutil.copy2(dir+"/"+item+"/"+list_images[i],
                            dir+"/"+item+"/"+list_images[i][0:5]+"_"+str(num)+list_images[i][5:])
        else:
            for num in range(size_spec6):
                i = random.randint(0, len(list_images) - 1)
                print(i)
                shutil.copy2(dir + "/" + item + "/" + list_images[i],
                             dir + "/" + item + "/" + list_images[i][0:5] + "_" + str(num) + list_images[i][5:])

#oversampke all the classes indicating the number of samples to draw and duplicate from the minority and all the other classes
#size_spec16 = 170
#size_spec = 120

#for item in directories:
  #      list_images = [image for image in os.listdir(dir + "/" + item)]
   #     if item == "Species1" or item == "Species6":
    #        for num in range(size_spec16):
     #           i = random.randint(0, len(list_images) - 1)
      #          print(i)
       #         shutil.copy2(dir+"/"+item+"/"+list_images[i],
        #                     dir+"/"+item+"/"+list_images[i][0:5]+"_"+str(num)+list_images[i][5:])
        #else:
         #   for num in range(size_spec):
          #      i = random.randint(0, len(list_images) - 1)
           #     print(i)
            #    shutil.copy2(dir + "/" + item + "/" + list_images[i],
             #                dir + "/" + item + "/" + list_images[i][0:5] + "_" + str(num) + list_images[i][5:])