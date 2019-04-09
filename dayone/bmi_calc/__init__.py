from bmi_calc.bmi import Bmi

def main():
    bmi = Bmi(input("이름를 입력하세요")
              ,int(input("키를 입력하세요"))
              ,int(input("몸무게를입력하세요")))

    bmi.bmicheck()


if __name__ == '__main__':
    main()