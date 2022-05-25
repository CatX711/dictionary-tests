email = input()
username = input()
password = input()

userprofile = {
    "name": (username),
    "email@@": (email),
    "password12": (password),
}

print("would you like to log onto your MySpace account?")
print("please enter your login details")

email = input()
username = input()
password = input()

if userprofile["email@@"] == (email):
    print("processing... please enter username")
    if userprofile["name"] == (username):
        print("processing... please enter password")
        if userprofile["password12"] == (password):
            print("password correct! welcome to MySpace.")

