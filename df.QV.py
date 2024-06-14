import pandas as pd


numbers = list(range(1, 11))

sqr_nums = [x**2 for x in numbers]

df = pd.DataFrame({'Votes': numbers, 'Quadratic Vote Cost': sqr_nums})
print(df)

from tabulate import tabulate

markdown_table = tabulate(df, headers='keys', tablefmt='pipe')
print(markdown_table)