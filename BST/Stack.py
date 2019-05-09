"""
@Time: 2018/11/2 19:45
@Author: dameng
@email: 15294156319@163.com
"""

from Stack import Stack

class Stack(object):
    """
    栈的定义
    定义
    """
    
    def __init__(self):
        self._items = []
        
    def is_empty(self):
        return self._items == []
    
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[len(self._items) - 1]
    
    def size(self):
        return len(self._items)