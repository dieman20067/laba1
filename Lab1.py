print("Hello Python from Visual Studio!")
# Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе
# добавить в конец строки "zzz"

text = input('your last word: \n')

if text[0:3] == 'abc':
    text = "www" + text[3:]
else:
    text = text + "zzz"
    
print(text)
input('Press <ENTER> to exit.')