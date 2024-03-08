import difflib

text1 = “welcome to computer science"
text2 = "welcome to computer network"
text3 = “design engineering"
sequence = difflib.SequenceMatcher(isjunk=None, a=text1,
b=text2)
difference = sequence.ratio()*100
difference = round(difference,1)
print(str(difference) + "% match")