# Character = :(

var1 = "Z-Digital"
var2 = "Software testing"

print("var1[0] will be: ", var1[0])
print(var2[2:6])

# [] - slice
# [:] - range slice

x = "Guru"
print("g" not in x)

prefix = "Z"
name = "Digital"
number = 2016

print('%s-%s was born in %d' % (prefix, name, number))

oldstring = "I like Z-Digital"
newstring = oldstring.replace("like", "love")
print(newstring)

test_data = "this IS z-digital"

print(test_data.upper())
print(test_data.lower())
print(test_data.capitalize())

# JOIN
print(":".join("Python"))

# REVERSED
string = "12345"
# BAD WAY
string_reverse = reversed(string)
# NICE WAY
print("".join(reversed(string)))

word = "Z-Digital Group provides you a great career"
print(word.split(" "))
print(word.split("i"))

# IMMUTABLE
x = "Z-Digital"
x = x.replace("Z-Digital", "Python")
print(x)
