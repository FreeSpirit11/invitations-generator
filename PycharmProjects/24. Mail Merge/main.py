with open("./Input/Letters/starting_letter.txt") as file:
    all_lines=file.read()

with open("./Input/Names/invited_names.txt") as data:
    all_names=data.readlines()

first_line=all_lines[0]
for namee in all_names:
    name=namee.strip()
    new_lines=all_lines.replace("[name]",name)
    with open(f"./Output/ReadyToSend/invitation_card_{name}.txt",mode="w") as card:
            card.write(f"{new_lines}")

