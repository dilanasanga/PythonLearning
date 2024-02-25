#import random
#generate function to generate random number
#def generate():
#    return random.randint(1,100)
#call the function
#print (generate())
#rand_num = random.randint(1,100)
#print (rand_num)

import re

#string = "abc:cde:d-e:2232:param/SUPPORT"
#pattern = r"([^/]+)$"
#matches = re.search(pattern, string)
#print(matches.groups())
#if matches:
#    grouped1_content = matches.group(0)
#    grouped2_content = matches.group(1)
#    print(grouped1_content,grouped2_content)

#match = re.match(r"^(.*):([^:]+)::?$", "arn:aws:iam:123456789012:secret:OMS:OAuth2ClientCredentials::")

'''match = re.search(r"^(.*)/([^:]+)", "arn:aws:iam:123456789012:secret:OMS/OAuth2ClientCredentials")
secretArn = match.group(1)
secretKey = match.group(2)
print(secretArn)
print(secretKey)
'''
data = {
    'Parameter': {
        'Name': 'string',
        'Type': 'String',
        'Value': 1111,
        'Version': 123,
        'Selector': 'string',
        'SourceResult': 'string',
        'LastModifiedDate': 'String',
        'ARN': 'string',
        'DataType': 'string'
    }
}

value_to_find = "Value"

# Iterate through the dictionary and find the key(s) matching the value
matching_keys = [key for key, value in data['Parameter'].items() if value == value_to_find]

# Print the matching keys
for key in matching_keys:
    print(key)
else:
    print("No matching key is found.")


#fizbuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)        




