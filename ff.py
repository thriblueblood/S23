##def sortedL(lst):
##    if len(lst ) <= 1:
##        return True
##    if lst[0] < lst[1]:
##        return sortedL(lst[1:])
##    else:
##        return False
##

##def remove_duplicates(lst):
##    result = []
##    for x in lst:
##        if x not in result:
##            result.append(x)
##    return result
##lst = [1,2,2,1,3,4,5]
##
##a = remove_duplicates(lst)

##def remove_duplicates(x):
##    z = [x[0]]
##    for i in range(1,len(x)):
##        for y in range(0, i):
##            if x[i] == x[y]:
##                break
##        else:
##            z.append(x[i])
##    return z
##x = [1,2,3,2,4]
##
##a = remove_duplicates(x)

##def remdup(l, dup=None):
## # If has zero or one elements, there are no duplicates.
## if len(l) < 2:
##  return l
## if dup is not None:
##  try:
##   l.remove(dup)
##   remdup(l, dup)
##  except ValueError:
##   pass
## return [l[0]] + remdup(l[1:], l[0])
##x = [1,2,3,2,4]
##a = remdup(x)
##print(a)       

def isCircular(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return arr1 in arr2 + ' ' + arr2
        
arr1 = "abc"
arr2 = "bac"
isCircular(arr1,arr2)
