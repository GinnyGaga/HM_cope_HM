# 练习1：定义一个整数变量, 编写代码判断年龄是否正确
age = int(input("这个年龄输写对么？"))
# 人的年龄应该在0-120之间
if age >=0 and age <= 120:
    print("这个年龄%d是对的。" % age)
else:
    print("这个年龄%d是不对的。" % age)
