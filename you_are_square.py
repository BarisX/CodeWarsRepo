#7 kyu
#You're a square!
import itertools
def is_square(n):
    for i in itertools.count(start=0):
        if i*i == n : return True
        if i < 0 or i >= n/2: return False
