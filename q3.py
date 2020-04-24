
class PefectNumber(object):
    def __init__(self):
        self.max_no = 1000000
        self.special = []
        self.test()
        
    
    def check_pallindrom(self,string):
        return string == string[::-1]
    def even_digits(self,string):
        return len(string)%2 == 0
    def zero_one(self,string):
        temp = {'2':True,'1':True}
        for i in string:
            if i not in temp:
                return False
        return True

    def find_perfect_no(self,n):
        for i in range(1,self.max_no+1):
            no = str(i)
            if False in [self.check_pallindrom(no),self.even_digits(no),self.zero_one(no)]:
                continue
            self.special.append(i)
        return self.special[n-1]

    def test(self):
        if self.find_perfect_no(1)==11:
            print('passed testecase 1')
        if self.find_perfect_no(2)==22:
            print('passed testecase 2')

if __name__ == "__main__":
    PefectNumber()
