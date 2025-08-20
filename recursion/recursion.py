def add_one(num):
    if (num >= 9):
        return 0
    total = num+1
    print(total)

    return add_one(total)


result = add_one(0)
print("Final result:", result)
