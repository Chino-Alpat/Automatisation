import requests

url= 'http://localhost:3001/'


def get_temp_from_room(room):
    thermostat_list = requests.get(url + '/thermostat_list').json()
    temperature_list = []

    try:
        room_id = [item['id'] for item in thermostat_list if room in item['name']]
    except:
        print("there is no room : " + room )
        return "error"
    for id_to_check in room_id:
        temp = requests.get(f"{url}/thermostat_temp", params={'id': id_to_check}).json()
        temperature_list.append(temp)
    return temperature_list


if __name__ == '__main__':
    print('De quelle pièce de la maison souhaitez vous connaitre la temperature ?:')
    room = input()
    temps = get_temp_from_room(room)
    if temps != "error":
        print('La temperature de la pièce :')
        for temp in temps:
            print(temp)
    else:
        print("il n'y a pas de pièce : " + room )

