def check_password(password):
    if len(password) < 10 or len(password) > 15:
        return " Password should be at least 10 characters long but should not exceed 15 characters."
    elif not any(c.isupper() for c in password):
        return "Password It should consist of at least one uppercase letter."
    elif sum(c.islower() for c in password) < 2:
        return "Password should consist of more than one lowercase letter."
    elif(password.isdigit()):
        return "password should consist at least 1 digit"
    elif not any(c in '@!#' for c in password):
        return "password should consists of at least one special character"
    elif any(c.isspace() for c in password):
        return "Password should not contain spaces"
    elif password[-1] in '.@':
        return "should not end with . or @"
    else:
        return "Strong password"
password = input("Enter your password: ")
result = check_password(password)
print(result)