import math


class standar_Deviation:
    def __init__(self):
        print("init")

    def sd(self,val):
        sum = 0
        for i in val:
            sum += i
        length = len(val)
        mean = sum / length
        # print(sum)
        deviation = 0
        for i in val:
            deviation += abs(i - mean) ** 2
        sq = math.sqrt(deviation / length)
        return sq

    def entropy(self,val):
        countYes = 0
        countNo = 0
        for i in val:
            if (i == 'Yes'):
                countYes += 1
            else:
                countNo += 1
        
        totalCount = len(val)
        n = 2
        pYes = countYes / totalCount
        pNo = countNo / totalCount
        H = -(pYes * (math.log(pYes, 2)) + pNo * (math.log(pNo, 2)))
        return H

    def info_gain(self, val1, val2, best_entropy):
        total_instance = len(val1) + len(val2)
        information_gain = best_entropy - (((len(val1) / total_instance) * (self.entropy(val1))) + ((len(val2) / total_instance) * (self.entropy(val2))))
        return information_gain

sd=standar_Deviation()
best_entropy = sd.entropy(['Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes'])
print(best_entropy)
val1 = ['Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes']
val2 = ['Yes', 'Yes', 'Yes', 'No', 'No', 'No']


print(sd.info_gain(val1, val2, best_entropy))
    # print(sd([4, 9, 11, 12, 17, 5, 8, 12, 14]))

    # print(entropy(['Yes','Yes','Yes','No','No','Yes','Yes','Yes']))
