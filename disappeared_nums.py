
nums = [4,3,2,2,3,1]

s = {x for x in range(1,len(nums)+1)}  #set() converts the list into [1,2,3,4] no duplicates left.
                                       #then we subtract set(nums) from s, which is numbers from 1 to len(nums)
s = s - set(nums)                      #and we are left with the numbers that are missing in nums

print(s)

# In the end its like [1,2,3,4,5,6] - [1,2,3,4] = [5,6] which is what we look for