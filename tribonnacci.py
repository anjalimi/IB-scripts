def tribonacci(n):
    dict1 = {}
    if n==0:
        dict1.update({0:0})
        return dict1[0]
    if n==1:
        dict1.update({1:1})
        return dict1[1]
    if n==2:
        dict1.update({2:1})
        return dict1[2]
    if n in list(dict1.keys()):
        return dict1[n]
    
    trib = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    
    return trib


n = 25
print tribonacci(n)