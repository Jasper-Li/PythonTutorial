# 1. bool type
is_human = True
is_smart = False

print('type is_human:', type(is_human))

if is_human and is_smart:
    print("a smart human.")
elif is_human and not is_smart:
    print("a human, but not smart.")
else:
    print("Who are you?")

# 2. compare
if 1 > 3:
    print('1 > 3')
else:
    print('1 > 3 is wrong')

# 3. in
people = ("唐僧", "悟空", "八戒", "沙僧")

if '悟空' in people:
    print('悟空 is here')
else:
    print('悟空 is not here')

if '白龙' not in people:
    print('白龙 is not here')
else:
    print('白龙 is here')
