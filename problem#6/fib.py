'''
Name: Nathan Carr
Time: Thursday @ 2pm
'''
def fibonacci(n):

    if n < 0:
        return -1
    else:
        x = 0
        y = 1
        z = 0
        for a in range(n):
            z = x
            x = x + y
            y = z
        return x


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')