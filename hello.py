friends = ["ahmed", "ali"]
"""
index rule    0       1    

["in an array/list each element has an index"]
in most programming languages we start counting from 0 and python is one of them
as we said above the element "ahmed" has an index of 0 and "ali" has an index of 1
an array/list is an ordered data structure wich means always elements are ordered in the order u assigneds
"""

popped_ali = friends.pop()
print("popped " + popped_ali) # removed ali [because its at the end pop() means remove anything at the last index of an array/list]

popped_ahmed = friends.pop() # pop ahmed
print("popped " + popped_ahmed) 

friends.append("hello") # append hello 
print("appended hello") # we didnt print the append because it returns None wich means nothing

print(friends) # print array/list

"""
note the implementation of an array can differ
from a list because both are different data structures
but from a user point of view its the same thing
but in a behind the scenes point of view its different alot
and in python a list is implemented behind the scenes
but in other languages like javascript an array is implemented behind the scenes
note that u can make ur own data structures and there are many!!!! data structures in python
like a dictionary {}
a tuple ()
a list []
and more
"""
