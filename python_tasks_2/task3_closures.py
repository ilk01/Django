def make_multiplier(k):
    def multiply(x):
        return x * k

    return multiply


if __name__ == "__main__":
    by_2 = make_multiplier(2)
    by_5 = make_multiplier(5)

    print("7 * 2 =", by_2(7))
    print("7 * 5 =", by_5(7))
