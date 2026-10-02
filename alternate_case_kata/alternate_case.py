def alternate_case(input_word):
    list_of_words = input_word.split()
    output = []
    counter = 0
    for word in list_of_words:
        new_word =[]
        for i in range(0, len(word)):
            if counter %2==0:
                new_word.append(word[i].upper())
            else:
                new_word.append(word[i].lower())
            counter +=1
        camel_word = "".join(new_word)
        output.append(camel_word)

    answer = " ".join(output)
    return answer
