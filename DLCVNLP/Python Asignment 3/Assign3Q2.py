"""Write List comprehensions to produce the following Lists

['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]

[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""
result = [ item*num for item in ["x","y","z"] for num in range(1,5)  ]
print("1 -> " +   str(result))

result = [ item*num for num in range(1,5) for item in ["x","y","z"] ]
print("2 -> " +   str(result))

result = [ [item+num] for num in range(0,3) for item in [2, 3, 4] ]
print("3 -> " +   str(result))

result = [ [item+num  for item in [2, 3, 4]] for num in range(0,3) ]
print("4 -> " +   str(result))

result = [ (num,item)  for item in range(1,4) for num in range(1,4) ]
print("4 -> " +   str(result))
