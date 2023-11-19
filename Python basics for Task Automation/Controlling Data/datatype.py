# int(정수) 형 
a,b,c = 5,-5,0
print(type(a), type(b), type(c))

# float(실수) 형 
d,e,f = 5.5, -5.5, 0.0
print(type(d),type(e),type(f))

#과학적 표기법 
# 1.234567e5 -> e 다음에 오는 숫자만큼 10의 제곱이 곱해진다. 
g = 1.234567e5 
print(g)

# 탈출문자 
# \', \", \\, \n, \r, \t

#작은 따옴표 출력
text1 = "Python 'is' Easy"
print(text1)
#역슬래쉬 (\) 출력 
text2 = "Python \is\ Easy"
print(text2)
#\r 사용시, \r 뒤에 있는 문자열만 출려된다. 
text3 = "Java, \rPython is Easy"
print(text3)
#\t는 tab의 역할을 한다.  
text3 = "Python \tis Easy"
print(text3)

#print의 역할 
a,b = 10,20
#변수와 변수 사이에 들어갈 문자 또는 기능 
print(a,b , sep=',')
#행의 마지막에 포함될 문자 또는 기능 
print(a,b , end='...')

#내장함수와 메서드 
# print() -> 내장함수 
# str.upper() -> 메서드  

#False 인 경우 
# 1. False
# 2. 값이 0인 경우 
# 3. [], (), {} 안에 null 값이 있는 경우 

