import random
import Tree
import copy
import time


def myFunc(e):
  return e[1]


# First We make a list of inputs and outputs here
# indexes in input and output are the same for example 1 gives 2 , 5 gives 11
# we can add more datas to both of them:
# we should do this for example:
# add 10 to input and  15 to output : 10 gives 15
start_time = time.time()
input_list = [2,5,8,3,4,11,13]
output_list = [17,34,56,98,105,130,153]
print("Input: ",input_list)
print("Output: ",output_list)

# here we generate some functions using function_generator() and make then
# make a tree from every one of them
#in making tree, first we convert expressions to postfix and them make tree
tree_count = int(input("Please Enter the number of the first genes: "))
generation_count = int(input("How many generations use wnat to go through: "))
trees = []
best_tree = []
for i in range(tree_count):
    aa = Tree.function_generator()
    postfix = Tree.infix_to_postfix(aa)
    r = Tree.Make_tree(postfix)
    trees.append(r)


# here we do our fitness function to get the value of our trees and save them in the new array of all_trees
# first index is the tree and second is the fitness
all_trees = []
#Fitness
for i in range(tree_count):
    all_trees.append([trees[i],Tree.Fitness(trees[i], input_list, output_list)])
#this line sort our trees based on fitness value
all_trees.sort(key=myFunc,reverse=True)

#this code is for printing our tree and its fitness function for generation 0
# print(f'\n\n\nGeneration Number 0')
# for i in range(tree_count):
#     Tree.Inorder(all_trees[i][0])
#     print("\t\t", "Fitness: ", all_trees[i][1])


# we want to get the best tree that has ever been produced in our algorithm
# so, we store it inside a variable
best_tree = copy.deepcopy(all_trees[0])


#here, with change the second number, we can set our many generations we want to go through
for j in range(1,generation_count):
    # CrossOver Call
    i = 0
    if (tree_count%2==0):
        while i < tree_count:
            Tree.CrossOver(all_trees[i][0], all_trees[i + 1][0])
            i = i + 2
    else:
        while i < tree_count-1:
            Tree.CrossOver(all_trees[i][0], all_trees[i + 1][0])
            i = i + 2


    # #Mutation
    i = 0
    for i in range(tree_count):
        Tree.Mutation(all_trees[i][0])
    # After mutation, we should calculate our fitnesses again and then find the best tree
    #Getting Fitness
    for i in range(tree_count):
        all_trees[i][1] = Tree.Fitness(all_trees[i][0], input_list, output_list)
    all_trees.sort(key=myFunc, reverse=True)

    # This part is for seeing the trees in every generation

    #print(f'\n\n\nGeneration Number {j}')
    #for i in range(tree_count):
    #    Tree.Inorder(all_trees[i][0])
    #    print("\t\t", "Fitness: ", all_trees[i][1])


    if (all_trees[0][1] > best_tree[1]):
        best_tree = copy.deepcopy(all_trees[0])


# this the best tree we have generated
end_time = time.time()
print("Tree is: ", end="")
Tree.Inorder(best_tree[0])
print("")
print("Fitness is: ", best_tree[1])
print("Execution Time: ", round(end_time - start_time, 2), "s")

