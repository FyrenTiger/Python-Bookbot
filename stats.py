def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = file_contents.split()
    return (len(word_count))


def char_breakdown(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        lowercase_file = file_contents.lower()

    char_count = {
        }

    for i in range (0, len(lowercase_file)):

        if lowercase_file[i] in char_count:
            char_count[lowercase_file[i]] += 1
        else:
            char_count[lowercase_file[i]] = 1

    return char_count


def sort_on(dict):
    return dict["count"]

def sort_dictionary(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict