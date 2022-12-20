import random


class Cpu():                                                #対戦CPU
    def __init__(self, num):
        self.cpuSelectNumber = num

    def ablenum(self, s, eat, bite):                        #候補の数
        if eat == 0 and bite == 0:                          #候補の数を減らす(もしもeat=0,bite=0だったら)
            a = []
            for i in s:
                if i not in self.cpuSelectNumber:
                   a.append(i)
        else:                                               #候補の数字を減らさない
            a = s
        return a

    def selectnum(self, s):                                 #CPUが相手の数字を当てる
        return random.sample(list(s), 3)

    s = [i for i in "0123456789"]                           #候補の数字の初期配列