def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            for i in range(2, res):
                if 0 == res % i:
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
