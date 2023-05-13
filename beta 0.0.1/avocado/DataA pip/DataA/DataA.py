def welcoming_new_user(welcome_type, user_name):
    welcome_type = int(welcome_type)
    if welcome_type == 1:
        print("Hello there ", user_name, "!")
    if welcome_type == 2:
        print("Hello ", user_name, "!")
    if welcome_type == 3:
        print("Welcome ", user_name, "!")
