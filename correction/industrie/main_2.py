import plush_plant
import google 
import csv
import requests
import time 

url= 'http://localhost:3002/'


def get_wind_force(region):
    wind_force_list = requests.get(url + '/wind_force').json()
    for wind_force in wind_force_list:
        if wind_force['region'] == region:
            return wind_force["beaufort"]
    return "region invalide"

def get_electric_power(region, ref_file):
    wind_force = get_wind_force(region)
    with open(ref_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if (row['region'] == region) and (row['force du vent '] == str(wind_force)):
                return row['puissance']
        return "aucune correspondance"


if __name__ == '__main__':
    print(get_electric_power('cote armor', 'energie-eoliens.csv'), "Mwh")