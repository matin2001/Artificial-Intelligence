import numpy as np
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *,value=None):
        #feature is the attribute we are using in this node
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        # if the node is a leaf, it would have a value
        self.value = value

    def leaf_node_or_not(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=50, n_features=None):
        self.min_semples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None


    def fit(self, x, y):
        #setting how many features we have
        if self.n_features:
            self.n_features = min(self.n_features, x.shape[1])
        else:
            self.n_features = x.shape[1]
        # training the tree
        self.root = self.train_tree(x, y)


    def train_tree(self, x, y, depth=0):
        # in this function, we have to do multiple jobs and will mention them using comments
        # this is the initial information
        n_samples, n_features = x.shape
        n_labels = len(np.unique(y)) # n_labels show us if we have both positive and negative data and if it is equal to
                                     # 1 means that we have only one type and it is a leaf node

        # check our stopping criteria
        if (n_labels == 1 or depth>self.max_depth or n_samples<self.min_semples_split):
            #means that we don't need to grow another tree and it is a leaf node
            leaf_value = self.most_common_label(y)
            return Node(value=leaf_value)

        # finding the best split
        feature = np.random.choice(n_features, self.n_features, replace=False) # this line will make the tree avoid using used features
        best_feature ,best_threshold = self.find_best_split(x, y, feature)
        # line below will show the number of the feature we use in this state
        print("Chosen Feature Count : ", best_feature, "\tThe Threshold Chosen For the Feature: ", best_threshold)

        # creating the child node by calling this function again
        # so this is going to be a recursive function
        left_child, right_child = self.split(x[:, best_feature], best_threshold)
        left = self.train_tree(x[left_child, :], y[left_child], depth+1)
        right = self.train_tree(x[right_child, :], y[right_child], depth + 1)
        return Node(best_feature, best_threshold, left, right)


    def find_best_split(self, x, y, feature):
        best_gain = 0
        split_idx = None
        split_threshold = None
        for feature_index in feature:
            x_column = x[:, feature_index]
            thresholds = np.unique(x_column)
            for i in thresholds:
                # we should find the IG here
                information_gain = self.information_gain_finder(y, x_column, i)

                if information_gain>best_gain:
                    best_gain = information_gain
                    split_idx = feature_index
                    split_threshold = i

        return split_idx, split_threshold


    def information_gain_finder(self, y, x_column, thr):
        #based on the IG formula, we need to find some information
        #parent entropy
        parent_entropy = self.Entropy_calculator(y)

        # creating children
        left_child, right_child = self.split(x_column, thr)
        if len(left_child) == 0 or len(right_child) == 0:
            return 0

        # calculating weighted avg
        count = len(y)
        count_left = len(left_child)
        count_right = len(right_child)
        entropy_left = self.Entropy_calculator(y[left_child])
        entropy_right = self.Entropy_calculator(y[right_child])
        weighted_entropy = (count_left/count)*entropy_left + (count_right/count)*entropy_right

        #return the IG
        IG = parent_entropy - weighted_entropy
        return IG


    def split(self, x_column, thr):
        left = np.argwhere(x_column <= thr).flatten()
        right = np.argwhere(x_column > thr).flatten()
        return left, right


    def Entropy_calculator(self, y):
        hist = np.bincount(y)
        probabilities = hist / len(y)
        sum = (-1) * np.sum([p * np.log2(p) for p in probabilities if p>0])
        return sum


    def most_common_label(self, y):
        counter = Counter(y)
        selected_value = counter.most_common(1)[0][0]
        return selected_value


    def predict(self, x):
        return np.array([self.traverse(i, self.root) for i in x])

    def traverse(self, x, node):
        if node.leaf_node_or_not():
            return node.value
        if x[node.feature] <= node.threshold:
            return self.traverse(x, node.left)
        else:
            return self.traverse(x, node.right)