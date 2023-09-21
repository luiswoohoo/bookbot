path_to_file = "books/frankenstein.txt"

chars = {}

with open(path_to_file) as f:
    file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)
   
    for word in words:
        for char in word:
            if char.lower() in chars:
                chars[char.lower()] += 1
            else:
                chars[char.lower()] = 1 

    char_list = list(chars)
    char_list.sort()

    print("\n")
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    
    for char in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")

    print("\n")
    print("--- End report ---")
    print("\n")
