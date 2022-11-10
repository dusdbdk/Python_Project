print()
while(True):
    name = input("성명을 입력하세요 : ")
    if name == "김준혁":
        print()
        classyear = input("학번을 입력하세요 : ")
        if classyear == "U202002265":
            print()
            num = int(input("정수값을 입력해주세요 (정수 이외의 값은 입력할 수 없습니다.) : "))
            for num in range(1, num+1):
                print()
                print("★☆★☆★☆★☆★☆")
                print("☆                        ★")
                if (num+1) % 2 == 1:
                    print("☆        ", num, "단         ★")
                    print("★                        ☆")
                    for num2 in range(1, num+1):
                        sum1 = num * num2
                        if (sum1<10):
                                if ((num2 + 1) % 2 == 1) :
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
                    for num2 in range(1, num+1):
                        sum1 = num * num2
                        if (sum1<10):
                                if ((num2 + 1) % 2 == 1) :
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
            break
        else:
            print("잘못 입력하셨습니다. 성명부터 다시 입력 해주세요. (U202002265)")
            print()
    else:
        print("잘못 입력하셨습니다. 다시 입력 해주세요. (김준혁)")
        print()
