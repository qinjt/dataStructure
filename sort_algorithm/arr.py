"""
@Time: 2018/9/28 16:31
@Author: dameng
@email: 15294156319@163.com
"""

from array import ArrayType

arr = ArrayType('i', [1, 2, 3, 4, 5])

for i in arr:
    print(i)
    
print(arr[3])

print(type(arr))
