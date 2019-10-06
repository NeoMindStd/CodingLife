import re

fin = open("./resource.txt", 'r', encoding='UTF8')
fout = open("./result.txt", 'w',  encoding='UTF8')

fout.write('{')
contents = ""
for line in fin.readlines():
    try:
        p = re.compile('#[0-9]+|">[^<]+</a>')
        pokemon = p.findall(line)
        pokemon[0] = str(int(pokemon[0][1:len(pokemon[0])]))
        for i in range(1, len(pokemon)):
            pokemon[i] = pokemon[i][2:-4]
        contents+= f"{pokemon[0]}:{pokemon[1:len(pokemon[1])]},"
    except:
        pass
fout.write(contents[:-1])
fout.write('}')

fin.close()
fout.close()
