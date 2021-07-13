str = "123"
str2 = "12.3"

print(float(str2), type(float(str2)))

test = "1+2"
print(test)
print(repr(test))
print(eval(test))
print(eval(repr(test)))
print(eval(eval(repr(test))))