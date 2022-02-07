


class A:

    '''1.set up class method''' #Begining of every class

    '''2.set up method''' #--> runs before every test case

    '''3.test 01'''

    '''4.test 02'''

    '''5.test 03'''

    '''6.test 04'''

    '''7.tear down method''' #--> runs after every test case

    '''8.tear down class method'''#End of every class


'''order of execution from class:
1-->2-->3-->7-->2-->4-->7-->2-->5-->7-->2-->6-->7-->8
'''