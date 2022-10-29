# a = [ 1,4,6,2,0]
# b = a
# b.append(3)
# print( a is b)
# print(a)
# print(b)


# c = [ 1,4,6,2,0]
# d = c.copy()
# d.append(3)

# print( c is d)
# print(c)
# print(d)


# tup_a = ('a','b','c')
# tup_b = ('a','b','c')

# print(tup_a is tup_b)


# a = -6
# b = -6
# print (id(a))
# print(id(b))
# print(hash(a))
# print(hash(b))
# print(a is b)


# a = 3
# b = 3
# print (id(a))
# print(id(b))
# print(hash(a))
# print(hash(b))
# print(a is b)

# my_list = [1,4,5,6,8]

# def print_list(seq):
#     print(id(seq))
#     for item in seq:
#       print(item)
      
# print (id(my_list))
# print_list(my_list)

a = ([1, 2, 3], "abc", 56)

print(id(a))

a[0][0] = 2

print(id(a))