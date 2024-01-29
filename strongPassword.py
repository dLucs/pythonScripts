import re

# password regex to check that for least eight characters long, contain both uppercase and lowercase characters, and have at least one digit.

passRegex = re.compile(
    r"""(
        (?=.*[a-z])
        (?=.*[A-Z])
        (?=.*\d)
        [a-zA-Z\d]{8,}
    )""",
    re.VERBOSE,
)


print(
    "Input password that is at least eight characters long, contain both uppercase and lowercase characters, and has at least one number."
)

while True:
    password = input()
    if passRegex.match(password):
        print("Password is strong!")
        break
    else:
        print("Password is not strong enough. please input strong password:")
