import requests
import json

# Исходные данные
list_heroes = ["Hulk", "Captain America", "Thanos"]
token = "2619421814940190"
power = 'intelligence'


# Вводим функцию сравнения
def rate_hero(heroes_list, token, power):
    # Только для этого сайта
    url = "https://superheroapi.com/api"
    search = "/search/"
    power_stats = "/powerstats"
    heroes_dict_for_compare = {}

    # Ищем ID всех героев
    for hero in heroes_list:
        response_for_id = requests.get(url + "/" + token + search + hero)
        id_data = json.loads(response_for_id.content)
        hero_id = id_data["results"][0]['id']

        # Ищем статистику  всех героев
        response_for_power_stats = requests.get(url + "/" + token + "/" + hero_id + power_stats)
        stats = json.loads(response_for_power_stats.content)

        heroes_dict_for_compare[int(stats[power])] = hero

    # Сортируем список
    sorted_heroes_dict = sorted(heroes_dict_for_compare.items())

    # Выводим резельтат сравинения
    for number, hero in enumerate(reversed(sorted_heroes_dict)):
        print(f'{number + 1} place - {hero[1]}, {power} = {hero[0]}')
    pass


# Собственно программа
print(rate_hero(list_heroes, token, power))
