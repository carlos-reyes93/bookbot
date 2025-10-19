def get_word_count(text):
    return len(text.split())

def get_count_chars(text):
    count = {}

    for w in text.split():
        for i in range(len(w)):
            c = w[i].lower()
            if (c in count):
                count[c]+=1
            else:
                count[c] = 1
    return count

def sort_on(items):
    return items["num"]

def sort_count(count):
    new_dict = []
    for key in count:
        new_dict.append({ "char": key, "num": count[key] })

    new_dict.sort(reverse=True, key=sort_on)

    return new_dict

