#
# This program is going to test the size of the distance matrix and the access time
#
import timeit
from collections import defaultdict

def setup_information():
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
    return setup, tests_random, tests_fixed, test_names


print(f"{'':*>60}")
print(f"*{'Testing access difference between Dicts and DFs':^58}*")
print(f"*{'As a function of matrix size':^58}*")
print(f"{'':*>60}")

n_cities = [int(pow(10, y / 2)) for y in range(1, 12)]
number, repeat = 1_000_000, 5

test_results_random = defaultdict(dict)
test_results_fixed = defaultdict(dict)
setup, tests_random, tests_fixed, test_names = setup_information()
for n in n_cities:
    print(f"n_cities = {n}")
    print("Now Testing Random Calls")
    for test, name in zip(tests_random, test_names):
        val = timeit.Timer(stmt=test, setup=setup).repeat(repeat=repeat, number=number)
        print(f"{name:>8} | {min(val):>8.4f} s")
        test_results_random[name][n] = val

    print()
    print("Now Testing Fixed Calls")
    for test, name in zip(tests_fixed, test_names):
        val = timeit.Timer(stmt=test, setup=setup).repeat(repeat=repeat, number=number)
        print(f"{name:>8} | {min(val):>8.4f} s")
        test_results_fixed[name][n] = val


