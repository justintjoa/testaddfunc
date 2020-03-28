from numpy import inf
import numpy as np

class Solution(object):
    def sumSubarrayMins(self, A):
        stack = []
        length = len(A)
        sum = 0
        runningsum = 0 
        for i in range(length):
            sum = sum + A[i]
            if (len(stack) == 0):
                stack.append([A[i],1])
                runningsum = runningsum + A[i]
            else:
                if (stack[-1][0] > A[i]):
                    count = 0
                    loss = 0 
                    while (stack and (stack[-1][0] >= A[i])):
                        l,m = stack.pop()
                        count = count + m
                        loss = loss + l*m 
                    runningsum = runningsum - loss + A[i]*(count)
                    stack.append([A[i],count])
                #add up stack
                sum = sum + runningsum
                if (A[i] == stack[-1][0]):
                    stack[-1][1] = stack[-1][1] + 1
                else:
                    stack.append([A[i],1])
                runningsum = runningsum + stack[-1][0]
        print(stack)
        Mod = 10**9 + 7 
        return (sum % Mod)
                #add new solution part to stack
     




