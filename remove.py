from unidecode import unidecode

def removeAdor(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

folder = open('HistoriaDosIndios.txt', 'r', encoding = 'utf8')

text = folder.read()

newText = text.lower()
newText2 = unidecode(newText)

newText3 = removeAdor(newText2, '/1234567890+\.><_:?!,;*()[]{}ªº¢¥¤ð-ßµÞ¦¶Ð+#@$%&^~´`§■«©■•�"‘£\'')

folderFomarted = open('textFormated.txt', 'w')

folderFomarted.write(newText3)

folder.close()
folderFomarted.close()