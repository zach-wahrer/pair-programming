def what_will_i_return():
    number = [0]

    def _what_will_i_do(i):
        number[0] += i
        if i < 5:
            _what_will_i_do(i + 1)
    _what_will_i_do(0)
    return number


print(what_will_i_return())


def what_will_i_return():
    number = [0]

    def _what_will_i_do(i):
        number[0] += i
        if i < 5:
            _what_will_i_do(i + 1)
    return _what_will_i_do(0)


print(what_will_i_return())
