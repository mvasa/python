#d	Signed integer decimal.
#i	Signed integer decimal.
#o	Unsigned octal.	(1)
#u	Unsigned decimal.
#x	Unsigned hexadecimal (lowercase).	(2)
#X	Unsigned hexadecimal (uppercase).	(2)
#e	Floating point exponential format (lowercase).
#E	Floating point exponential format (uppercase).
#f	Floating point decimal format.
#F	Floating point decimal format.
#g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
#G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
#c	Single character (accepts integer or single character string).
#r	String (converts any python object using repr()).	(3)
#s	String (converts any python object using str()).	(4)
#%	No argument is converted, results in a "%" character in the result.
#printing variables without string formatters


#Escape What it does.
#\\ Backslash (\)
#\' Single- quote (')
#\" Double- quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r ASCII carriage return (CR)
#\t ASCII horizontal tab (TAB)
#\uxxxx Character with 16- bit hex value xxxx (Unicode only)
#\Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
#\v ASCII vertical tab (VT)
#\ooo Character with octal value oo
#\xhh Character with hex value hh
print "\n\n----------------------------------------------------------------"
cards = 52
decks = 4
players = 10
rules = """
the rules of the game are 
that there are no rules.
this game is 
pointless
"""

print "each player gets", (52*4)/10, "cards"
print "there are", decks, "decks"
print "there are", players, "players"
print "there are ", cards*decks, "cards"
print "here are the rules: \n%s" % rules
#printing variables with string formatters
print "\n\n----------------------------------------------------------------"
myAge = 22
myName = "None"
myOccupation = "IT"

print "my age is %s" % myAge
print "my name is %s" % myName

print "my name, age, and occupation is %s, %s, and %s" % (myName, myAge, myOccupation)

#string practice
print "\n\n----------------------------------------------------------------"

w = "test string"
testStr = " test String 2"
print w + testStr, "\n"

testStr2 = "This is an example boolean formatter statement %r"
boolVal = True
print testStr2 % boolVal


testStr4 = "this is another test string with more than %d words" % 12
var = "here's another example: %r" % testStr4
print var

#more string formatter practice
print "\n\n----------------------------------------------------------------"

formatter = "%r %r %r %r"

print formatter % ("hello", "hell", "hel", "he")
print formatter % (True, False, False, True)
