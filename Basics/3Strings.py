
# Strings
Sent1 = "Hi everyone !"
sent2 = 'How you guys are doing'
sent3 = "Time is 10.30 So everyone go to sleep ..."

print(Sent1)
print(sent2)
print(sent3)
Lengthy_sent = """This is to check 
How Paragraph strings are working in 
    Python"""

print(Lengthy_sent)

# Strings in python consider as an Array

Word = "Manirathnam"
print(Word[2], Word[6])
a = Word[3:7]
# slicing
print(a)
Word2 = "Hello Python"
print(Word2[-5:-1])
print(Word2[-10:-3])

FirstName = "Naveen"
LastName = " Kumar"
print(FirstName + LastName)  # Concat

# Length
print(len(Lengthy_sent))
print(len(Word2))
print(len(Word))

# Methods strip, upper, lower, replace, split , in

StrOne = "   This is to check strip method   "
print(StrOne.strip())

LowerCase = "abcd"
UpperCase = "XYZ"
print(LowerCase.upper())
print(UpperCase.lower())

ToBeReplace = "Good Morn"
print(ToBeReplace.replace("rn", "rning"))
print(ToBeReplace.replace("rn", "rning Bro !"))

ToBeSplit = 'RajeshKumar'
print(ToBeSplit.split('h'))
print(ToBeSplit.split('esh'))

print("check" in Lengthy_sent)
print("Morn" in ToBeReplace)
print("Morning" in ToBeReplace)


