msg = input(">")
words = msg.split()
emoji = {
    ":)": "🙂",
    ":(": "☹️"
}
output = ""
for word in words:
    output += emoji.get(word,word) + " "
print(output)