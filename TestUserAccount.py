#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Three things are missing from the line below - fill them in
my_user=UserAccount( "my_username" , "my_password" , "my_secret")

#Call the print_secret method (function) - it takes one input - a guess for the password.


#Use the wrong password as input here
my_user.print_secret("password_attempt")

#Use the right password here
my_user.print_secret("my_password")
