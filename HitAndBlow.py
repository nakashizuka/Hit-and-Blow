class HitAndBlow():                                   #eat,bite判定
    def __init__(self, num1, num2):                #2値を引数として受け取る
        self.num1 = num1                            
        self.num2 = num2
        
    def judge(self):
        eat = 0
        bite = 0
        for i in range(3):
            if self.num1[i] == self.num2[i]:        #eat判定
                eat += 1
            elif self.num1[i] in self.num2:         #bite判定
                bite += 1
            else:
                pass
        
        return eat, bite                            #eat,biteを返す    