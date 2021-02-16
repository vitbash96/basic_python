import argparse

parser = argparse.ArgumentParser(description="Pay calculation")
parser.add_argument(
    'hours', metavar='--hours', type=float, help='Number of hours worked'
)
parser.add_argument(
    'wage', metavar='--wage', type=float, help='Hourly rate'
)
parser.add_argument(
    '-bonus', metavar='--bonus', type=float, help='Bonus amount, if any', default=0
)
args = parser.parse_args()
print(
    f' The salary is {args.hours} hours * ${args.wage} per hour + ${args.bonus} bonus = {args.hours * args.wage + args.bonus}')
