import csv
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas

critique_moi = {}
critique_michel = {}
critique_global = {}
url = "file:///D:/Users/leo.sarreau/Desktop/formation/automatisation%20de%20test/TP_vscode/informatique/mon-site-cinema.html"
fichier_michel = "film-de-michel.csv"


def click_and_wait(browser, path, wait):
    elmt_to_click = browser.find_element(By.XPATH, path)
    if elmt_to_click is not None:
        elmt_to_click.click()
        time.sleep(wait)
        return True
    else:
        print("can't find element", path)
        return False

def turn_table_in_dict(browser, path):
    print("lecture note de moi")
    html_dict = {}
    rows = 1+len(driver.find_elements(By.XPATH, path + "/tbody/tr")) 
    cols = len(driver.find_elements(By.XPATH,path + "/tbody/tr[1]/td")) 
    for r in range(2, rows): 
        film = driver.find_element(By.XPATH, path + "/tbody/tr["+str(r)+"]/td[2]").text
        real = driver.find_element(By.XPATH, path + "/tbody/tr["+str(r)+"]/td[3]").text
        note = len(driver.find_elements(By.XPATH, path + "/tbody/tr["+str(r)+"]/td[5]/img"))
        html_dict[film] = {"réalisateur": real,"note": note}
    return html_dict

def get_info_csv(fichier_csv):
    print("lecture note de michel")
    csv_dict = {}
    with open(fichier_michel, newline='', encoding='utf-8') as csvfile:
       reader = csv.DictReader(csvfile, delimiter=';')
       for row in reader:
           csv_dict[row['Titre']] = {"réalisateur": row['Réalisateur'],"note": row['note']}
    return csv_dict

def merge_json(dict1, dict2):
    merge_dict = {} 
    for key in dict1:
        print(key)
        for key2 in dict2:
            if key.strip("éèà'° :") == key2.strip("éèà'° "):
                print("Critique moi :", dict1[key]["note"])
                print("Critique michel :", dict2[key2]["note"])
                not_moy =  (int(dict1[key]["note"]) + int(dict2[key2]["note"]))/2
                print("Critique moyenne :", not_moy, "\n")
                merge_dict[key] = {"réalisateur": dict1[key]["réalisateur"],"note": not_moy}
    return merge_dict



if __name__ == '__main__':
    action = {"1": {"path": "/html/body/main/section[1]/a", "wait": 3}}
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    click_and_wait(driver, action["1"]["path"], action["1"]["wait"])
    critique_moi = turn_table_in_dict(driver, "//*[@id='mes-notes']")
    critique_michel = get_info_csv(fichier_michel)
    critique_global = merge_json(critique_moi, critique_michel)

    #print(critique_michel)
    #print(critique_moi)
    print(critique_global)
    driver.close()

