import random

from Cpu import Cpu
from HitAndBlow import HitAndBlow

randomNumber = random.sample(Cpu.s, 3)
cpu = Cpu(randomNumber)
CPU_ANSWER = random.sample(Cpu.s, 3)            #CPUの答えを変数に入れる
print("あなたの答え：",end="")
YOUR_ANSWER = list(input())                     #自分の答えを変数に入れる
print()
i = 0
j = 1
k = 1
while True:
    if i % 2 == 0:
        print(j,"回目表")
        j += 1
        print("あなたのターン")
        yourSelectNumber = list(input())        #CPUの数字を当てる
        Nu1 = HitAndBlow(CPU_ANSWER, yourSelectNumber)
        print("CPUの答え:", CPU_ANSWER, "あなたの選んだ数字:", yourSelectNumber)
        yourEat, yourBite = Nu1.judge()          #eat,bite判定
        print("youreat:", yourEat, "yourbite:", yourBite)
        if yourEat == 3:
            print("clear!")
            break
    else:
        print(k,"回目裏")
        k += 1
        print("CPUのターン")
        cpu.cpuSelectNumber = cpu.selectnum(cpu.s)         #あなたの数字を当てる
        print("CPUが選択可能な数字:", cpu.s)
        Nu2 = HitAndBlow(YOUR_ANSWER, cpu.cpuSelectNumber)
        print("あなたの答え:", YOUR_ANSWER, "CPUの選んだ数字:", cpu.cpuSelectNumber)
        cpuEat,cpuBite = Nu2.judge()          #eat,bite判定
        print("cpueat:", cpuEat, "cpubite:", cpuBite)
        cpu.s = cpu.ablenum(cpu.s, cpuEat, cpuBite)        #候補の数の増減判定
        if cpuEat == 3:
            print("defeat!")
            break
    i += 1