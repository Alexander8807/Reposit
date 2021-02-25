# новые методы dump  dumps  load  loads

import json

json_string = '''       
{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false,
      "salary": 1500
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true,
      "salary": 1700
    },
    {
      "name": "Steven Cooke",
      "phone": null,
      "emails": "stevencooke@example.com",
      "has_licence": true,
      "salary": 2500
    }
  ]
}'''

data = json.loads(json_string)    #прочитать древо, загрузить

print(type(data))                 #читается, как словарь, методы словарей к нему подходят
print(data)

print(type(data["people"]))       #превращает в список
print(data["people"][0]["emails"][0])   #выбрать из 1го элемента списка мыло

#for person in data["people"]:
#    print(person)
#    print(person["emails"][0])    #можно работать как со списком

people = data["people"][1]  #обращение через переменную
print(people["name"], people["phone"])
print(people)

for person in data["people"]:
    del person["phone"]

print(data["people"])
print(type(data))
print(data)

new_string = json.dumps(data, indent=2, sort_keys=True)  #indent сколько пробелов в отступах, sort_keys сортировка в алфавитном порядке да - True, нет - false
print(new_string)
print(type(new_string))     #взяли строку для работы, поработали, и сохранили снова в строку

