def list_sum(lst):
    '''This function takes list as input and returns the sum of elements of the list'''
    return sum(lst)

def list_max(lst):
    '''This function takes list as input and returns the element having maximum value in the list'''
    return max(lst)

def list_reverse(lst):
    '''This function takes list as input and returns the list with reverse elements'''
    lst = lst[::-1]
    return lst

def list_sort(lst):
    '''This fun ction takes list as input and sort the elements of list'''
    for i in range(len(lst)):
        for j in range(i+1, (len(lst))):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def list_mean_mode(lst):
    '''This finction takes list as input and returns the mean and mode of elements of the list'''
    import statistics as st
    mean_val = st.mean(lst)
    mode_val = st.mode(lst)
    return "Mean: {} and Mode: {}".format(round(mean_val, 3), mode_val)

def k_sum():
    '''This function takes a sequence of number seperated by space from user and also takes number of sums to be returned
     along with strat and end corresponding to each k. Then, returns the k sum in form of list.'''
    num_sequence = input('Enter a sequence of numbers seperated by a space: ').split()
    num_sequence = [int(x) for x in num_sequence]
    k = int(input('Enter an inetger k which can be used to return k sized list: '))
    dictionary = {}
    for i in range(k):
        start, end = input('Enter start and end numbers seperated by space: ').split()
        start, end = int(start), int(end)
        if end <= len(num_sequence) and start <= (len(num_sequence) - 1):
            dictionary[i] = [int(start) - 1, int(end) - 1]
        else:
            print('You have entered start or end larger than length of list')
            break
        
    list_k_sum = []
    if k < len(num_sequence):
        for x in dictionary:
            sum_1 = sum(num_sequence[dictionary[x][0]:dictionary[x][1]+1])
            list_k_sum.append(sum_1)
    else:
        print('You have entered value of k larger than total numbers in sequence: ')

    if len(list_k_sum) == k:
        return list_k_sum



