# методами строк очистить текст от знаков препинания;
txt="Хочется чая! А к чаю - горячие плюшки. \n"+\
    "И непременно под глянцевым боком плечо! \n"+\
    "(Душ единенье, как в маленькой старой однушке) \n"+\
    "В тёплых объятьях сжимать непутево-заблудших \n"+\
    "И улыбаться на краткое, ёмкое «чё».\n"
print(txt)
znaki='\"!@#$%^&*()_+=-,./\\«»№;:?'
for z in znaki:
    txt=txt.replace(z,'')
print(txt)

# сформировать list со словами (split);
lst=txt.split()
print(type(lst), len(lst), lst)

# привести все слова к нижнему регистру (map) и
# выполнить лемматизацию. https://pymorphy2.readthedocs.io/en/0.2/user/index.html;
# import https://github.com/no-plagiarism/pymorphy3
import pymorphy3

lst=[x.lower() for x in lst]
print(lst)

mor=pymorphy3.MorphAnalyzer()
lst=[mor.parse(x)[0][2] for x in lst]
print(lst)

# получить из list пункта 3 dict,
# ключами которого являются слова,
# а значениями их количество появлений в тексте;
lst_uniq = list(set(lst))
dct = dict([(x,lst.count(x)) for x in lst_uniq])
print(dct)

# вывести 5 наиболее часто встречающихся слов (sort)
dct_sorted_keys = sorted(dct, key=dct.get, reverse=True) # список ключей сортированных по значению
print([x for x in dct_sorted_keys[:5]])

# вывести количество разных слов в тексте (set).
print(lst_uniq)

