for i in range(0,6):
    for j in range(1, 6 - i):
        print(" ", end=' ')
    for k in range(0, i + 1):
        print("*", end= ' ')
    print()


    # 1,5
    # 2,4  2,5
    # 3,3 3,4 3,5

    # for i in range(5):
    #     for j in range(1, 5 - i):
    #         print(" ", end="")
    #     for k in range(0, i + 1):
    #         print("*", end="")
    #     print()

