def _(val):
    return val


def belobelo(func):
    def inner(*args, **kwargs):
        print('Belo Belo...')
        func(*args, **kwargs)
    return inner


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += str(arg)
    return result


def types(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += str(type(arg))
    return result

# unpacking_call.py


def my_sum(a, b, c):
    print(a + b + c)


@belobelo
def main(*args, **kwargs):
    is_suka = 'suka' in kwargs
    print('Hello!')
    print(args)
    print(kwargs)
    print('is suka: %s' % is_suka)
    print("concatenate: %s" % concatenate(**kwargs))
    print("types: %s" % types(**kwargs))


def others():
    my_list = [1, 2, 3]
    my_sum(*my_list)

    # extract_list_body.py
    my_list = [1, 2, 3, 4, 5, 6]

    a, *b, c = my_list

    print(a)
    print(b)
    print(c)

    # merging_lists.py
    my_first_list = [1, 2, 3]
    my_second_list = [4, 5, 6]
    my_merged_list = [*my_first_list, *my_second_list]

    print(my_merged_list)

    # merging_dicts.py
    my_first_dict = {"A": 1, "B": 2}
    my_second_dict = {"C": 3, "D": 4, "A": 0}
    my_merged_dict = {**my_first_dict, **my_second_dict}

    print(my_merged_dict)

    # string_to_list.py
    a = [*"RealPython"]
    print(a)

    # mysterious_statement.py
    *a, = "RealPython"
    print(a)

    d = {
        "name": "Jo",
        "Tel": 2121231221,
        "Address": "My Place"
    }
    print(" --- Val is: {x[a]} --- ".format(x={"a": 12, "test": "caccola"}))
    print("{name} ({Address})".format(**d))

    yeartoend = 5
    print(_("End in +%dy") % yeartoend)


main("test!", 11, 12, 13, suka=12, minkia='aaa', peppo={'a': 'xxx'})
others()
