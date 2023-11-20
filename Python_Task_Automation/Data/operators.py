# int형의 나눗셈 값은 항상 float 형으로 나온다. 
print(10 / 2)

# 몫만 나오게 하기 
print(10//2)

# 나눗셈 값만 나오게 하기 
print(10 % 3)

# int형으로 변환하기 
print(int(125.456789))
print(int(True))
print(int(False))
print(int("0925"))
print()
# float형으로 변환하기 
print(float(100))
print(float(True))
print(float(False))
print(float("0925"))
print()

# 문자형으로 변환하기 
print(str(100))
print(str(125.456789))
print(str(True))
print(str(False))
print()

# boolean 형으로 변환하기 
# False 
print(bool(0))
print(bool(0.0))
print(bool(""))
print()
# True
print(bool(1))
print(bool(1.0))
print(bool("str"))
print()

# 논리형 자료 비교연산자 
is_True = True 
is_False = False 
print(is_True > is_False) #True
print(is_True < is_False) #False
print()

# 문자형 자료 비교연산자 
# 소문자가 대문자보다 큰 값을 가지고 있다. 
print("Python" < "python") #True
print("100" < "200") #True
print()

# and 연산에서 and가 여러개일 때
#거짓으로 판별될 경우, 거짓으로 판별된 첫번째 값이 값으로 출력된다.  
print("a" and 0 and True and False) # 0

# or 연산에서 or가 여러개일 때
#하나라도 참으로 판별될 경우, 참으로 판별된 첫번째 값이 값으로 출력된다.  
print(0 or 0.0 and False or "a") # a

# and와 or의 우선순위 
# and 연산이 or 연산보다 우선순위가 높다. 
print(True or False and "참")

