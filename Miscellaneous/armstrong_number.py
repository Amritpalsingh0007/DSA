class Solution:
    def __init__(self, num):
        self.num = num

    def no_of_digits(self):
        temp_num = self.num
        count = 0
        while temp_num > 0:
            count += 1
            temp_num = temp_num//10
        return count
    
    def power(self, digit, power):
        product = 1
        for _ in range(power):
            product *= digit
        return product


    def armstrong_sum(self, power):
        temp_num = self.num
        sum = 0
        while temp_num > 0:
            sum += self.power((temp_num % 10), power)
            temp_num = temp_num//10
        return sum
    
    def is_armstrong(self):
        if self.num == self.armstrong_sum(self.no_of_digits()):
            return True
        else:
            return False

print(Solution(int(input("Number : "))).is_armstrong())