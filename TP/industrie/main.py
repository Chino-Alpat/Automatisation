import plush_plant
import google 

if __name__ == '__main__':
    plant = plush_plant.PlushPlant()
    print(plant.send_cmd("show all"))