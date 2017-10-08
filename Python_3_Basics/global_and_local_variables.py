x = 6

def example():
    global_x = x
    print(global_x)
    global_x += 5
    print(global_x)

    return global_x


x = example()
print(x)
