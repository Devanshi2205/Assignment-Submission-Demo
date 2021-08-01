def it_remove(t1, item):
    res = [i for i in t1 if i != items]
    return res
if __name__ == "__main__":
    t1 = [int(i) for i in input("enter values: ").split()]
    items = int(input("Enter the items"))
    print("The original list is : " + str(t1))
    res = it_remove(t1, items)
    print("The list after performing the remove operation is : " + str(res))