string = input()

print(len(string))
print(string.lower())
sumVowel = 0
for i in ["a", "e", "i", "o", "u"]:
    sumVowel += string.count(i)
print(sumVowel)
print(string.replace("ugly", "beauty"))
print("The: " + str(string[:3]=="The") + ". end: " + str(string[len(string)-3:] == "end"))
# or string.startswith && string.endswith
