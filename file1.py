from sys import argv
script, filename = argv

try:
    txt = open(filename)
    print(f"Here's your file {filename}")
    print(txt.read())
    txt.close()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found")
    exit(1)

print("Type the file name again :")
filename_again = input("> ")

try:
    txt_again = open(filename_again)
    print(txt_again.read())
    txt_again.close()
except FileNotFoundError:
    print(f"Error: File '{filename_again}' not found")
