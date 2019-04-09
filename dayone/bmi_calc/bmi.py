class Bmi:

    def __init__(self,name,hei,wei):
        self.hei = hei
        self.wei = wei
        self.name = name

    def bmicheck(self):

        bmi = self.wei / (self.hei*self.hei) * 10000

        if bmi >= 40:
            res =  "고도비만"
        elif bmi >= 35:
            res =  "중등도비만"
        elif bmi >= 30:
            res =  "경도비만"
        elif bmi >= 25:
            res = "과체중"
        elif bmi >= 18.5:
            res = "정상"
        else:
            res = "저체중"

        print("{}님은 {}입니다{}".format(self.name
                                         ,res
                                           ,round(bmi,5)))


