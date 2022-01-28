def is_prime_number(num)
    # Program to check if a number is prime or not
    # From: https://www.programiz.com/python-programming/examples/prime-number

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


if __name__ == '__main__':
    is_prime_number(42)