import os
from datetime import datetime

import dotenv
import requests


dotenv.load_dotenv()

day = datetime.today().day
result = requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies={'session': os.environ['SESSION_TOKEN']})

for l in result.text.split('\n')[:5]:
    print(l)
print('...')

with open(f'inputs/{day:02d}', 'w') as f:
    f.write(result.text[:-1])

with open(f'solutions/{day:02d}.py', 'w') as f:
    f.write(
f'''with open('inputs/{day:02d}') as f:
    l = []


def part_1(l):
    pass


def part_2(l):
    pass

part_1(l)
part_2(l)
'''
    )
