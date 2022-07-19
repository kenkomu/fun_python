class sum:
    @staticmethod
    def getSum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
def main():
    print("Sum is:",sum.getSum(1,2,3,4,5))
main()