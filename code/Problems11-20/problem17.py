#Devin Riley
#Project Euler
#Problem 17
#12/30/2013

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


#1-9: 36
#10-19: 70
# 1-99: 8*36 + 10(6 + 6 + 5 + 5 + 7 + 6 + 6)  i.e. 10("twenty" + "thirty" + ... + "ninety")
#       = 854
#1-9 100 each => 36*100
#1-99 0 times => 854(9)
#"hundred" 9 times => 9(7)
#"hundred and" 9*99 times => 9*99*10
#
# => 20259 + 854 + 11
# = 21124  

