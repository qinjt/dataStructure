"""
@Time: 2018/11/2 12:43
@Author: dameng
@email: 15294156319@163.com
"""

class Node(object):
    
    def __init__(self, data, left=None, right=None):
        
        """
        初始化
        :param data: 节点数据
        :param left: 左孩子
        :param right: 右孩子
        """
        self.data = data
        self.left = left
        self.right = right
        
        
class BST(object):
    
    def __init__(self):
        self._root = None
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def add(self, val):
        if self._root is None:
            self._root = Node(val)
            self.size += 1
        else:
            self._add(self._root, val)
            
    def contains(self, item):
        
        """
        查找元素
        :param item: 要查找的元素
        :return: True/False
        """
        return self._contains(self._root, item)
    
    def preOrder(self):
        """
        前序遍历（递归）
        :return:
        """
        self._preOrder(self._root)
        
    def preOrderNR(self):
        """
        前序遍历（非递归
        :return:
        """
        
    def inOrder(self):
        """
        中序遍历
        :return: None
        """
        
        self._inOrder(self._root)
        
    def postOrder(self):
        """
        后序遍历
        :return: None
        """
        
        self._postOrder(self._root)
    
            
    def _add(self, node, val):
        if node is None:
            self.size += 1
            return Node(val)
        
        else:
            if val < node.data:
                node.left = self._add(node.left, val)
            elif val > node.data:
                node.right = self._add(node.right, val)
                
        return node
    
    def _contains(self, node, val):
        if node is None:
            return False
        
        if val == node.data:
            return True
        elif val < node.data:
            return self._contains(node.left, val)
        else:
            return self._contains(node.right, val)
        
    def _preOrder(self, node):
        
        if node is None:
            return
        
        print(node.data)
        self._preOrder(node.left)
        self._preOrder(node.right)
        
    def _inOrder(self, node):
        
        if node is None:
            return
        
        self._inOrder(node.left)
        print(node.data)
        self._inOrder(node.right)
        
    def _postOrder(self, node):
        
        if node is None:
            return
        
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.data)
        
            
            
        
            
        
        
        
        