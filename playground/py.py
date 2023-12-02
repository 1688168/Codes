import os
def fizzBuzz(n):

    for ii in range(1, n+1):
        if ii%3==0 and ii%5==0:
            print("FizzBuzz")
        elif ii%3==0:
            print("Fizz")
        elif ii%5==0:
            print("Buzz")
        else:
            print(ii)

if __name__ == '__main__':
    #n = int(input().strip())
    inputfile = os.path.join("inputfile.txt")
    ii=0
    with open(inputfile, 'r', encoding='utf-8') as f:
        for line in f:
            print("ii: ", ii, ": ", line)

        n=15
        fizzBuzz(n)