def count_to(count):
    '''Our iterator implementation'''
    #Our list
    number_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    #Our built-in iterator
    #creates a tuple such as (a, 'eins')
    iterator = zip(range(count), number_in_german)


    #Iterate through our iterator list
    #Extract the German numbers
    #Put them in a generator called number
    for position, number in iterator:
        #Return a 'generator' containing numbers in German
        yield number

# Test the generator returned by our iterator
for num in count_to(4):
    print('{}'.format(num))
