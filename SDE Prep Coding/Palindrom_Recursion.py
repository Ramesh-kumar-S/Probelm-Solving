def generator(num):
    for i in range(num):
        yield i

# print(next(generator(5)))
# print("Hey Ramesh - SDE (Google)")
def reverse(str):
    print(str)
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]
    
print(reverse("ramesh"))

def factorial(num):
    #Looping Method
    # factorial=1
    # if num < 0:
    #     return factorial
    # else:
    #     for i in range(1,num+1):
    #         factorial=factorial*i
    # return factorial

    #Recursive Approach
    if num == 1:
        # print("returning 1")
        return 1
    else:
        # print(num)
        return num * factorial(num-1)
    
# print(factorial(10))

def isPalindrom(str):
    start = 0
    end= len(str)-1
    mid=len(str)//2

    for x in range(mid):
        if str[x] != str[end-x]:
            return "No"
    return "Yes"
        


# print(isPalindrom("racecar"))




