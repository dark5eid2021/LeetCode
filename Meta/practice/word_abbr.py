word = "internationalization"
pattern = "i18n"

def is_valid_interpretation(word, pattern):
    if len(pattern) < 3:
        return False
    
    first_char = pattern[0]
    last_char = pattern[-1]

    number_part = pattern[1: -1]

    if not number_part.isdigit():
        return False
    
    count = int(number_part)

    if len(word) < count + 2:
        return False
    
    if word[0] != first_char or word[-1] != last_char:
        return False
    
    if len(word) -2 != count:
        return False
    
    return True

print(is_valid_interpretation(word, pattern))