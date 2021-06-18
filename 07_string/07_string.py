# 07 string, 字符串

fruit = 'Apple'
# 序号： 01234
print(fruit)
print('01234')
print()

print('0号', fruit[0])
print('1号', fruit[1])
print('-1号', fruit[-1])
print('从1报数', fruit[1:])
print('1数到3', fruit[1:3])  # 前闭后开
print('length', len(fruit))
print()

foods = 'Apple Banana Milk Bread'
eats = foods.split(' ')
print('eats', eats)
