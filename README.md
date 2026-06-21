# RPG-Maker-Team-Compostition
Was destiny inspired to help me better understand what i wanted to achieve view the read me or code itselft as there is alot of information in there also cause at the time of making this code I a big destiny 2 fan had its final update and wanted to do something thats inspired by the game itself


# RPG Maker — Destiny 2 Fireteam Composition Checker

A terminal-based Python project inspired by Destiny 2, built to practice core Object-Oriented Programming concepts.

## What it does

- Select your guardian class (Titan, Hunter, Warlock) and super ability
- Choose a Dungeon (3 players) or Raid (6 players) activity
- Fill the rest of your fireteam manually or randomize it
- Get a full team breakdown and composition analysis

## Concepts practiced

| Concept | How it was used |
|---|---|
| Classes | Base `RPG` class stores owner and super |
| Inheritance | `Titan`, `Hunter`, `Warlock` extend `RPG` with unique roles |
| Polymorphism | `.analyze()` called on every guardian — each runs its own version |
| Dictionaries | Used as hashmaps for class/super selection and activity mapping |
| Lists | Fireteam stored as a list of guardian objects |
| Functions | Modular design — input validation, guardian builder, comp checker all separated |
| Randomization | `random` module used to generate random teammates |

## How to run

```bash
python3 RPGmaker.py
```

## Example output

```
--- Dungeon Team ---
1) Class: Titan | Super: Thundercrash | Role: Tank
2) Class: Hunter | Super: Tether | Role: DPS
3) Class: Warlock | Super: Well | Role: Support

--- Analysis ---
Titan — DPS burst
Hunter — team support
Warlock — team support

✓ Good comp
```

## Author

Christopher DeMoura — Computer Engineering & Electrical Engineering  
University of Massachusetts Dartmouth
