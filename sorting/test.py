import random
import time
import argparse

from insertion_sort import insertion_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from counting_sort import counting_sort_1, counting_sort_2
from radix_sort import radix_sort, counting_sort_for_radix

parser = argparse.ArgumentParser(description='Test implementations for sorting algorithms.')
parser.add_argument('-t', '--type', required=True, help='Type of test (speed or correctness).')

args = vars(parser.parse_args())

def test_speed(method, test_size=100, num_cases=10, case_type='worst', random_state=None):
    if method == insertion_sort:
        name = 'Insertion sort'
    elif method == merge_sort:
        name = 'Merge sort'
    elif method == heap_sort:
        name = 'Heap sort'
    elif method == counting_sort_1:
        name = 'Counting sort 1'
    elif method == counting_sort_2:
        name = 'Counting sort 2'
    elif method == radix_sort:
        name = 'Radix sort'
        
    if case_type == 'average':
        if random_state:
            random.seed(random_state)

    start_time = time.time()
    for n in range(num_cases):
        if case_type == 'best':
            A = list(range(test_size))
        elif case_type == 'worst':
            A = list(reversed(range(test_size)))
        elif case_type =='average':
            A = random.sample(range(test_size), test_size)
        method(A)
    end_time = time.time()
    print('* {}:\n  No. of cases = {}, Total time: {:.5f}s'.format(name, num_cases, end_time-start_time))

def test_correctness(method, test_size=100, num_cases=10, random_state=None):
    if method == insertion_sort:
        name = 'Insertion sort'
    elif method == merge_sort:
        name = 'Merge sort'
    elif method == heap_sort:
        name = 'Heap sort'
    elif method == counting_sort_1:
        name = 'Counting sort 1'
    elif method == counting_sort_2:
        name = 'Counting sort 2'
    elif method == radix_sort:
        name = 'Radix sort'

    if random_state:
        random.seed(random_state)

    for n in range(num_cases):
        A = random.sample(range(test_size), test_size)
        A_sorted_1 = method(A)
        A_sorted_2 = sorted(A)
        if A_sorted_1 != A_sorted_2:
            print("* {} implementation: Incorrect!".format(name))
            return
    print("* {} implementation: Correct!".format(name))

# best case
def best_case_test(test_size, num_cases):
    print('Best-case testing...')
    test_speed(insertion_sort, test_size, num_cases, 'best')
    test_speed(merge_sort, test_size, num_cases, 'best')
    test_speed(heap_sort, test_size, num_cases, 'best')
    test_speed(counting_sort_1, test_size, num_cases, 'best')
    test_speed(counting_sort_2, test_size, num_cases, 'best')
    test_speed(radix_sort, test_size, num_cases, 'best')

# average case
def avg_case_test(test_size, num_cases, random_state):
    print('Average-case testing...')
    test_speed(insertion_sort, test_size, num_cases, 'average', random_state)
    test_speed(merge_sort, test_size, num_cases, 'average', random_state)
    test_speed(heap_sort, test_size, num_cases, 'average', random_state)
    test_speed(counting_sort_1, test_size, num_cases, 'average', random_state)
    test_speed(counting_sort_2, test_size, num_cases, 'average', random_state)
    test_speed(radix_sort, test_size, num_cases, 'average', random_state)

# worst case
def worst_case_test(test_size, num_cases):
    print('Worst-case testing...')
    test_speed(insertion_sort, test_size, num_cases, 'worst')
    test_speed(merge_sort, test_size, num_cases, 'worst')
    test_speed(heap_sort, test_size, num_cases, 'worst')
    test_speed(counting_sort_1, test_size, num_cases, 'worst')
    test_speed(counting_sort_2, test_size, num_cases, 'worst')
    test_speed(radix_sort, test_size, num_cases, 'worst')

# test for correctness
def test_correctness_all(test_size, num_cases, random_state):
    test_correctness(heap_sort, test_size, num_cases, random_state)
    test_correctness(merge_sort, test_size, num_cases, random_state)
    test_correctness(insertion_sort, test_size, num_cases, random_state)
    test_correctness(counting_sort_1, test_size, num_cases, random_state)
    test_correctness(counting_sort_2, test_size, num_cases, random_state)
    test_correctness(radix_sort, test_size, num_cases, random_state)

if __name__ == '__main__':
    test_type = args['type']
    if test_type == 'speed':
        case_type = int(input("- Type of test case (1=Best, 2=Average, 3=Worst, 4=All):  "))
        if 1 <= case_type <= 4:
            test_size = int(input('- Test size: '))
            num_cases = int(input('- Number of cases: '))
            if case_type == 2 or case_type == 4:
                try:
                    random_state = int(input('- Random seed: '))
                except ValueError:
                    random_state = None
            if case_type == 1:
                best_case_test(test_size, num_cases)
            elif case_type == 2:
                avg_case_test(test_size, num_cases, random_state)
            elif case_type == 3:
                worst_case_test(test_size, num_cases)
            else:
                best_case_test(test_size, num_cases)
                print()
                avg_case_test(test_size, num_cases, random_state)
                print()
                worst_case_test(test_size, num_cases)
        else:
            print('Test type out of range')
    elif test_type == 'correctness':
        test_size = int(input('- Test size: '))
        num_cases = int(input('- Number of cases: '))
        random_state = int(input('- Random seed: '))
        test_correctness_all(test_size, num_cases, random_state)
    else:
        print('Test type undefined!')