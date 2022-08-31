# input값에 split()함수를 사용하면 선언된 변수의 형태는 list의 형태를 갖는다.
from posixpath import split


number_list = int(input("enter name : ").split())
print(type(number_list))