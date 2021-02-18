with open("Text1.txt", "r", encoding="UTF8") as rfile:
    data = rfile.read()
    data = data.replace("/n", " ")
    data = data.replace(",", "").replace("'", "").replace(".", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("—", "")
    data = data.lower()
    words = data.split()

    max_count = 0
    new = []
    for word in words:
        if words.count(word) > max_count:
            max_count = words.count(word)
        if words.count(word) == max_count:
            new.append(word)
    new = list(set(new))
    new = ", ".join(new)

    with open("Results.txt", "w", encoding="UTF8") as wfile:
        wfile.write("Количество слов в тексте равно: " + str(len(data.split(" "))) + "\n")
        wfile.write("Количество уникальных слов в тексте равно: " + str(len(set(words))) + "\n")
        wfile.write("Наиболее часто встречаются слова: " + str(new) + ".")
rfile.close()







