from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os.path
from easygui import *

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\ItStep_Lessons\\Python\\selenium_python\\dz4\\chromedriver.exe")
wait = WebDriverWait(agent_ghost, 10)
path = os.path.join("", "text1.txt")
path2 = os.path.join("", "text2.txt")
my_list = []
inf = enterbox("Країна відбору вантажу", "Країна відбору", [])
inf2 = enterbox("Місто відбору вантажу", "Місто відбору", [])
inf3 = enterbox("Країна доставки", "Країна доставки", [])
inf4 = enterbox("Місто доставки вантажу", "Місто", [])


agent_ghost.get(url="https://lardi-trans.ua/gruz/")
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-2-input"]')))
space3 = agent_ghost.find_element(By.XPATH, '//*[@id="react-select-2-input"]')
space3.send_keys(inf)
space3.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-4-input"]')))
space1 = agent_ghost.find_element(By.XPATH, '//*[@id="react-select-4-input"]')
space1.send_keys(inf2)
time.sleep(3)
space1.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-6-input"]')))
space2 = agent_ghost.find_element(By.XPATH, '//*[@id="react-select-6-input"]')
space2.send_keys(inf3)
time.sleep(3)
space2.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-8-input"]')))
space4 = agent_ghost.find_element(By.XPATH, '//*[@id="react-select-8-input"]')
space4.send_keys(inf4)
time.sleep(3)
space4.send_keys(Keys.ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="proposal-search"]/div/div[1]/div[3]/div[2]/button/span')))
space5 = agent_ghost.find_element(By.XPATH, '//*[@id="proposal-search"]/div/div[1]/div[3]/div[2]/button/span')
space5.click()
time.sleep(5)

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ps_search-result_data-item')))
space_6 = agent_ghost.find_elements(By.CLASS_NAME, 'ps_search-result_data-item')
for e in space_6:
    my_file = open(path, "w")
    my_file.write(e.text)
    my_file.close()
    my_file = open(path, 'r')
    cheat = my_file.readlines()
    try:
        if [s for s in cheat[6] if s in '1234567890']:
            a = list(cheat[6])
            for element in a:
                if "€" in cheat[6]:
                    if element.isdigit():
                        my_list.append(element)
                        b = "".join(my_list)
                        if int(b) > 500:
                            my_file2 = open(path2, "a")
                            my_file2.write("\n" + e.text + "\n")
                            my_list.clear()
                            my_file2.close()
                else:
                    continue

    except:
        pass
    my_file.close()

agent_ghost.close()
