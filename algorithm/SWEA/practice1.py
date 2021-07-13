def str_rev(str):
    # str -> list
    arr = list(str)
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    #swap
    # list -> str
    str = "".join(arr)
    return str
# ------------------
str = "algorithm"
str1 = str_rev(str)
print(str1)

s = "algorithm"
s = s[::-1]
print(s)