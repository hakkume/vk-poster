import vk_api
from colorama import init
init()
from colorama import Fore, Back, Style
login = input("Введите номер телефона:")
password = input("Введите пароль:")
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()
postik = input("Введи текст который хочешь опубликовать на стене:) :")
print(vk.wall.post(message=postik))
print(Fore.GREEN)
print("Пост успешно опубликован!")
input()