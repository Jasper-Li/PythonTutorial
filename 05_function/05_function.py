#05 function
# 消除重复 --> 引入函数(封装)

def print_circle(r):
    print('半径', r)    #以缩进表示上下从属关系
    print('直径', 3 * r)
    print('周长', 2 * 3.14 * r )
    print('面积', 3.14 * ( r ** 2) )
    print()

print_circle(3, '-'*15)
print_circle(4, '-'*20)
print_circle(4, '-'*20)
print_circle(5, '#'*25)
