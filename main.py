PLACEHOLDER = "[name]"

with open("/Users/ethanlai/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    names = data.readlines()


with open("/Users/ethanlai/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,new_name)
        with open(f"/Users/ethanlai/Downloads/Mail Merge Project Start/Output/ReadyToSend/To_{name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)

