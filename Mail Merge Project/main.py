PLACEHOLDER = "[name]"

with open("./Input/Names/Invited_names.txt") as namesFile:
    names = namesFile.readlines() # The readlines() method returns a list containing each line in the file as a list item.
    print(names)

with open("./Input/Letters/starting_letter.txt") as letterFile:
    letterContent = letterFile.read()  #  This is going to be a normal read because I want all of the content inside
    # that letter. It is now going to be saved as a string inside my letterContent.
    for name in names:
        strippedName = name.strip() # The strip() method removes any leading, and trailing whitespaces.
        newLetter = letterContent.replace(PLACEHOLDER, strippedName)
        with open(f"./Output/ReadyToSend/letter_for_{strippedName}.txt", mode='w') as completedLetter:
            completedLetter.write(newLetter)
