
def valid_email(n):
    if "@" in n and "." in n:
        print("Your e-mail is valid")
        return True
    else:
        print("Your e-mail is invalid")
        return False
valid_email(input("E-mail adresini giriniz:"))