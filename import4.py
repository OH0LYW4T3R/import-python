#1
print("""총 3대의 매물이 있습니다.
강남아파트 매매 10억 2010년
마표 오피스텔 전세 5억 2007녕
송파 빌라 월세 500/50 2000년""")

#2
class SoldOutError(Exception):
    def __init__(self):
        super().__init__('재고가 소진되어 더 이상 주문을 받지 않습니다.')


try:
    #num = int(input(">>"))

    if(num < 1):
        raise ValueError
    elif(num > 10):
        raise SoldOutError

      
except ValueError as e:
    print("잘못된 값을 입력하였습니다.")
except Exception as e:
    print(e)

#1
class Human():
    def __init__(self):
        print("응애응애")

human = Human()

#2
class Human():
    def __init__(self, nm):
        print(nm, "님이 태어났습니다.")

human = Human("유종훈")
human = Human("조현호")

#3
class Human():
    def __init__(self, nm, y):
        self.year = y
        print(self.year)

human = Human("유종훈", 1986)
human.year

#4
class Human():
    def __init__(self, nm):
        self.first = nm[0]
        self.name = nm[1:]
    

human = Human("유종훈")
print(human.first)
print(human.name)

#5
class Human():
    def __init__(self, nm1, nm2):
        self.fri1 = nm1
        self.fri2 = nm2

human = Human("유종훈", "조현호")
print(human.fri1)
print(human.fri2)

#6
class Human():
    def __init__(self, nm1, nm2):
        self.friend = [nm1, nm2]

human = Human("유종훈", "조현호")
print(human.friend)

#7
class Human():
    def __init__(self):
        self.friend = []

    def addfri(self, nm):
        self.friend.append(nm)


human = Human()
human.addfri("김하나")
human.addfri("김기리")
print(human.friend)

#8
class Human():
    def __init__(self, nm, nmls):
        self.friend = []
        self.name = nm

        for i in nmls:
            self.friend.append(i)

    def addfri(self, nm):
        self.friend.append(nm)

human = Human("유종훈", ["김철수", "김영희"])
human.addfri("김범수")
print(human.name)
print(human.friend)

#9
class Human():
    def __init__(self, nm, nmls):
        self.friend = []
        self.name = nm

        for i in nmls:
            self.friend.append(i)

    def addfri(self, nm):
        self.friend.append(nm)
    
    def list(self):
        print(self.name,"친구목록")
        for i in self.friend:
            print("-",i)

human = Human("유종훈", ["김철수", "김영희"])
human.list()

#10
class Human():
    def __init__(self, nm, nmls):
        self.friend = []
        self.name = nm

        for i in nmls:
            self.friend.append(i)

    def addfri(self, nm):
        self.friend.append(nm)
    
    def list(self, n):
        for i in range(n):
            print(self.friend[i])

human = Human("유종훈", ["김철수", "김영희", "박영수", "이미자"])
human.list(3)
human.list(1)

#11
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def __init__(self):
        pass

    def fly(self):
        print("날다")


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

#12
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print("0")

#13
per = ["10.31", "", "8.00"]
ary = []

for i in per:
    try:
        print(float(i))
        ary.append(float(i))
    except ValueError:
        print("0")
        ary.append(0.0)

#14
try:
    num = 2
    num2 = 0

    result = num / num2
except ZeroDivisionError as e:
    print(e)

#15
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

#16
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print("0")
    else:
        print("clear")
    finally:
        print("예외가 있을까??")

#17
class Car():
    
    def run(self):
        print("차가 달립니다.")
        
class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")

t = Truck()
t.load()

#18
class Human():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.
person = Human("설지석", 95)


print(person)

#19
class MyException(Exception):
    def __init__(self):
        pass
    
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")