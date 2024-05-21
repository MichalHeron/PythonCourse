from translate import Translator
translator = Translator(to_lang="pl")

try:
    with open('file.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('file-pl.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print(e)

