# Salior uniform is the best!
# Actually, I always call list 数组, but the book call it 列表. I think 数组 is more suitable for me.

数组 = ['eric', 'mashiro', 'shizuyama', ['p', 'maru', 'sama']]
print(数组)
print(数组[0])
print("The book said other unicode chracters can be used as variable names, so I can use 数组 as a variable name.")
print(f"{数组[3][0].upper()}{数组[3][1]}{数组[3][2]}")

# Actually, Chinese characters can be used as variable names, but It's so hard to type them.
names = 数组
print(names)

names[0] = 'pmarusama'
print(names)

names.append('shizuyama')
names.append('hina')
print(names)

names.insert(0, 'aris')
print(names)

del names[2]
print(names)

removed_name = names.pop()
print(removed_name)
print(names)