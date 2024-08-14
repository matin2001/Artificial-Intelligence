import random
from collections import deque
import math


def function_generator():
    """
        in this function, first we make a mathematical expression using +-*/
        after that, we add '(' and ')' to the expression in order to make a tree of them
    :return: our expression in string form -> 6+x-((5*2)/6)
    """
    operators = ["+", "-", "*", "/"]
    operands = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "x"]
    operand = random.choice(operands)
    expression = []
    expression.append(operand)
    check_x = False
    for i in range(7):
        if(expression.__contains__("x")):
            check_x = True
        operator = random.choice(operators)
        operand = random.choice(operands)
        expression.append(operator)
        expression.append(operand)
    if(check_x == False):
        while(True):
            replace_x = random.randint(0, len(expression)-1)
            if isOperator(expression[replace_x]) == False:
                expression[replace_x] = "x"
                break
    i = 0
    #adding parantheses
    while i < len(expression):
        if expression[i] == "*" or expression[i] == "/":
            temp = expression[i-1]
            expression[i-1] = "(" + temp
            j = i+2
            while(j < len(expression)):
                if(expression[j] == "*" or expression[j]=="/"):
                    j = j+2
                else:
                    new_temp = expression[j-1]
                    expression[j-1] = new_temp + ")"
                    break
        i = i + 1
    final_exp = "".join(expression)
    while final_exp.count("(") != final_exp.count(")"):
        final_exp = final_exp + ")"
    return final_exp


def infix_to_postfix(infix_input: list) -> list:
    """
        for writting this function I helped from Internet
        this function, converts our infix expression to postfix
    :param infix_input:
    :return:
    """
    # precedence order and associativity helps to determine which
    precedence_order = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    associativity = {'+': "LR", '-': "LR", '*': "LR", '/': "LR", '^': "RL"}
    # clean the infix expression
    clean_infix = infix_input

    i = 0
    postfix = []
    operators = "+-/*^"
    stack = deque()
    while i < len(clean_infix):

        char = clean_infix[i]
        # check if char is operator
        if char in operators:
            # check if the stack is empty or the top element is '('
            if len(stack) == 0 or stack[0] == '(':
                # just push the operator into stack
                stack.appendleft(char)
                i += 1
            # otherwise compare the curr char with top of the element
            else:
                # peek the top element
                top_element = stack[0]
                # check for precedence
                # if they have equal precedence
                if precedence_order[char] == precedence_order[top_element]:
                    # check for associativity
                    if associativity[char] == "LR":
                        # pop the top of the stack and add to the postfix
                        popped_element = stack.popleft()
                        postfix.append(popped_element)
                    # if associativity of char is Right to left
                    elif associativity[char] == "RL":
                        # push the new operator to the stack
                        stack.appendleft(char)
                        i += 1
                elif precedence_order[char] > precedence_order[top_element]:
                    # push the char into stack
                    stack.appendleft(char)
                    i += 1
                elif precedence_order[char] < precedence_order[top_element]:
                    # pop the top element
                    popped_element = stack.popleft()
                    postfix.append(popped_element)
        elif char == '(':
            # add it to the stack
            stack.appendleft(char)
            i += 1
        elif char == ')':
            top_element = stack[0]
            while top_element != '(':
                popped_element = stack.popleft()
                postfix.append(popped_element)
                # update the top element
                top_element = stack[0]
            # now we pop opening parenthases and discard it
            stack.popleft()
            i += 1
        # char is operand
        else:
            postfix.append(char)
            i += 1
        #     print(postfix)
        # print(f"stack: {stack}")

    # empty the stack
    if len(stack) > 0:
        for i in range(len(stack)):
            postfix.append(stack.popleft())
    # while len(stack) > 0:
    #     postfix.append(stack.popleft())

    return postfix


def isOperator(input):
    if (input == '+' or
        input == '-' or
        input == '*' or
        input == '/'):
        return True
    else:
        return False


def Make_tree(postfix):
    """
        this function gets a postfix and return root of our tree
    :param postfix:
    :return:
    """
    mystack = []
    for i in postfix:
        mytree = Node(i)
        if isOperator(i):
            temp1 = mystack.pop()
            temp2 = mystack.pop()
            mytree.right = temp1
            mytree.left = temp2
        mystack.append(mytree)
    mytree = mystack.pop()
    return mytree


