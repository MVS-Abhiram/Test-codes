
"""
-------------------
PROBLEM STARTEMENT
-------------------
Given 2 integers n and k find all the possible combinations of k numbers out of 1 to n. 
Display the result in sorted order of list

----------------
--Sample Input--
----------------
4
2

------------------
-- Sample Output--
------------------
1 2
1 3
1 4
2 3
2 4
"""

# Python3 program to print all combinations of size
# k of elements in set 1..n
def check1(n, left, k):
    # Pushing this vector to a vector of vector
    if (k == 0):
        ans.append(tmp)
        d=""
        for i in range(len(tmp)):
            d+=str(tmp[i])+" "
        print(d.strip())
        # Using strip function to remove spaces in the end
        return
    # i iterates from left to n. First time
    # left will be 1
    for i in range(left, n + 1):
        tmp.append(i)
        check1(n, i + 1, k - 1)
        tmp.pop()
n =int(input())
k =int(input())
ans=[]
tmp=[]
ans =check1(n,1,k)
