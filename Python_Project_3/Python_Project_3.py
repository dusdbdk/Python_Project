while True:
    try:
        User = int(input('�� ���� �Է��Ͻó���? '))
        print()
    except ValueError:
        print()
        print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
        print() 
    except NameError:
        print()
        print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
        print()       
    else:
        products = [] * User
        n = 0
        for i in range(User):
            n = n + 1
            print(n, '��° ����ڰ� �Է��� �����Դϴ�.')
            print()
            productname = input('��ǰ���� �Է����ּ���: ')
            print()
            while True:
                try:
                    price = int(input('��ǰ ������ �Է����ּ���: '))
                    print()
                except ValueError:
                    print()
                    print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
                    print() 
                except NameError:
                    print()
                    print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
                    print()
                else:
                    madein = input('��ǰ �������� �Է����ּ���: ')
                    print()
                    quantity = input('��ǰ �뷮�� �Է����ּ���: ')
                    print()
                    while True:
                        try:
                            discount = int(input('��ǰ �������� �Է����ּ���: '))
                            print()
                        except ValueError:
                            print()
                            print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
                            print() 
                        except NameError:
                            print()
                            print('Ÿ���� ���� �ʽ��ϴ�. ���� �Է����ּ���.')
                            print()
                        else:
                            finalprice = price - (price * (discount / 100))
                            products.insert(i, [productname, price, madein, quantity, discount, int(finalprice)])
                            i = i + 1
                            break
                    break
        break
print('����Ʈ ������ ù��°�� ��ǰ��,')
print()
print('�ι�°�� ��ǰ ������,')
print()
print('����°�� ��ǰ ������,')
print()
print('�׹�°�� ��ǰ �뷮,')
print()
print('�ټ���°�� ��ǰ ������,')
print()
print('������°�� ���ε� ���������Դϴ�.')
print()
print('�� ��ǰ �Է� ���� ��� ��')
print()
print(products)
