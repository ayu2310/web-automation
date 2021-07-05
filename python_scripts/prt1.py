#data entry automation
import time
from selenium import webdriver
#from proj_1_prt2 import img_to_text

web = webdriver.Chrome()
web.get("https://cyberautics.co.in/login.aspx")  #
#web.find_element_by_xpath('/html/body/header/div/nav/ul/li[6]/a').click()
username = "SKY0038024042"
password = "3pyrLs"
username_path = web.find_element_by_xpath('//*[@id="txtemailid"]')
username_path.send_keys(username)
pass_path = web.find_element_by_xpath('//*[@id="txtpassword"]')
pass_path.send_keys(password)
web.find_element_by_xpath('//*[@id="btnsignUP"]').click()

for i in range(0,160):
    web.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
    web.find_element_by_xpath('//*[@id="frm"]/header/nav/ul/li[2]/div/a[1]').click()

    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    # from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver import ActionChains
    import urllib.request
    import numpy as np
    import cv2
    import pyautogui as pg
    import pyperclip

    # img_path = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Imgquestions"]')
    # right_click =ActionChains(web).context_click(img_path).perform()  #img right click
    # img_address= right_click.Select_by_visible_text('Copy image address')
    # address= web.find_element_by_name('Copy image address').click()

    # pg.rightClick(x=715, y=705)  #right click
    # pg.click(x=823, y=837)   #copy img url
    # url = pyperclip.paste()
    from proj_1_prt2 import img_to_text
    img_path = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Imgquestions"]')
    url = img_path.get_attribute('src')
    #time.sleep(1)


    img_list = img_to_text(url)
    print(img_list)

    if (len(img_list)!=17):
        break
    if (img_list[10] == 'sc'):
        img_list[10] = 'SC'
    if (img_list[14] == 'sc'):
        img_list[14] = 'SC'

    int1 = int(img_list[3])
    int2 = int(img_list[4])
    int3 = int(img_list[6])
    int4 = int(img_list[7])
    int5 = int(img_list[11])

    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtFirstname"]').send_keys(img_list[0])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textLastname"]').send_keys(img_list[1])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textEmailID"]').send_keys(img_list[2].replace(' ',''))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textSSN"]').send_keys(img_list[3].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textphone"]').send_keys(img_list[4].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textBankName"]').send_keys(img_list[5])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textacno"]').send_keys(img_list[6].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textloanamt"]').send_keys(img_list[7].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textAddress"]').send_keys(img_list[8])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textCity"]').send_keys(img_list[9])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textState"]').send_keys(img_list[10])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textzip"]').send_keys(img_list[11].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textdob"]').send_keys(img_list[12].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textLicenceNumber"]').send_keys(img_list[13].replace(' ','').replace('§','5'))
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textLicenceState"]').send_keys(img_list[14])
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_textIP"]').send_keys(img_list[15].replace(' ','').replace('§','5'))
    #time.sleep(1)
    pg.scroll(-400)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSubmit"]').click()

    # //*[@id="ContentPlaceHolder1_txtFirstname"]
    # //*[@id="ContentPlaceHolder1_txtFirstname"]





