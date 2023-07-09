class Solution:
    @staticmethod
    def mango_tree_finder(row,column,x):
        """"
        Dora is interested so much in gardening and she plants more trees in her garden. She plants trees in a rectangular fashion with the order of rows and columns and numbered the trees in row-wise order. She planted the mango tree only in a 1st row, 1st column and last column. So given the tree number, your task is to find whether the given tree is a mango tree or not? Write a program to check whether the given number is a mango tree or not.
        Input consists of 3 integers
        The first input denotes the number of rows y
        The second input denotes the number of columns
        The third input denotes the tree number, which you have to find whether it's a mango tree or not.
        """
        if x<=row or x%column==0 or x%column==1:
            return "True"
        return "False"

if __name__ == '__main__':
    s=Solution()
    print(s.mango_tree_finder(5,5,11))
    print(s.mango_tree_finder(5,5,14))
    print(s.mango_tree_finder(10,60,2))


