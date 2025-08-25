import random
import reportlab
import pdfrw
import numpy as np
from dnd_class import dnd_class, dnd_class_description
from species import dnd_species, dnd_species_list
from sub_class import dnd_subclasses, dnd_subclass_list

#Rolling 4d6 and dropping the lowest for ability scores
def roll_dice():
    dice = [random.randint(1, 6) for _ in range(4)]
    dice.remove(min(dice))  # Remove the lowest roll
    return tuple(dice)

#Intelligence
intelligenceroll = roll_dice()
intelligence = []
intelligence.extend(intelligenceroll)
total_intelligence = sum(intelligence)
intelligence_modifier = (total_intelligence - 10) // 2

#Strenght
strengthroll = roll_dice()
strength = []
strength.extend(strengthroll)
total_strength = sum(strength)
strength_modifier = (total_strength - 10) // 2

#Dexterity
dexterityroll = roll_dice()
dexterity = []
dexterity.extend(dexterityroll)
total_dexterity = sum(dexterity)
dexterity_modifier = (total_dexterity - 10) // 2

#Wisdom
wisdomroll = roll_dice()
wisdom = []
wisdom.extend(wisdomroll)
total_wisdom = sum(wisdom)
wisdom_modifier = (total_wisdom - 10) // 2

#Constitution
constitutionroll = roll_dice()
constitution = []
constitution.extend(constitutionroll)
total_constitution = sum(constitution)
constitution_modifier = (total_constitution - 10) // 2

#Charisma
charismaroll = roll_dice()
charisma = []
charisma.extend(charismaroll)
total_charisma = sum(charisma)
charisma_modifier = (total_charisma - 10) // 2

#Selecting your Characters Nmae
char_name = input("What is your character's name?: ").title()

#Selecting  your characters Class
while True:
    char_class = input("Choose your class (type: Option) for class list: ").strip().title()
    if char_class.title() == "Option":
        for c in dnd_class_description:
            print("\n")
            print(c)
        continue  # Ask again after showing the list
    if char_class not in dnd_class:
        print("Invalid class selection. Please try again.")
    else:
        break  # Valid class selected, exit loop

#Selecting Your Characters Species
while True:
    char_species = input("Choose your species (type: Option) for species list: ").strip().title()
    if char_species.title() == "Option":
        for s in dnd_species_list:
            print("\n")
            print(s)
        continue
    if char_species not in dnd_species:
        print("Invalid species selection. Please try again.")
    else:
        break

#Selecting Your Characters Subclass
while True:
    char_subclass = input("Choose your subclass (type: Option) for subclass list: ").strip().title()
    if char_subclass.title() == "Option":
        for sc in dnd_subclass_list:
            print("\n")
            print(sc)
        continue
    if char_subclass not in dnd_subclasses:
        print("Invalid subclass selection. Please try again.")
    else:
        break

#Character Summary 
print(f"Character Name: {char_name}")
print("\n")
print(f"Character Class: {char_class}")
print("\n")
print(f"Character Sub-Class: {char_subclass}")
print("\n")
print(f"Character Species: {char_species}")
print("\n")
print(f"Intelligence: {total_intelligence} \nintellifence Modifier: {intelligence_modifier}")
print("\n")
print(f"Strength: {total_strength}\nStrength Modifier: {strength_modifier}")
print("\n")
print(f"Dexterity: {total_dexterity}\nDexterity Modifier: {dexterity_modifier}")
print("\n")
print(f"Wisdom: {total_wisdom}\nWisdom Modifier: {wisdom_modifier}")
print("\n")
print(f"Constitution: {total_constitution}\nConstitution Modifier: {constitution_modifier}")
print("\n")
print(f"Charisma: {total_charisma}\nCharisma Modifier: {charisma_modifier}")
print("\n")