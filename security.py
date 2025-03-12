


import bcrypt

# Hash a password
def hash_password(password):
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Verify a password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Test the functions
password = "MyS3cur3P@ssword"
hashed_password = hash_password(password)
print(f"Hashed Password: {hashed_password}")

# Check if the password is correct
is_valid = verify_password("MyS3cur3P@ssword", hashed_password)
print(f"Password is valid: {is_valid}")
