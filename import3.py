#1
for i in range(1, 51):
    str1 = "./testfile/" + str(i) + "주차.txt"
    name = "- " + str(i) +" 주차 주간 보고 -\n"

    with open(str1,"+w") as f:
        f.write(name)
        f.write("부서 : \n")
        f.write("이름 : \n")
        f.write("업무 요약 : \n")
    
#2
with open("./testfile/매수종목1.txt","+w") as f:
    f.write("005930\n")
    f.write("005380\n")
    f.write("035420\n")
#3
with open("./testfile/매수종목2.txt","+w") as f:
    f.write("005930 삼성전자\n")
    f.write("005380 현대차\n")
    f.write("035420 NAVER\n")
#4
with open("./testfile/매수종목.csv","+w", encoding="cp949") as f:
    f.write("종목명,종목코드,PER\n")
    f.write("삼성전자,005930,15.79\n")
    f.write("NAVER,035420,55.82\n")
#5
lines = []

with open("./testfile/매수종목1.txt","+r") as f:
    lines.append(f.readline())
    lines.append(f.readline())
    lines.append(f.readline())

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)
#6
#7
#8
#9
#10
class Human():
    def __init__(self, name, age, sex):
        print("응애응애")
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("이름","25", "여자")

print("이름 : ",areum.name,", 나이 : ",areum.age,", 성별 :",areum.sex)

#11
#12
#13
#14
#15
class 사람():
    def __init__(self, name, year):
        print("응애응애")
        print(name,"님이 태어났습니다.")
        self.year = year
        self.성 = name[0]
        self.이름 = name[1:3:1]

human = 사람("유종훈",1986)
print(human.성)
print(human.이름)

#15
#16
#17
#18
class 사람1():
    def __init__(self, name, name2):
        self.친구0 = name
        self.친구1 = name2
        self.친구 = [name, name2]
        self.친구들 = []

    

    def 친구추가(self, string):
        self.친구들.append(string)


human = 사람1("유종훈", "조현호")

print(human.친구0)
print(human.친구1)
print(human.친구)

human.친구추가("김하나")
human.친구추가("김기리")
print(human.친구들)


#18
#19
#20

class 사람2():
    def __init__(self, name, ls):
        self.친구들 = []
        self.이름 = name
        self.친구들 = self.친구들 + ls

    def 친구추가(self, string):
        self.친구들.append(string)

    def 친구목록1(self):
        print(self.이름,"친구목록")
        print("-", self.친구들[0])
        print("-", self.친구들[1])

    def 친구목록2(self,i):
        for j in range(i):
            print(self.친구들[j])

    

human = 사람2("유종훈", ["김철수", "김영희"])
human.친구추가("김범수")
print(human.이름)
print(human.친구들)
human.친구목록1()

human2 = 사람2("유종훈", ["김철수", "김영희", "박영수", "이미자"])
human2.친구목록2(3)
human2.친구목록2(1)