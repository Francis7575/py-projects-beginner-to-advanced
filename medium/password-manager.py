from cryptography.fernet import Fernet

# def write_key():
#   key = Fernet.generate_key()
#   with open("key.key", "wb") as key_file:
#     key_file.write(key)
    
def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

key = load_key()
fer = Fernet(key)

# 'a' append, 'r' read mode, 'w' write mode
def view():
  with open('password.txt', 'r') as f:
    for line in f.readlines():
      data = (line.rstrip())
      user, passw = data.split("|")
      print("User:", user, "| Password:", str(fer.encrypt(passw.encode())))


def add():
  name = input("Account Name: ")
  pwd = input("Password: ")

  with open('password.txt', 'a') as f:
    f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
  mode = input("Would you like to add a new password or view existing ones (view, add)? press Q to quit ").lower()
  if mode == "q":
    break

  if mode == "view":
    view()
  elif mode == "add":
    add()
  else: 
    print("Invalid mode")