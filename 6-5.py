import copy

print("<< Shallow Copy >>")
a = [1, 2, 3, 4]
b = a  # 얕은 복사, shallow copy
print(b)  # [1, 2, 3, 4]
b[2] = 10
print(b)  # [1, 2, 10, 4]
print(a)  # [1, 2, 10, 4] b[2]에 대입한 10이 a[2]에서도 출력

print("<< Deep Copy >>")
c = [1, 2, 3, 4]
d = copy.deepcopy(c)
print(c)  # [1, 2, 3, 4]
d[2] = 10
print(d)  # [1, 2, 10, 4]
print(c)  # [1, 2, 3, 4] c는 변하지 않고 그대로 3을 출력
