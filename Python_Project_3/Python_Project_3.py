while True:
    try:
        User = int(input('몇 명이 입력하시나요? '))
        print()
    except ValueError:
        print()
        print('타입이 맞지 않습니다. 수를 입력해주세요.')
        print() 
    except NameError:
        print()
        print('타입이 맞지 않습니다. 수를 입력해주세요.')
        print()       
    else:
        products = [] * User
        n = 0
        for i in range(User):
            n = n + 1
            print(n, '번째 사용자가 입력할 차례입니다.')
            print()
            productname = input('상품명을 입력해주세요: ')
            print()
            while True:
                try:
                    price = int(input('상품 가격을 입력해주세요: '))
                    print()
                except ValueError:
                    print()
                    print('타입이 맞지 않습니다. 수를 입력해주세요.')
                    print() 
                except NameError:
                    print()
                    print('타입이 맞지 않습니다. 수를 입력해주세요.')
                    print()
                else:
                    madein = input('상품 원산지를 입력해주세요: ')
                    print()
                    quantity = input('상품 용량을 입력해주세요: ')
                    print()
                    while True:
                        try:
                            discount = int(input('상품 할인율을 입력해주세요: '))
                            print()
                        except ValueError:
                            print()
                            print('타입이 맞지 않습니다. 수를 입력해주세요.')
                            print() 
                        except NameError:
                            print()
                            print('타입이 맞지 않습니다. 수를 입력해주세요.')
                            print()
                        else:
                            finalprice = price - (price * (discount / 100))
                            products.insert(i, [productname, price, madein, quantity, discount, int(finalprice)])
                            i = i + 1
                            break
                    break
        break
print('리스트 원소의 첫번째는 상품명,')
print()
print('두번째는 상품 원가격,')
print()
print('세번째는 상품 원산지,')
print()
print('네번째는 상품 용량,')
print()
print('다섯번째는 상품 할인율,')
print()
print('여섯번째는 할인된 최종가격입니다.')
print()
print('↓ 상품 입력 정보 결과 ↓')
print()
print(products)
