# https://www.techiedelight.com/add-padding-string-python/#:~:text=The%20standard%20way%20to%20add,of%20ASCII%20space%20is%20used.

# The standard way to add padding
# if no padding is specified, the default padding of ASCII space is used


def useRjust(string, len, padding):
    return string.rjust(len, padding)


# Padding paramter not supported, always filles with digit 0


def useZfill(string, len):
    return string.zfill(len)

# General string formatting


def strFormat(string, len, padding):
    # '{:padding>len}'.format(string)
    return ('{:' + padding + '>' + str(len) + '}').format(string)

# Available on Python 3.6 or higher


def f_strings(string, len, padding):
    return f'{string:{padding}>{len}}'


if __name__ == "__main__":
    my_string = 'Jiwook Kim'
    padding = 'X'
    len = 20
    print("##### Using str.rjust() #####")
    print(useRjust(my_string, len, padding))
    print("##### Using str.zfill() #####")
    print(my_string.zfill(len))
    print("##### Using str.format() #####")
    print(strFormat(my_string, len, padding))
    print("##### Using f-strings #####")
    print(f_strings(my_string, len, padding))
