print("Make your Password Stronger!")
print("Insert Password Here :")
get_user_password = input()

def create_replacement_rules():
    rules = {
        'i': '1',
        'a': '@',
        'm': 'M',
        'B': '8',
        's': '$',
        'o': '0',
        'e': '3',
        'l': '!',
        't': '7',
        'g': '9',
        'z': '2',
        'A': '4',
        'S': '5',
        'b': '6',
        'q': '9'
    }
    return rules

def modified_password(get_user_password, rules):
    checking_characters_in_password = ""
    
    for char in get_user_password:
        if char in rules:
            checking_characters_in_password += rules[char]
        else:
            checking_characters_in_password += char
            
    return checking_characters_in_password

rules = create_replacement_rules()
stronger_password_made_from_rules_above = modified_password(get_user_password, rules)

print("Your stronger password is:", stronger_password_made_from_rules_above)
