import re
#1
txt = "kslsflabsklf"
x = re.search(r"ab*", txt)
print(x.group())

#2
x2 = re.search(r"abb{2,3}", txt)
if x2:
    print("Match found:", x2.group())
else:
    print("No match.")

#3
txt = "hello_world"
x3 = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x3)

#4
txt = "She is KBTU Student"
x4 = re.findall(r"\b[A-Z][a-z]+\b", txt)
print(x4)

#5
txt = "xxxxxxxaXYZ123b"
x5 = re.findall(r"a.*b$", txt)
print(x5)

#6
txt = "Hello, world. How are you today?"
x6 = re.sub(r"[ ,.]", ":", txt)
print(x6)

#7
txt = "random_string_example"
x7 = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), txt)
print(x7)

#8
txt = "HelloWorldPythonIsFun"
x8 = re.split(r'(?=[A-Z])', txt)
print(x8)

#9
txt = "HelloWorldPythonIsFun"
x9 = re.sub(r'(?<!^)([A-Z])', r' \1', txt)
print(x9)

#10
txt = "randomStringExample"
x10 = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()
print(x10)