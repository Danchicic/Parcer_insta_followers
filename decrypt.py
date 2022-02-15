def links():
    fm = []
    with open('followers_list.txt', 'r+') as file:
        for line in file:
            abc = line
            el_s = 'https://www.instagram.com/' + line.split("\n")[0] + '/' + '\n'
            fm.append(el_s)

    with open('dict.txt', 'w') as file:
        for line in fm:
            file.write(line)
