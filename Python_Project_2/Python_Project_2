star = 1
num = 0
a = 7

def name() :
    while(True):
        print()
        name = input("성명을 입력하세요 : ")
        if name == "김준혁":
            print()
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력 해주세요. (김준혁)")
            print()
        
def classyear() :
    while(True):
        classyear = input("학번을 입력하세요 : ")
        if classyear == "U202002265":
            print()
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력 해주세요. (U202002265)")
            print()

def test(*numbers) :
    for n in numbers:
        b = a * n
    return b

def multiple() :
        begin = 1
        num = int(input("정수값을 입력해주세요 (정수 이외의 값은 입력할 수 없습니다.) : "))
        for num in range(begin, num+begin):
            print()
            if star ==1:
                print("★☆★☆★☆★☆★☆")
                print("☆                        ★")
                if (num+1) % 2 == begin:
                    print("☆        ", num, "단         ★")
                    print("★                        ☆")
                    for num2 in range(begin, num+begin):
                        sum1 = num * num2
                        if (sum1<10):
                                if ((num2 + 1) % 2 == begin) :
                                    print("☆    ", num, "x", num2, "=", num * num2, "     ★")
                                else :
                                    print("★    ", num, "x", num2, "=", num * num2, "     ☆")
                        else :
                                if ((num2+1) % 2 == 1) :
                                    print("☆    ", num, "x", num2, "=", num * num2, "   ★")
                                else :
                                    print("★    ", num, "x", num2, "=", num * num2, "   ☆")
                    print("★                        ☆")
                    print("☆★☆★☆★☆★☆★")
                                
                else :
                    print("★        ", num, "단         ☆")
                    print("☆                        ★")
                    for num2 in range(begin, num+begin):
                        sum1 = num * num2
                        if (sum1<10):
                                if ((num2 + 1) % 2 == begin) :
                                    print("☆    ", num, "x", num2, "=", num * num2, "     ★")
                                else :
                                    print("★    ", num, "x", num2, "=", num * num2, "     ☆")
                        else :
                                if ((num2+1) % 2 == begin) :
                                    print("☆    ", num, "x", num2, "=", num * num2, "   ★")
                                else :
                                    print("★    ", num, "x", num2, "=", num * num2, "   ☆")
                    print("★                        ☆")
                    print("☆★☆★☆★☆★☆★")
                
name()
classyear()
print("환영합니다, 김준혁님.")
print()
while(True):
    what = int(input("무엇을 할까요? (1 = 입력받은 수 n x n 단 출력, 2 = 곱하기 퀴즈) : "))
    print()
    if what == 1 :
        multiple()
        break
    if what == 2 :
            answer = test(7, 6)
            ask = int(input("7곱하기 6은? : "))
            print()
            if answer == ask :
                print("정답입니다!")
                break
            else :
                    print("오답입니다. 다시 공부하세요.")
                    print()
    else :
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            print()
