# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    current = numpy.zeros(n,int)
    # Your code here
    for i in range(n):
      height=0
      num=i
      while num != -1:
        if current[num]==0:
          height = height+1
        else:
          height = height+current[i]
          pass
        num = int(parents[num])
      current[i]=height

    for i in range(n):
      if current[i] > max_height:
        max_height = current[i]
        
    return max_height


def main():
    # implement input form keyboard and from files
    tips = input()
    if tips[0] == "I":
      n = int(input())
      numbers = input()
      parents = list(map(int, numbers.split()))
      print(compute_height(n, parents))
      
    elif tips[0] == "F":
      file = input()
      f = open("./test/" + file, "r")
      n = int(f.readline())
      parents = list(map(int, f.readline().split()))
      print(compute_height(n, parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
