print("Hello, World!")

##############################################

#숫자형
a = 3
b = 4

print(type(a))
print('a를 b로 나눈 값 :', a/b)     #나누기
print('a를 b로 나눈 몫 :', a//b)    #몫
print('a를 b로 나눈 나머지 :', a%b) #나머지
print('a의 b제곱 :', a**b)          #제곱

##############################################

#문자열 자료형 (문자열 자료형은 immutable(불변)한 자료형이다. 따라서 문자열 자료형은 그 요솟값을 변경할 수 없다.)

#문자열 자료형 만들기
string1 = "Python's favorit food is perl"
string2 = '"python is very easy." he says.'
string3 = 'Python\'s favorit food is perl' #백슬래시 + 따옴표 예시 (문자 따옴표를 쓸 거니까 이 따옴표는 스트링의 시작과 끝이 아닌 문자열 따옴표라는 것을 알려주는 것)
string4 = "\"Python is very easy.\" he says."
string5 = 'Life is too short \nYou need python' #이스케이프 코드
string6 = """Life is too short
You need python
as dsf
 ddd s""" #여러줄로 이루어진 문자열은 따옴표 3개로 만들면 편리함. (따옴표 3개로 문자열을 만들면 이스케이프 문자가 없어도 문장의 모양이 동일하게 출력된다.)

print(string1)
print(string2)
print(string3)
print(string4)
print(string5)
print(string6)

#문자열 더해서 연결하기
a = "Python"
b = " is fun!"
print(a + b) #문자열 더하기
print(a * 2) #문자열 곱하기 (문자열 a를 2번 출력해라)
#문자열 인덱싱 (다른 언어에는 string에 인덱싱이 없다. 하기위해서는 함수 사용해야함 파이썬만 기본제공)
c = "Life is too short, You need Python" #문자열이 있으면 각 자리마다 숫자로 번호가 매겨짐
print('문자열 e의 길이는 :', len(c)) #문자열 길이 구하기(len 함수는 기본 내장 함수)
print(c[0])
print(c[-1]) #인덱싱에서 -는 역방향

#문자열 슬라이싱    ***a[(이상):(미만):(간격)]***
#표현방법 ***a[(이상):(미만):(간격)]***   기본은 0일 때를 의미(이상은 기본 0부터, 미만은 기본 문자열 마지막 인덱스 값, 간격은 기본 1칸)
print(c[0:4]) #인덱스 0~4까지 출력(띄어쓰기 포함)
print(c[:8]) #0~8미만까지 출력 즉, 0~7까지 출력
print(c[8:]) #8~문자열 끝까지 출력
print(c[::-1]) #역방향으로 출력

#문자열 포매팅 (c언어와 비슷함)
d = "I eat %s apples. so I was sick for %s days." % (3, "three") #%s는 무적
e = "I eat %s apples. si I was sick for {} days.".format("이삼일")
f = "asdfs{age}adfdasf {name} asdfsdafaa".format(name="최예제", age='스무살')

name = "int"
g = f"나의 이름은 {name}입니다." #f문자열 포매팅

print(d)
print(e)
print(f)
print(g)

#문자열 정렬과 공백(소수점 표현할 때 빼면 이걸 쓰긴 쓰나...?)
h = "%10s" % "hi" #전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미.
i = "%-10s" % "hi" #전체 길이가 10개인 문자열 공간에서 대입되는 값을 왼쪽으로 정렬하고 그 뒤의 나머지는 공백으로 남겨 두라는 의미.
j = "%0.4f" % 3.42134234 #%(문자열의 전체 길이).(소수점 남기는 자리 수) => %0.4
k = "%10.4f" % 3.42134234 #숫자 3.42134234를 소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하라는 의미.
print(h)
print(i)
print(j)
print(k)

#문자열 개수 세기(.count()함수 사용)
l = "hobby"
print(l.count('b')) #문자열 n에 들어가있는 b의 개수를 리턴함

#문자열에 있는 문자의 위치를 찾는 함수(.find()함수 사용), (.index()함수 사용) 사용방법은 동일함
print(l.find('b')) #문자열 n에서 가장 먼저 나오는 b의 인덱스 값을 찾아서 리턴(두 번째 b는 안나옴, 처음에 나온 b의 인덱스 값만 리턴됨)
print(l.find('x')) #찾는 값이 문자열에 없으면 -1을 리턴
print(l.index('b')) #.find()함수와 동일
#print(l.index('x')) #찾는 값이 문자열에 없으면 에러 메시지 출력

#.join()함수 (리스트나 튜플에서 자주 사용)
m = ",".join("abcd") #","이 스트링을 기준으로, .join(abcd)은 뒤에 나온 "abcd"이 문자열을 쪼개서 조인을 하겠다는 의미.
print(m)

n= ",".join(["aaa", "bb", "c"]) #","를 기준으로, .join(["a", "b", "c"])은 뒤에 있는 리스트를 쪼개서 스트링 하나로 만들어준다.
print(n)

#.upper()함수 (소문자를 대문자로 바꾸는 함수)
#.lower()함수 (대문자를 소문자로 바꾸는 함수)
#.strip()함수 (양쪽 공백을 지우는 함수)

#.replace()함수 replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환해 줌.
o = "Life is too short"
o.replace("Life", "Your leg") #"Life"를 "Your leg"로 치환함.
print(o)

#.split()함수 split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
# 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다.
p = "a:b:c:d"
print(p.split()) #띄어쓰기를 기준으로 잘라서 리스트로 만든다.
print(p.split(":")) #':' 표시를 기준으로 쉼표가 찍히고 리스트가 만들어진다.

#############################################

#리스트 (변수 여러 개를 묶는 역할), 하나의 변수에 여러 개의 값을 관리할 때 사용함
a = [1, 2, "int", "최예제", ["원숭이", "벌크업"]]

print(a)
print(a[3])
print(a[4])
print(a[4][1])

#리스트도 스트링과 마찬가지로 (인덱싱, 슬라이싱, 리스트 더하기, 리스트 곱하기)
#리스트는 스트링과 다르게 ((불변자료형이 아니다. 따라서 리스트 자료형은 요솟값을 변경할 수 있다.), (인덱스 요솟값을 수정할 때 슬라이싱을 이용하여 수정할 수 있다.), (del a[] 또는 a[1] = []를 하면 즉, 리스트가 있을 때 빈 리스트로 교체를 하면 바뀐다.(해당 리스트 삭제)), )

#.append()함수