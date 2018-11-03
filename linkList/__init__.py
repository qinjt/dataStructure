"""
@Time: 2018/9/28 17:45
@Author: dameng
@email: 15294156319@163.com
"""
from LinkedList import LinkedList

linkList = LinkedList()
for i in range(10):
    linkList.append(i)
  
print(linkList)
linkList.delete(3)
print(linkList)
