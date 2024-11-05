with open('vocal.txt', 'r') as file:
    content = file.read()

content_no_spaces = content.replace(" ", "")

with open('vocal.txt', 'w') as file:
    file.write(content_no_spaces)

print("the vocals are now compressed :D")