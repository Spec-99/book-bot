def get_number_of_words(text):
    return len(text.split())

def get_number_of_characters(text):

    text = text.lower()
    
    num_of_characters = {}
# For each character in "text"
    for char in text:
        # Check if this character is already in our dictionary
        if char in num_of_characters:
            # If it is, increase its count by 1
            num_of_characters[char] += 1
            # If it's not, add it with a count of 1
        else:
            num_of_characters[char] = 1
    
    return num_of_characters
        

def sort_on(num_of_characters):
    return num_of_characters["count"]


def sort_character_by_count(num_of_characters):
    chars_list = [] #Creates an empty list to store the character dictionaries
    for char, count in num_of_characters.items(): #Loops through each character and count in the input dictionary
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list













    