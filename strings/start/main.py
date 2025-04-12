"""
String Algorithms

Write code to show basic string operations
"""

string = "Hello, World!"
print(string)
print(string[0])
print(string[2:5])
print(string[2:])

print(string.upper())
print(string.lower())
print(string.strip())
print(string.replace("H", "J"))
print(string.split(","))
print(len(string))
print("Hello" in string)
print("Bye" not in string)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "We have {:<8} chickens."
print(txt.format(49))

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "We have {:^8} chickens."
print(txt.format(49))

txt = "We have {:=8} chickens."
print(txt.format(49))

txt = "We have {:-8} chickens."
print(txt.format(49))

txt = "We have {:+} chickens."
print(txt.format(49))

txt = "We have {:-} chickens."
print(txt.format(49))

txt = "We have {:-8} chickens."
print(txt.format(49))

txt = "We have {:-8} chickens."
print(txt.format(-49))

txt = "We have {:,} chickens."
print(txt.format(49000))

txt = "We have {:b} chickens."
print(txt.format(49))

txt = "We have {:c} chickens."
print(txt.format(49))

txt = "We have {:d} chickens."
print(txt.format(49))

txt = "We have {:e} chickens."
print(txt.format(49))

txt = "We have {:E} chickens."
print(txt.format(49))

txt = "We have {:f} chickens."
print(txt.format(49))

txt = "We have {:F} chickens."
print(txt.format(49))
