def add_numbers(start, end):
    """
    write the body of this
    function, similar to the block
    of code we just saw. Hint:
    don’t forget to use return
    """
    c = 0
    for number in range(start, end+1):
        c = c + number
    return c
 
test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)
