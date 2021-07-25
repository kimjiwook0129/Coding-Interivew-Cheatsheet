import sys
import timeit

# rstrip() function has to called as well since readline()
# gets the next line char as an input as well.

start = timeit.timeit()
data = sys.stdin.readline().rstrip()
print(data)
end = timeit.timeit()
print(f'Time taken for \'sys.stdin.readline()\' to read : {end - start}s')

start = timeit.timeit()
data = input()
print(data)
end = timeit.timeit()

print(f'Time taken for \'input()\' to read : {end - start}s.')
