tup = ('Jan', 'Feb', 'Mar');
tup1 = ();
tup2 = (50,);

# TUPLE ASSIGNMENT
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7);

print(tup1[0])
print(tup2[1:4])

# Packing
x = ("Z-Digital", 20, "Outsource")
# Unpacking
(company, emp, profile) = x
print(company)
print(emp)
print(profile)

# COMPARING
a = (5, 6)
b = (5, 8)
if (a > b):
  print("a is bigger")
else:
  print("b is bigger")

# directory[last, first] = number
#   for last, first in directory:
#     print first, last, directory[last, first]

# TUPLES AND DICTIONARIES
a = {'x':100, 'y':200}
b = list(a.items())
print(b)

del(tup1)

x = ("a", "b", "c", "d", "e")
print(x[2:4])

# all() any() enumerate() max() min() sorted() len() tuple()

