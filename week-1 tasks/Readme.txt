Hi this is the code for the random password generator. This is a command-line tool for generating random passwords with customizable length and complexity. 

This password generator project has these features : 
• Users can specify the length of the password to be generated. 
• Users can specify the type of password to be generated (For ex. uppercase letters, lowercase letters, digits or special characters.

Below are the Commands and Options which needs to be used to get your password generated : 
• -l, --length (required): Specifies the length of the password. 
• -u, --uppercase: Include uppercase letters in the password. 
• -lo, --lowercase: Include lowercase letters in the password. 
• -d, --digits: Include digits in the password. 
• -s, --special: Include special characters in the password.

Please Note : 
The first option i.e. the length of the password is mandatory. 
Selecting at least one type from the given types is also mandatory.

To use this project we need to use the commands. Examples are given below:

Ex 1: python random_password_generator.py -l 8 -u -lo -d -s
This command will generate a random password of length 8 including all the types as we have specified in the command to include uppercase, 
lowercase, digits and special characters.

Ex 2: python random_password_generator.py -l 16 -u -s
This command will generate a random password of length 16 including only uppercase and special characters.

Error Handling :
• The tool will raise an error if the password length is less than 1.
• The tool will raise an error if none of the character types (uppercase, lowercase, digits, special characters) are selected.
