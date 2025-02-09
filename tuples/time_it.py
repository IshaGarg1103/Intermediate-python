#how timeit works

import timeit
time_taken=timeit.timeit(stmt='[1,2,3]',number=100000)
print(time_taken)
#timeit.timeit() returns the total time taken to execute the given code for the given amount of times.
#difference between the usecase of stmt and setup
#stmt - returns the time taken to run for specific amount of times
#setup - used as the prerequisite to setup the environemnt for thespeciifc code to run in
#        such as module import or value initialisation

setup = 'import math'  # Runs once
stmt = 'math.sqrt(16)'  # Runs repeatedly

time_taken = timeit.timeit(stmt=stmt, setup=setup, number=100000)
print(f"Time taken: {time_taken} seconds")
