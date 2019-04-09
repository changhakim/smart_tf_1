class Contact:

    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):

        print("{}님의 정보{}{}{}가 저장되었습니다".format(self.name
                                                ,self.phone
                                                ,self.email
                                                ,self.address))

    @staticmethod
    def set_contact():
        contact = Contact(input("이름을 입력하세요")
                          , input("번호을 입력하세요")
                          , input("이메일을 입력하세요")
                          , input("주소을 입력하세요"))
        return contact

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def print_menu():
        print("1 연락처 입력")
        print("2 연락처 출력")
        print("3 연락처 삭제")
        print("4 종료")
        menu = input("메뉴 선택:")
        return int(menu)

    @staticmethod
    def del_contact(ls,name):
        for i, t in enumerate(ls):
            if t.name == name:
                del ls[i]

    @staticmethod
    def run():
        ls=[]
        while 1:
            menu = Contact.print_menu()
            if menu == 1:
                t = Contact.set_contact()
                ls.append(t)
            elif menu == 2:
                Contact.get_contact(ls)
            elif menu == 3:
                name = input("삭제할 이름")
                Contact.del_contact(ls,name)
            elif menu == 4:
                break