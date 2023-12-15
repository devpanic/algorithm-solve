import sys

result = []

def getDivs(num):
    ret_list = []
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            ret_list.append(i)
            if i**2 != num:
                ret_list.append(num // i)
    ret_list.sort()
    return ret_list

while True:
    try:
        a = int(sys.stdin.readline().rstrip())
        result = getDivs(a)
        if a * 2 == sum(result):
            print(a, "= ", end="")
            for i in range(len(result) - 2) :
                print(result[i], "+ ", end="")
            print(result[i + 1])
        else:
            print(a, "is NOT perfect.")
    except:
        break