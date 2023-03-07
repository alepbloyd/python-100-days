#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as file:
  start_letter = file.read()

names = []
with open("./Input/Names/invited_names.txt", "r") as file:
  new_names = file.readlines()
  for name in new_names:
    names.append(name.strip())

for name in names:
  with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
    file.write(start_letter.replace("[name]", name))