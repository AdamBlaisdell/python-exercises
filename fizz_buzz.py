# Write a program that prints the numbers from 1 to 100 and for multiples of
# ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”.

def fizz_buzz(num):
    rules = {
        3: "fizz",
        5: "buzz",
    }

    for i in range(1, num + 1):
        output = ""
        for k, v in rules.items():
            if i % k == 0:
                output += v
        print(output or i)


if __name__ == '__main__':
    fizz_buzz(100)

