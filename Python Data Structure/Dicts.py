Dict = {'Tim' : 18, 'Charlie' : 20, 'Tiffany' : 22, 'Rob' : 15}

Boys = {'Tim' : 18, 'Rob' : 15}
Girls = {'Charlie' : 20, 'Tiffany' : 22}

studentX = Boys.copy()
studentY = Girls.copy()

print(Dict)
Dict.update({'Sarah' : 9})
print(Dict)

# print(studentX)
# print(studentY)

del Dict ['Charlie']
print(Dict)

print("Students name: %s" % list(Dict.items()))

for key in list(Dict.keys()):
  if key in list(Boys.keys()):
    print('It is a boy')
  elif key in list(Girls.keys()):
    print('It is a girl')
  else:
    print('I do not really know who is it')

Students = list(Dict.keys())
Students.sort()
for S in Students:
  print(":".join((S, str(Dict[S]))))

print("Length: %d" % len(Dict))
print(type(Dict))
print(str(Dict))
