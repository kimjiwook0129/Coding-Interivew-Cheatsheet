

if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    # Retur
    # Basic Sort functions

    # Returns a newly sorted array, leaves the original
    new_array = sorted(array, key=lambda x: x, reverse=False)
    array.sort(key=lambda x: x, reverse=False)

    array = [[1, 2, 3], [9, 0, 3], [1, 6, 2], [4, 8, -1]]
    # Sorting multi-field array
    # array.sort() # This will automatically sorts in the field order
    # To Customize:
    array.sort(key=lambda x: (-x[0], x[1], -x[2]))
    # - if Descending Order
    print(array)
