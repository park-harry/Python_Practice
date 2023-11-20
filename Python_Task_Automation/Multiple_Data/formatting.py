left = "left"
right = "right"
middle = "middle"

# <,>,^
print("({2:>10s}), ({1:^10s}), ({0:<10s})".format(left,middle,right))
# left은 왼쪽 정렬, middle은 가운데 정렬, right은 오른쪽 정렬
# 각 변수마다 10칸 공백

#공백 부분에 기호 넣기 
print("({2:!>10s}), ({1:@^10s}), ({0:#<10s})".format(left,middle,right))

#지정해준 숫자만큼의 글자를 출력하고 남은 공간에 특수 기호로 채움 
print("({2:!>10.4s}), ({1:@^10.3s}), ({0:#<10.2s})".format(left,middle,right))

#f-string 
weather = "맑음"
temperature = 20 

print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")