from configparser import ConfigParser

config = ConfigParser()

config["EMAIL"] = {
    "email": "test@example.com",
    "password": "123456789"
}

config["DATABASE"] = {
    "name": "DBNAME",
    "password": "123456789",
    "host": "localhost"
}

config["DEFAULT"] = {
    "username": "Alex",
    "password": "123456"
}

with open("config2.ini", "w") as configfile:
    config.write(configfile)



from configparser import ConfigParser

config = ConfigParser()
config.read("config2.ini")

print(list(config["EMAIL"]))

password = config["DATABASE"]["name"]
print(password)

config.add_section("NEWLOGIN")  #добавить новый блок
config.set("NEWLOGIN", "login", "Alex123")
config.set("NEWLOGIN", "password", "1236548")
with open("config2.ini", "a") as configfile:
    config.write(configfile)