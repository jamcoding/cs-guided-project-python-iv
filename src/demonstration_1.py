"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore97
if there is a mathematical approach that you can take.*
"""
# def to_lower_case(string):
#     # Your code here
#     # create an empty string / list to add our output to
#     result = ""
#     for char in string:
#         # encode it to a number
#         num = ord(char)
#         if 65 <= num <= 90:
#             # this is a capital english character turning into lower case
#             num += 32
#         result += chr(num)
#     return result

def to_lower_case(string):
    # print(string.encode())
    output_str = ''
    for num in string.encode():
        if 65 <= num and num <= 90:
            num += 32
        output_str += chr(num)
    return output_str

print(to_lower_case("Hello World"))
# print(to_lower_case("lambda school"))
# print(to_lower_case("LAMBDAAAAA"))