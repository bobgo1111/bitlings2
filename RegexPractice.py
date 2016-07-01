import re

text = ''
while True:
    print("-------------------------- %s ----------------------"%(text))
    newText = input('New text (just press ENTER use same): ')
    if newText:
        text = newText
    regEx = input('Regex: ')
    try:
        matcher = re.compile(regEx)
        print("RegEx<%s> matches %s"%(regEx, matcher.findall(text)))
    except:
        print("Error compiling RegEx<%s>"%(regEx))
