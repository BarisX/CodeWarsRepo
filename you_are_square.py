#7 kyu
#You're a square!
def is_square(n):
    return True if n >= 0 and (n**0.5)%1 == 0 else False
