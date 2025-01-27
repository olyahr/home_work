def count_word_freq(file_name):
  word_counts = {}
  with open(file_name) as text_file:
    text_contents = text_file.readlines()
    for line in text_contents:
        words = line.lower().split() # Split into words ["I", "love", "Python." ]
        for word in words:
           word = word.strip('.,!?"') #remove punctuation
           if word != "":
              word_counts[word] = word_counts.get(word, 0) + 1 # Skip empty strings
  return word_counts

def sort_dictionary_and_write_to_file(dictionary):
    list_to_write = []  # [("i", 1), ("python", 2), ...]

    for key, value in dictionary.items():
        list_to_write.append((key, value))

    # Sort the list based on the second element (value) in descending order
    def sort_by_value(item):
        return item[1]

    list_to_write.sort(key=sort_by_value, reverse=True)

    with open("newfile.txt", "w") as dict_file:
        for item in list_to_write:
            dict_file.write(item[0] + ":" + str(item[1]) + "\n")

final_dictionary = count_word_freq("textfile.txt")
print(final_dictionary)

sort_dictionary_and_write_to_file(final_dictionary)

print("All done")