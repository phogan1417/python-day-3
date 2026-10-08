def vote_age_check():
    persons_age = int(input("How old are you?"))
    if persons_age >= 18:
        print("You Can Vote!")
    else:
        print("Sorry, You Can Not Vote.")

def main():
    vote_age_check()
main()