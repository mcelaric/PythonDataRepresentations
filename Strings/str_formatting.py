"""
String formatting code examples
"""
from openpyxl.styles.builtins import output

country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)

"""
In order to provide more control of the formatted output, you can also provide a number 
that indicates which argument should be used. 
This allows you to repeat arguments or use them out of order:
"""
mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

"""
You can also give a format specification for a replacement field. 
The format specification is preceeded by a colon and must come after the argument index 
(if there is one) in the replacement field. 
The format specification indicates how to format the individual field. 
It can be used to align strings (or numbers):

n the format strings on lines 6 and 7, you can see that after the argument index 
in each replacement field there is a colon. 
The format specifiers after the colon include a number. This number is the width of the field in the output. 
The output will contain exactly that many characters for that field (padded with spaces), 
regardless of how wide the argument is. 
In this example the width is preceded by a symbol which indicates how the field should be aligned: 
    < for left aligned 
    > for right aligned
    ^ for centered
"""
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

"""
Formatting numeric output
"""
num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)