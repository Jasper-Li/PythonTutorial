# 06 tuple 2, 序列

people = ("唐僧", "悟空", "八戒", "沙僧")   #tuple, 可变
# 序号：     0      1        2      3
def print_people(people):
    print(people)
    print('0号', people[0])
    print('1号', people[1])
    print('-1号', people[-1])
    print('人数', len(people))  
    print()

print_people(people)

people = ["唐僧", "悟空", "八戒", "沙僧"]   #list, 可变
people.append('白龙')
print_people(people)
