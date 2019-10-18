for i in range(1, 10):
    print(i, '단')
    for j in range(1, 10):
        print(i, ' * ', j, ' = ', i * j)
        j = j + 1
    print('\n')    
    i = i+1
