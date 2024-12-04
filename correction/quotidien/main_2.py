import requests

url= 'http://localhost:3001/'


def get_all_room_beneath_temp(temp_to_check):
    thermostat_list = requests.get(url + '/thermostat_list').json()
    room_list = []
    for thermostat in thermostat_list:
        temp = requests.get(f"{url}/thermostat_temp",params={'id': thermostat['id']}).json()
        if int(temp[0]['temperature']) < int(temp_to_check):
            thermostat['temperature'] = temp[0]['temperature']
            room_list.append(thermostat)
    return room_list


if __name__ == '__main__':
    print('temperature limite ?:')
    temp_to_check = input()
    room_list = get_all_room_beneath_temp(temp_to_check)
    if room_list != []:
        print(f'Il fait moins de {temp_to_check} degré dans les pièces suivantes:')
        for room in room_list:
            print(f"{room['name']} - {room['id']} - Temperature : {room['temperature']}°")
    else:
        print(f"il fait moint de  {temp_to_check} dans aucune des pièces de la maison")

