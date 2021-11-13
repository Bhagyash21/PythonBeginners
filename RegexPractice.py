# #Program 1
# import re
# phone = "2004-959-559 # This is Phone Number"
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print( "Phone Num : ", num)
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print ("Phone Num : ", num)



#Program 2
import re
def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))

