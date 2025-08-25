import random
from fillpdf import fillpdfs
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

#Selecting your Characters Name
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

#getting the form fields
form_fields = list(fillpdfs.get_form_fields("dnd_character_sheet.pdf").keys())

#Filling out the PDF
CharacterName = char_name
CharacterClass = char_class
CharacterSpecies = char_species
CharacterSubclass = char_subclass
InteligenceMod = intelligence_modifier
inteligence  = total_intelligence

data_dict = {
    form_fields[0]: CharacterName,
    form_fields[1]: CharacterClass,
    form_fields[2]: CharacterSpecies,
    form_fields[3]: CharacterSubclass,
    form_fields[4]: str(intelligence_modifier),
    form_fields[5]: str(total_intelligence),
    form_fields[6]: str(strength_modifier),
    form_fields[7]: str(total_strength),
    form_fields[8]: str(wisdom_modifier),
    form_fields[9]: str(total_wisdom),
    form_fields[10]: str(dexterity_modifier),
    form_fields[11]: str(total_dexterity),
    form_fields[12]: str(constitution_modifier),
    form_fields[13]: str(total_constitution),
    form_fields[14]: str(charisma_modifier),
    form_fields[15]: str(total_charisma)
}

fillpdfs.write_fillable_pdf(input_pdf_path='dnd_character_sheet.pdf',output_pdf_path=f"{char_name}.pdf",data_dict=data_dict)
print("\n")
#Character Summary 
print("Character Summary")
print("_________________")
print(f"Character Name: {char_name}")
print(f"Character Class: {char_class}")
print(f"Character Sub-Class: {char_subclass}")
print(f"Character Species: {char_species}")
print(f"Intelligence: {total_intelligence} \nintellifence Modifier: {intelligence_modifier}")
print(f"Strength: {total_strength}\nStrength Modifier: {strength_modifier}")
print(f"Dexterity: {total_dexterity}\nDexterity Modifier: {dexterity_modifier}")
print(f"Wisdom: {total_wisdom}\nWisdom Modifier: {wisdom_modifier}")
print(f"Constitution: {total_constitution}\nConstitution Modifier: {constitution_modifier}")
print(f"Charisma: {total_charisma}\nCharisma Modifier: {charisma_modifier}")
print(f"{char_name}.pdf has been created! check the root of this project folder.")

input("Press Enter to exit...")