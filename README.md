# rpg-character-generator

Reddit bot that uses this character generator: https://github.com/kjong/rpg-reddit-bot

## How It Works
The user input is used as the seed for a randomly generated 16 digit number.
The attributes of the character are based on this 16 digit "character number".

```
# creates number to base character on
def gen_char_num(in_name) -> int:
    random.seed(in_name)
    # generate 16 digit char_num
    return "%0.16d" % random.randint(0, 9999999999999999)
```

By using the user input as the seed for this character number, every character that is generated is uniquely tied to each user.

Sections of the character number are used to determine each attribute.

For example, the surname of the generated character is determined by the first 4 digits of the character number.

That 4 digit number is used to find the corresponding name in `lists/surnames.txt`.

```
# surname (4 numbers)
char_dict["surname"] = get_line_at_index(
    "lists/surnames.txt", char_num, 0, 4).capitalize()
```

## Attributes
* Name

* Surname

* Race

* Cosmic force

* Alignment

* Strength (1 ~ 9)

* Agility (1 ~ 9)

* Intelligence (1 ~ 9)

* Charisma (1 ~ 9)

* Weapon

* Utility item

## Example
```
Enter your name:
Bruce Wayne
Bruce Wayne the Descriptive
Race: Human
Cosmic force: death
Alignment: chaotic evil
Strength: 1
Agility: 2
Intelligence: 6
Charisma: 6
Weapon: unarmed
Utility item: soap
Generated 12 characters
```
