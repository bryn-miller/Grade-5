def lots_of_numbers(max):
    for x in range(0, max):
            print(x)

lots_of_numbers(1000)
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
             print(x)
    t2 = time.time()
    print('it took %s seconds' % (t1-t2))

lots_of_numbers(1000)

