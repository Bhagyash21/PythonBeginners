import re
text = """Hello my number is 123456789 and my friend's number is 987654321"""
output = re.findall('[0-9]+', text)
print(output)
