def wordCount(t):
    """
    Retrieves data from a text file t and returns a dictionary where the keys are unique words
    in the file and the corresponding values are lists of line numbers where the words are found.
    """
    word_dict = {}

    with open(t, 'r') as file:
        # Read each line in the file
        for line_number, line in enumerate(file, start=1):
            # Split the line into words
            words = line.strip().split()

            # Process each word
            for word in words:
                # Convert the word to lowercase for case-insensitive comparison
                word = word.lower()

                # If the word is not in the dictionary, add it with an empty list
                if word not in word_dict:
                    word_dict[word] = []

                # Append the line number to the list of occurrences of the word
                word_dict[word].append(line_number)

    return word_dict


print("Word occurrences:", wordCount('q3.txt'))