from functools import reduce

print(f'The product of numbers from 100 to 1000 is equal to: {reduce(lambda x, y: x * y, range(100, 1001, 2))}')

