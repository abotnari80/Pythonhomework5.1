# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

letters = 'абв'
with open('Task1Text.txt') as file:
    text = ' '.join(file.readlines()).lower().split(' ')
    filtered = [word for word in text if letters in word]
print(*filtered, sep='\n')