from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Opretter en webdriver
driver = webdriver.Chrome()

# Åbner webapplikationen
driver.get("file:///C:/Users/John%20Mayer/source/repos/Webcams%20jan%202023/index.html")
try:
    # Test 1: Tilføjelse af et nyt webcam
    new_webcam_data = {"Id": "6", "Brand": "TestBrand", "Height": "720", "Width": "1280"}

    # Find inputfelterne og indtast værdierne for det nye webcam
    id_input = driver.find_element_by_xpath("//input[@placeholder='Id']")
    brand_input = driver.find_element_by_xpath("//input[@placeholder='Brand']")
    height_input = driver.find_element_by_xpath("//input[@placeholder='Height']")
    width_input = driver.find_element_by_xpath("//input[@placeholder='Width']")

    id_input.send_keys(new_webcam_data["Id"])
    brand_input.send_keys(new_webcam_data["Brand"])
    height_input.send_keys(new_webcam_data["Height"])
    width_input.send_keys(new_webcam_data["Width"])

    # Klik på knappen for at tilføje det nye webcam
    add_button = driver.find_element_by_xpath("//button[contains(text(), 'Add Webcam')]")
    add_button.click()

    # Vent på at det nye webcam bliver tilføjet til tabellen
    time.sleep(2)

    # Bekræft at det nye webcam er tilføjet ved at finde det i tabellen
    new_webcam_row = driver.find_element_by_xpath(f"//tr[contains(text(), '{new_webcam_data['Id']}')]")
    assert new_webcam_row is not None, "Test 1: Tilføjelse af nyt webcam fejlede"

    print("Test 1: Tilføjelse af nyt webcam gennemført succesfuldt")

    # Test 2: Sletning af et eksisterende webcam
    # Find slet-knappen for det første webcam i tabellen og klik på den
    delete_button = driver.find_element_by_xpath("//tr[1]//button[contains(text(), 'Delete')]")
    delete_button.click()

    # Vent på at det første webcam bliver slettet fra tabellen
    time.sleep(2)

    # Bekræft at det første webcam ikke længere er til stede i tabellen
    first_webcam_row = driver.find_elements_by_xpath("//tbody/tr")[0]
    assert "1" not in first_webcam_row.text, "Test 2: Sletning af eksisterende webcam fejlede"

    print("Test 2: Sletning af eksisterende webcam gennemført succesfuldt")

finally:
    # Lukker browseren
    driver.quit()
