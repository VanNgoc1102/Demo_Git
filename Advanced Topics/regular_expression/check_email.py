import re

# Define a function for
# for validating an Email

def check(email):
    pattern = r'\b[a-zA-Z0-9_.%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,4}\b'
    # \	Signals a special sequence (can also be used to escape special characters)
    # \b	Returns a match where the specified characters are at the beginning or at the end of a word
    #           (the "r" in the beginning is making sure that the string is being treated as a "raw string")
    # \.
    matcher = re.search(pattern, email)
    if matcher:
        print("Valid email")
    else:
        print("Invalid Email")

if __name__ == '__main__':
 
    # Enter the email
    email = "ankitrai326@@gmail.com"
 
    # calling run function
    check(email)
 
    email = "my.ownsite@our-earth.org"
    check(email)
 
    email = "ankitrai326.com"
    check(email)

