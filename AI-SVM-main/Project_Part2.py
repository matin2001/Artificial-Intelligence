from matplotlib.image import imread
from sklearn.metrics import classification_report
from PIL import Image as im
import numpy as np
from sklearn import svm
import os
  

path = "train"  
contents = os.listdir(path) 
array_of_numbers = []
value_of_numbers = []
for i in range(len(contents)):
    mem = imread(os.path.join('train',f"{contents[i]}"))
    flat = mem.flatten()
    array_of_numbers.append(flat)
    if '0_' in contents[i] :
      value_of_numbers.append(0)
    elif '1_' in contents[i] :
      value_of_numbers.append(1)
    elif '2_' in contents[i] :
      value_of_numbers.append(2)
    elif '3_' in contents[i] :
      value_of_numbers.append(3)
    elif '4_' in contents[i] :
      value_of_numbers.append(4)
    elif '5_' in contents[i] :
      value_of_numbers.append(5)
    elif '6_' in contents[i] :
      value_of_numbers.append(6)
    elif '7_' in contents[i] :
      value_of_numbers.append(7)
    elif '8_' in contents[i] :
      value_of_numbers.append(8)
    elif '9_' in contents[i] :
      value_of_numbers.append(9)
numpy_array = np.array(array_of_numbers)
     

    
path1 = "test"  
contents1 = os.listdir(path1) 
array_of_numbers1 = []
value_of_numbers1 = []
for i in range(len(contents1)):
    mem = imread(os.path.join('test',f"{contents1[i]}"))
    flat = mem.flatten()
    array_of_numbers1.append(flat)
    if '0_' in contents[i] :
      value_of_numbers1.append(0)
    elif '1_' in contents1[i] :
      value_of_numbers1.append(1)
    elif '2_' in contents1[i] :
      value_of_numbers1.append(2)
    elif '3_' in contents1[i] :
      value_of_numbers1.append(3)
    elif '4_' in contents1[i] :
      value_of_numbers1.append(4)
    elif '5_' in contents1[i] :
      value_of_numbers1.append(5)
    elif '6_' in contents1[i] :
      value_of_numbers1.append(6)
    elif '7_' in contents1[i] :
      value_of_numbers1.append(7)
    elif '8_' in contents1[i] :
      value_of_numbers1.append(8)
    elif '9_' in contents1[i] :
      value_of_numbers1.append(9)
numpy_array1 = np.array(array_of_numbers1)
     
     
my_svm = svm.SVC(kernel='rbf',gamma = 'auto' ,C=10)
my_svm.fit(numpy_array, value_of_numbers)
my_predict = my_svm.predict(numpy_array1)
print(classification_report(value_of_numbers1,my_predict))






