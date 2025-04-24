'''
What is the product and business

Observation process is not lossless

Is there more data or information to use?

What is the maximum size of the array


Tests
ex1
ex2
empty list
list with all zeros
list with repeating zeros [ 1, 2, 3, 0, 0, 3, 2, 1]
list with negative values [ -1, 0, 2]


'''
import sys

def reorder(int_order)->None:
    index = 0
    while index < len(int_order):
        if int_order[index] == 0:
            int_order.insert(index+1, 0)
            int_order.pop()
            index +=1
        index +=1


def ex1_test():
    inv = [4,0,1,3,0,2,5,0]
    reorder(inv)
    assert inv == [4,0,0,1,3,0,0,2]
def ex2_test():
    inv = [3, 2, 1]
    reorder(inv)
    assert inv == [3,2,1]
def empty_list_test():
    inv = []
    reorder(inv)
    assert inv == []
def all_zeros_test():
    inv = [0,0,0]
    reorder(inv)
    assert inv == [0,0,0]
def repeating_zeros_test():
    initial = [1,2,3,0,0,2,5,1]
    inv = [1,2,3,0,0,2,5,1]
    reorder(inv)
    print("before processing:"+str(initial))
    print("after processing:"+str(inv))
    assert inv == [1,2,3,0,0,0,0,2], f"inventory was {initial} and is now {inv}"
def negative_test():
    inv = [-1, 0, 2, 2]
    reorder(inv)
    assert inv == [-1, 0, 0, 2]

def test_runner(test_list):
    for test in test_list:
        try:
            test()
            print(f"{test.__name__} passed")
        except AssertionError as e:
            print(f"{test.__name__} failed")


def main():
    tests = [ex1_test, ex2_test, empty_list_test, all_zeros_test, repeating_zeros_test, negative_test]

    test_runner(tests)

if __name__ == "__main__":
    sys.exit(main())