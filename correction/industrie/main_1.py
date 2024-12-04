import plush_plant
import google 

if __name__ == '__main__':
    plant = plush_plant.PlushPlant()
    liste_line = plant.send_cmd("show all").split(" ")
    print("Quelle ligne de production souhaitez vous controler ?", liste_line)
    line_to_control = input()
    print("Quelle action souhaitez vous effectuez ? (1- activer / 2 - désactiver)")
    action = input()
    if action != "1" and action != "2":
        print("Action non supporté")
        exit()
    elif action == "1":
        action = "activate"
    elif action == "2":
        action = "deactivate"

    print(plant.send_cmd(f"{action} line -u {line_to_control}"))
    print(plant.send_cmd(f"show line -l {line_to_control}"))
