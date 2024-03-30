# Mail Merge
# This program takes a letter template and a wordlist of names, then creates personalized letters for each name

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

names_clean = []
for name in name_list:
    names_clean.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as template:
    template_content = template.read()

    for name in names_clean:
        modified_content = template_content.replace("[name]", name)
        file_name = f"letter_to_{name}"

        with open(f"./Output/ReadyToSend/{file_name}".replace(" ", "_"), "w") as letter:
            letter.write(modified_content)
