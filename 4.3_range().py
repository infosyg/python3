for value in range(1,5):
    print(value)
numbers = list(range(1, 5))
print(numbers)
#range 指定步长 3
even_numbers = list(range(2,21,3))
print(even_numbers)

#10个整数平方加入到一个列表
squares = []
for value1 in range(1, 11):
    square = value1**2  #使用一个square临时变量
    squares.append(square)
print(squares)
#同样10个整数平方，更简洁做法,不使用临时变量。直接把值追加到squares。
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#同样10个整数平方，更简洁做法, 列表解析和创建新元素代码合并一行，并追加新元素。
squeres = [value ** 2 for value in range(1,11)]
print(squares)
