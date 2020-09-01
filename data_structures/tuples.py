tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# not valid for tuples changes values
# tup1[0] = 100

print('abc' in tup2) #prints True

# assigning result to new tuple
tup3 = tup1 + tup2
print(tup3) # prints 12, 34.56, 'abc', 'xyz'

