class Product:
    new = 0
    def __init__(self, name = '', price = 0, madein = '', quantity = '', brand = '' ,discount = 0, finalprice = 0):
        Product.new += 1
        self.num = Product.new
        self.name = name
        self.price = price
        self.madein = madein
        self.quantity = quantity
        self.brand = brand
        self.discount = discount
        self.finalprice = int(finalprice)

    def __str__(self):
        print()
        print('입력된 상품(들)의 정보입니다.')
        print()
        return '상품번호: ' + str(self.num) + '\n\n' + '상품명: ' + str(self.name) + '\n\n' + '가격: ' +str(self.price)+'원' + '\n\n' +'원산지: ' +\
               str(self.madein) +'\n\n' + '용량: ' + str(self.quantity) + '\n\n' + '브랜드: ' + str(self.brand) + '\n\n' + '할인율: ' + str(self.discount) +'%' + '\n\n' + '최종금액: ' + str(self.finalprice) + '원'

class ProdManage:
    def __init__(self):
        self.data = []

    def insert(self, product):
        self.data.append(product)

    def remove(self, product):
        self.data.remove(product)

    def select(self, num):
        for i in self.data:
            if i.num == num:
                return i

    def selectAll(self):
        return self.data

class ProdDo:
    def __init__(self):
        self.manage = ProdManage()

    def addProd(self):
        print()
        print('상품 등록을 선택하셨습니다: ')
        print()
        name = input('상품명을 입력해주세요: ')
        print()
        price = int(input('상품 가격을 입력해주세요: '))
        print()
        madein = input('상품 원산지를 입력해주세요: ')
        print()
        quantity = input('상품 용량을 입력해주세요: ')
        print()
        brand = input('상품 브랜드를 입력해주세요: ')
        print()
        discount = int(input('상품 할인율을 입력해주세요: '))
        finalprice = price - (price * (discount / 100))
        product = Product(name, int(price), madein, quantity, brand, int(discount), int(finalprice))
        self.manage.insert(product)

    def printProd(self):
        print()
        print('상품 검색을 선택하셨습니다.')
        print()
        num = int(input('검색할 제품번호를 입력하세요: '))
        product = self.manage.select(num)
        if product == None:
            print()
            print('상품 검색 결과 없음.')
        else:
            print()
            print(product)

    def changeProd(self):
        print()
        print('상품 정보 수정을 선택하셨습니다.')
        print()
        num = int(input('수정할 상품번호를 입력하세요:'))
        proddata = self.manage.select(num)
        if proddata == None:
            print()
            print('상품 검색 결과 없음.')
        else:
            print()
            proddata.price = int(input('수정할 가격을 입력하세요: '))
            print()
            proddata.madein = input('수정할 원산지를 입력하세요: ')
            print()
            proddata.quantity = input('수정할 용량을 입력하세요: ')
            print()
            proddata.discount = int(input('수정할 할인율을 입력하세요: '))
            print()
            print('수정 완료!')

    def rmvProd(self):
        print()
        print('상품 삭제를 선택하셨습니다.')
        print()
        num = int(input('삭제할 제품번호를 입력하세요: '))
        proddata = self.manage.select(num)
        if proddata == None:
            print()
            print('제품 검색 결과 없음.')
        else:
            self.manage.remove(proddata)
            print()
            print('삭제 완료!')

    def printAll(self):
        data = self.manage.selectAll()
        for i in data:
            print(i)
            print()
            print('□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')

class Menu:
    def __init__(self):
        self.do = ProdDo()

    def Go(self):
        while True:
            print()
            print('□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
            print('■               □                ■               □               ■                       □                ■')
            print('□   1.등록   ■   2.검색   □   3.수정   ■   4.삭제   □   5.전체 출력   ■   0.종료    □')
            print('■               □                ■               □               ■                       □                ■')
            print('□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
            print()
            menu = int(input('원하는 메뉴를 선택해주세요: '))
            if menu == 1:
                self.do.addProd()
            if menu == 2:
                self.do.printProd()
            if menu == 3:
                self.do.changeProd()
            if menu == 4:
                self.do.rmvProd()
            if menu == 5:
                self.do.printAll()
            if menu == 0:
                print()
                print('종료합니다.')
                break

def main():
    proddata=Menu()
    proddata.Go()
main()
