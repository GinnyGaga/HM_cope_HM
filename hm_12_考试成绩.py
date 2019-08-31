# 练习2：定义两个整数变量python_score、c_score,编写代码判读成绩
python_score = int(input("python成绩为："))
c_score = int(input("c成绩为:"))
# 要求只要有一门成绩>60分就算合格
if python_score > 60 or c_score > 60:
    print("这位同学的成绩是合格的")
else:
    print("这位同学的成绩是不合格的")