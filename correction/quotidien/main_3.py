import requests
import time 

url= 'http://localhost:3001/'


def get_all_room_temp():
    thermostat_list = requests.get(url + '/thermostat_list').json()
    room_list = []
    for thermostat in thermostat_list:
        temp = requests.get(f"{url}/thermostat_temp",params={'id': thermostat['id']}).json()
        thermostat['temperature'] = temp[0]['temperature']
        room_list.append(thermostat)            
    return room_list

def toggle_thermostat(id, change_status):
    response = requests.get(f"{url}/thermostat_toggle",params={'id': id, 'change_status': change_status}).json()
    print("         " + response)

if __name__ == '__main__':
    print('Démarrage régulation automatique')

    for i in range (0,30):
        room_list = get_all_room_temp()
        if room_list != []:
            print(f'température des pièces:')
            for room in room_list:
                print(f"    {room['name']} - {room['id']} - Temperature : {room['temperature']}°")
                if room['temperature'] > 20:
                    toggle_thermostat(room['id'], 'OFF')
                elif room['temperature'] < 17:
                    toggle_thermostat(room['id'], 'ON')

        time.sleep(30)

