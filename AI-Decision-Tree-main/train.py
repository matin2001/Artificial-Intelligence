from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from DecisionTree import DecisionTree
import csv


def accuracy(test, pred):
    return np.sum(test == pred) / len(test)

# Restaurnat Data
# data_restaurant1 = [[1,0,0,1,1,3,0,1,1,1],[1,0,0,1,2,1,0,0,2,3],[0,1,0,0,1,1,0,0,3,1],[1,0,1,1,2,1,1,0,2,2],
#                    [1,0,1,0,2,3,0,1,1,4],[0,1,0,1,1,2,1,1,4,1],[0,1,0,0,0,1,1,0,3,1],[0,0,0,1,1,2,1,1,2,1],
#                    [0,1,1,0,2,1,1,0,3,4],[1,1,1,1,2,3,0,1,4,2],[0,0,0,0,0,1,0,0,2,1],[1,1,1,1,2,1,0,0,3,3]]
# target_restaurant1 = [1,0,1,1,0,1,0,1,0,0,0,1]
# data_restaurant = np.array( data_restaurant1 )
# target_restaurant = np.array( target_restaurant1 )
# x, y = data_restaurant, target_restaurant
# print("we show the index of the feature we choose and the threshold of it.")
# print("For example 1 stands for Alt and 2 stands for Bar")



# Diabates Data
diabates_data = []
diabetes_target = []
with open("diabetes.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        diabates_data.append(row)
for i in diabates_data:
    target = i.pop()
    diabetes_target.append(target)
diabetes_target = [eval(i) for i in diabetes_target]
for j in range(len(diabates_data)):
    diabates_data[j] = [eval(i) for i in diabates_data[j]]
diabates_data1 = np.array( diabates_data )
diabetes_target1 = np.array( diabetes_target )
x, y = diabates_data1, diabetes_target1
print("we show the index of the feature we choose and the threshold of it.")
print("For example 0 stands for pregnancies and 1 stands for Glucose")







Training_Input, Testing_Input, Training_Output, Testing_Output = train_test_split(x, y, test_size=0.2, random_state=1234)
Tree = DecisionTree()
Tree.fit(Training_Input, Training_Output)
tree_prediction = Tree.predict(Testing_Input)
acc = accuracy(Testing_Output, tree_prediction)
print("\n\nTree Id is: ", Tree)
print("Accuracy is: ", acc)
