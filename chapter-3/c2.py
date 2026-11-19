def count_vowels(text):
    count=0
    for i in text.lower():
        if i in "aeiou":
            count+=1
        else:
            pass
    print(count)
count_vowels("Hello World")