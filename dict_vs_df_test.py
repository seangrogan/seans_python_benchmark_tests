#
# The following code tests the idea behind a 2d distance matrix loaded into
# python's dict and loaded into pandas.  The access difference is recorded
# using timeit.
#

import timeit

print(f"{'':*>60}")
print(f"*{'Testing access difference between Dicts and DFs':^58}*")
print(f"{'':*>60}")

n = 10_000

setup = f'''
import pandas, numpy, timeit, random
n={n}

df = pandas.DataFrame(numpy.zeros(shape=[n, n]))
dict_2d = df.to_dict()
random.seed(12345)
n -= 1
i, j = random.randint(0, n), random.randint(0, n)
'''
tests_random = [
    "value = dict_2d[random.randint(0, n)][random.randint(0, n)]",
    "value = df.loc[random.randint(0, n), random.randint(0, n)]",
    "value = df.at[random.randint(0, n), random.randint(0, n)]",
    "value = df.iloc[random.randint(0, n), random.randint(0, n)]",
    "value = df.iat[random.randint(0, n), random.randint(0, n)]"
]
tests_fixed = [
    "value = dict_2d[i][j]",
    "value = df.loc[i,j]",
    "value = df.at[i,j]",
    "value = df.iloc[i,j]",
    "value = df.iat[i,j]"
]
test_names = ['2D dict', '.loc', '.at', '.iloc', '.iat']
print("Now Testing Random Calls")
for test, name in zip(tests_random, test_names):
    print(f"{name:>8} | {timeit.timeit(stmt=test, setup=setup):>8.4f} s")

print()
print("Now Testing Fixed Calls")
for test, name in zip(tests_fixed, test_names):
    print(f"{name:>8} | {timeit.timeit(stmt=test, setup=setup):>8.4f} s")

# Lenovo Laptop
# --------------------
# 2D dict |  38.9733 s
#    .loc |  11.8610 s
#     .at |   9.8257 s
#   .iloc |  13.9015 s
#    .iat |  10.4174 s
# --------------------
# Desktop Work
# --------------------
# 2D dict |   5.6250 s
#    .loc |  22.4196 s
#     .at |  15.6386 s
#   .iloc |  22.1832 s
#    .iat |  15.4502 s
# --------------------
