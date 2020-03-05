#файлы
# fool = open("test.txt", "w", encoding='utf-8')
# fool = open("/Users/Andrey/PycharmProjects/lessons/homework/test.txt", "r", encoding='utf-8' )

# content = fool.readlines()
# print(content)

# for i in fool:
#     print(i)

# while True:
#     content = fool.read(1024)
#     print(content)
#     if not content:
#         break
# fool.close()

# fool = open("/Users/Andrey/PycharmProjects/lessons/homework/test1.txt", "a", encoding='utf-8' )
# # fool.write("Hello, Pyton!")
# fool.writelines(["Hello,\n", "Pyton!\n"])
# fool.close()
#
try:
    with open("test1.txt") as fool:
        print(type(fool))
        for i in fool:
            print(i)
except IOError:
    print("Ошибка!")
finally:
    print("ого")

# состояния:
# print("Файл. Имя: ", fool.name)
# print("Файл. Закрыт: ", fool.closed)
# print("Файл. Режим: ", fool.mode)
#
# import os
# print(os.listdir())

# import json
# data = {"income": {"salary": 50000, "bonus": 20000}}
# with open("my_json.json", 'w') as fool:
#     json.dump(data, fool)

json.dump(all_list, j_file, ensure_ascii=False, indent=4)