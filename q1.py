

class CandyDistribution(object):
    def __init__(self):
        self.test()

    def candy_distibution(self,candidates):
        candies = []
        candies.append(1)
        for current in range(1,len(candidates)):
            if candidates[current] > candidates[current-1]:
                candy = candies[current-1] + 1
                candies.append(candy)
            else:
                candies.append(1)
                temp = current
                while candies[temp] == candies[temp-1]:
                    candies[temp-1] += 1
                    temp -= 1
        return candies


    def test(self):
        candidates = [1,5,2,1]
        output = [1,3,2,1]
        result =  self.candy_distibution(candidates)
        if result==output:
            print('passed testcase 1')
        candidates = [2,1,3,7,4,9,5,8,6,3]
        output = [2,1,2,3,1,2,1,3,2,1]
        result =  self.candy_distibution(candidates)
        if result==output:
            print('passed testcase 2')


if __name__ == "__main__":
    obj = CandyDistribution()