class Node:
    """
    this class is used for declaring a tree that has a value and right and left leaves
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key     # self.data = key


def Inorder(root):
    """
        this function return the inorder description of our tree
    :param root:
    :return:
    """
    if root:
        Inorder(root.left)
        print(root.val, end=" ")
        Inorder(root.right)


def Fitness(tree, input_list, output_list):
    """
        in Fitness function, we give a value from our input_list to the tree
        and then, calculate the value that tree gives us
        then we will find its difference to the output
        we sum all the differences and calculate our fitness
        the less our difference, the better fitness we have
    :param tree:
    :param input_list:
    :param output_list:
    :return:
    """
    distance = 0
    for i in range(len(input_list)):
        dis1 = Calculate(tree, float(input_list[i]))
        distance += abs(dis1 - output_list[i])
    if distance == 0:
        return 101
    else:
        return round(100 / distance, 3)


def Calculate(node, Sepcial_value) -> float:
    """
        this function, gives us the value of our tree with x
    :param node:
    :param Sepcial_value:
    :return:
    """
    if isOperator(node.val) == False:
        if(node.val == "x"):
            return Sepcial_value
        else:
            node.val = float(node.val)
            val1 = float(node.val)
            return val1
    left_value = Calculate(node.left, Sepcial_value)
    right_value = Calculate(node.right, Sepcial_value)
    # addition
    if node.val == "+":
        return left_value + right_value
    # subtraction
    elif node.val == "-":
        return left_value - right_value
    # division
    elif node.val == "/":
        if(right_value == 0):
            return 1
        return left_value / right_value
    # multiplication
    elif node.val == "*":
        return left_value * right_value


def CrossOver(root1, root2):
    #chosing a node from tree 1
    list_nodes_root1 = []
    All_Nodes(root1, list_nodes_root1)
    node1 = random.choice(list_nodes_root1)

    # chosing a node from tree 2
    list_nodes_root2 = []
    All_Nodes(root2, list_nodes_root2)
    node2 = random.choice(list_nodes_root2)

    #make sure we do not swap an operand and an operator
    while(node1[1] == root1 or node2[1] == root2 or
          (not isOperator(node1[0]) and isOperator(node2[0])) or
          (isOperator(node1[0]) and (not isOperator(node2[0])))):
        node1 = random.choice(list_nodes_root1)
        node2 = random.choice(list_nodes_root2)

    # here we make parents of our nodes and them swap the nodes
    parent1 = FindParent(root1, node1[1])
    parent2 = FindParent(root2, node2[1])
    if(parent1.right == node1[1] and parent2.right == node2[1]):
        parent1.right, parent2.right = parent2.right, parent1.right
    if(parent1.left == node1[1] and parent2.right == node2[1]):
        parent1.left, parent2.right = parent2.right, parent1.left
    if(parent1.right == node1[1] and parent2.left == node2[1]):
        parent1.right, parent2.left = parent2.left, parent1.right
    if(parent1.left == node1[1] and parent2.left == node2[1]):
        parent1.left, parent2.left = parent2.left, parent1.left


def FindParent(root, special_node):
    """
        this function will find the parent of the node we want
    :param root:
    :param special_node:
    :return:
    """
    if root:
        if (root.left and root.left == special_node) or (root.right and root.right == special_node):
            return root or FindParent(root.left, special_node) or FindParent(root.right, special_node)
        else:
            return FindParent(root.left, special_node) or FindParent(root.right, special_node)


def All_Nodes(root, mylist):
    """
        this function will save all the nodes of the tree we enter
    :param root:
    :param mylist:
    :return:
    """
    if root:
        All_Nodes(root.left, mylist)
        mylist.append([root.val, root])
        All_Nodes(root.right, mylist)


def Mutation(root):
    """
        here we do our mutation and change a random value with another random value
    :param root:
    :return:
    """
    operators = ["+", "-", "*", "/"]
    operands = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "x"]
    list_nodes = []
    All_Nodes(root, list_nodes)
    mutation_node = random.choice(list_nodes)
    if mutation_node[1] == root:
        root.val = random.choice(operators)
    else:
        if isOperator(mutation_node[0]):
            mutation_node[1].val = random.choice(operators)
        else:
            mutation_node[1].val = random.choice(operands)

