PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as guests:
    names = guests.readlines()

with open('./Input/Letters/Hello.docx') as starting_letter:
    content = starting_letter.read()

for name in names:
    stripped_name = name.strip()
    new_letter = content.replace(PLACEHOLDER, stripped_name)

    with open(f"Output/ReadyToSend/{stripped_name}.txt", mode='w') as final_letter:
        final_letter.write(new_letter)