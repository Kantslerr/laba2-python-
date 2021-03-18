text = str(input("Введите строку: "))
def check_palindrome(text):
    import string
    for i in text:
        text = text.lower()
        text = ''.join(e for e in text if e.isalnum())
        revers = ''.join(reversed(text))
    print(revers)
    if text == revers:
        print("Строка", text, "является палиндром:")
    else: print("Строка", text, "не является палиндромом: ")

check_palindrome(text)
