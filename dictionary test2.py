print("Welcome to MySpace. Want to create a new account? Please enter your email, new username and password.")

email = input()
print("EMAIL REGISTERED.")
username = input()
print("USERNAME REGISTERED.")
password = input()
print("PASSWORD REGISTERED.")

userprofile = {
    "name": (username),
    "email@@": (email),
    "password12": (password),
}
print("Welcome, user '1212444' to MySpace! Your email is: ", userprofile["email@@"], ",", "your username is: ", userprofile["name"], ",", "and you password is ,'", userprofile["password12"], "' .")

# ---Old Test (doesn't work(working version in 'dictionary test3'))---

print("would you like to log onto your MySpace account?")
print("please enter your login details")

email = input()
print("processing... please enter username.")
username = input()
print("processing... please enter password.")
password = input()

if userprofile["email@@"] != (email):
    print("email incorrect.")
if userprofile["email@@"] == (email):
    print("EMAIL REGISTERED.")
if userprofile["name"] != (username):
        print("username incorrect")
if userprofile["name"] == (username):
    print("USERNAME REGISTERED.")
if userprofile["password12"] != (password):
    print("password incorrect")
if userprofile["password12"] == (password):
    print("PASSWORD REGISTERED.")
    print("welcome to MySpace!")

