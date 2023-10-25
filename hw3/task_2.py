"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами, апостроф не считается за пробел. Такие слова как dont, its, didnt итд
(после того, как убрали знак препинания апостроф) считать одним словом.
"""
text = "Python is an interpreted, high-level, general-purpose programming language. " \
       "Created by Guido van Rossum and first released in 1991, " \
       "Python's design philosophy emphasizes code readability with its " \
       "notable use of significant whitespace. Its language constructs and " \
       "object-oriented approach aim to help programmers write clear, logical " \
       "code for small and large-scale projects."
text_1 = text.replace(".", "").replace(",", "") \
    .replace("'", " ").replace("!", "").replace("?", "").replace("-", " ").lower().split(" ")
lst = []
dict_1 = {}
for i in text_1:
    if i.isalpha():
        dict_1[i] = dict_1.get(i, 0) + 1
lst = sorted(dict_1.items(), key=lambda item: item[1], reverse=True)
print(lst[:10])
