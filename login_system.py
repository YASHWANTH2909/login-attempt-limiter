import time

# Correct credentials
USERNAME = "admin"
PASSWORD = "password123"

MAX_ATTEMPTS = 3
LOCK_TIME = 30  # seconds

attempts = 0

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login Successful!")
        break

    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        if remaining > 0:
            print(f"Invalid credentials. Attempts remaining: {remaining}")

        if attempts >= MAX_ATTEMPTS:
            print(f"\nToo many failed attempts.")
            print(f"Account locked for {LOCK_TIME} seconds.")

            time.sleep(LOCK_TIME)

            print("\nYou may try again.")
            attempts = 0
