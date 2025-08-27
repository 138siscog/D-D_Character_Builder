# D&D 5e Character Builder (CLI)

A simple Python CLI that helps you build a D&D 5e character by rolling ability scores and letting you choose a class, species, and subclass. The project also includes curated data files for species and subclasses to speed up character creation.

## (DO NOT DELETE THE PDF FILE "dnd_character_sheet" THIS IS WHAT IS USED TO AUTOFILL THE INFO)

## How it works

### 1) Rolling Ability Scores
- Uses the classic **4d6 drop-lowest** method.
- For each score:
  1. Roll four six-sided dice.
  2. Drop the lowest die.
  3. Sum the remaining three → **ability score** (e.g., 14).
- Repeated six times to produce scores for **STR, DEX, CON, INT, WIS, CHA**.

### 2) Computing Modifiers
- D&D 5e modifier formula:
  ```
  modifier = floor((score - 10) / 2)
  ```
  Examples: 10–11 → +0, 12–13 → +1, 14–15 → +2, 8–9 → −1.

### 3) Choosing Class, Species, and Subclass
- The CLI prompts you to choose:
  - **Class** (e.g., Fighter, Wizard, etc.)
  - **Species** (from the curated list)
  - **Subclass** (specialization tied to the chosen class)
- If you type `Option`, it prints the available choices.  
- Input is validated against the lists in `species.py`, `dnd_class.py`, and `sub_class.py`.

### 4) Data Files
- **`species.py`**: Core 5e species that most tables allow.
- **`dnd_class.py`**: Extra/expanded species with short flavor descriptions to help users decide quickly.
- **`sub_class.py`**: A mapping of **Class → Subclasses** (PHB first, expandable).

> The code is structured so you can swap in a different species/subclass catalog later (e.g., to align with your table’s allowed books).

## 5) PDF File

> The program now fills out the PDF D&D Character Sheet, when this happens it is named after your characters name and is exported to the root of the "D&D Character" Folder
> The program now lets you decide if you would like to create another character before closing the program

## Dependencies

List is intentionally small and ready for future PDF work:
random
fillpdf

## License

Copyright (c) 2025 138siscog

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
