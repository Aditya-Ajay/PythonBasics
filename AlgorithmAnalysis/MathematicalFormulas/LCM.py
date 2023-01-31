def lcm(a, b):
    res = max(a, b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1


'''
THIS IS A NAIVE APPROACH AND TAKES MORE TIME TO EXECUTE 
AND HAS A 0(n) . To be precise it will be 

theta(a*b - max(a, b)) ==>  this much time the function takes to execute
'''
# print(lcm(15, 12))
