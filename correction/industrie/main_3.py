import plush_plant
import google 
import csv
import requests
import time 
import re 

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

def get_line_consumption(line, plant):
    ret = plant.send_cmd(f"show line power consumption -l {line}")
    line_power = re.search(r'\s(\d+)mWh',ret).group(1)
    return line_power

def toggle_line_and_check_it(action, plant, line):
    print(plant.send_cmd(f"{action} line -u {line}"))
    print(plant.send_cmd(f"show line -l {line}"))

def determine_line(objective, lines_consumption, available_power, minimal_power):
    line_to_activate = []
    available_line = [item for item in objective]

    while (available_power >= int(minimal_power)) and available_line != []:
        prior_candidate = ""
        for key in available_line:
            if int(lines_consumption[key]) <= available_power:
                if prior_candidate == "" or int(objective[prior_candidate]) > int(objective[key]):
                    prior_candidate = key
        if prior_candidate == "":
            break

        line_to_activate.append(prior_candidate)
        available_line.remove(prior_candidate)
        available_power = available_power - int(lines_consumption[prior_candidate])

    return (line_to_activate)


if __name__ == '__main__':
    objective = {'corgi':2, 'akita':3,'tibetan_mastiff':1, 'shiba':1, 'husky':2}
    objective_status = {'corgi':"nok", 'akita':"nok",'tibetan_mastiff':"nok", 'shiba':"nok", 'husky':"nok"}
    plant = plush_plant.PlushPlant()
    objective_reach = False
    lines_consumption = {}
    minimal_power = 0
    
    for key in objective:
        line_consumption = int(get_line_consumption(key, plant))
        lines_consumption[key] = line_consumption
        if minimal_power == 0 or minimal_power > line_consumption:
            minimal_power = line_consumption


    print("consommation électrique de chaque ligne :")
    print("         ", lines_consumption)
    print("puisance minimal nécessaire : ", minimal_power, "mWh")

    while not objective_reach:
        print("-------------------------------------------------------")
        pw = get_electric_power('cote armor', 'energie-eoliens.csv')
        print("Puissance éolienne disponible : ",pw,"Mwh")

        minimal_power = min([lines_consumption[x] for x in lines_consumption])
        print("puissance minimum nécessaire :", minimal_power)
        lines_to_control = determine_line(objective, lines_consumption, int(pw), minimal_power)
        if lines_to_control != []:
            print("ligne à activer :", lines_to_control)
        else:
            print("puissance éolienne trop faible")

        for line in lines_to_control:
            toggle_line_and_check_it("activate", plant, line)
        time.sleep(1)


        for line in lines_to_control:
            toggle_line_and_check_it("deactivate", plant, line)
            objective[line] = objective[line] - 1
            if objective[line] == 0:
                objective_status[line] = "OK - DONE"
                del objective[line]
                del lines_consumption[line]
        if objective == {}:
            objective_reach = True
        print(objective_status)
        print("-------------------------------------------------------")
    
    print("""
                /\_/\                  
               /  @ @   Woof! 
               \    <>              _  
                |  _/\------____ ((| |))
                |               `--' |   
            ____|_       ___|   |___.' 
            /_/_____/____/_______|
    
    """)