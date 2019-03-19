def    sum_array(array):
    '''
    Takes a list or a tuple as the input
    and returns the sum of the elements
    e.g sum_array([1,2,3,4,5]) == 15
    '''
    if len(array)== 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

def    fibonacci(n):
    '''
    Returns the nth value in the fibonacci
    sequence
    e.g fibonacci(5) == 120
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def    factorial(n):
    '''
    Returns the factorial value of an integer n
    e.g factorial(6) == 720
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n

def reverse(word):
    '''
    Returns reverse letters of a string
    e.g reverse('make') == 'ekam'
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
