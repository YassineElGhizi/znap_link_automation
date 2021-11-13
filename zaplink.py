import random
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import sys, os

start_time = time.time()
usr_name = '/html/body/main/div/div/div/div/div/form/div[1]/div/input'
tmp_mail = 'https://www.moakt.com'
copy_icon = '//*[@id="copy-email"]'
zap_link_login_in_page_url = 'https://app.znaplink.com/register'
mail_input = '/html/body/main/div/div/div/div/div/form/div[2]/div/input'
password_input = '/html/body/main/div/div/div/div/div/form/div[3]/div/input'
slash_acount_link = '//*[@id="step1_form"]/div[1]/div/input'
register_button = '/html/body/main/div/div/div/div/div/form/div[5]/button'
next_button = '//*[@id="step1_form"]/div[2]/button'
next_button2 = '//*[@id="step_form"]/div[5]/button'
next_button3 = '/html/body/main/div/div/div/div/div[2]/button'
profil_bio = '//*[@id="step_form"]/div[4]/div/input'
skip_button = '//*[@id="step_form"]/div[6]/button[2]'
skip_button2 = '//*[@id="step_form"]/div[5]/button[2]'
remove_pop_up = '//*[@id="new_link_modal"]/div/div/div[1]/button'
trash_icon1 = '/html/body/main/section[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/a[2]'
trash_icon2 = '/html/body/main/section[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/a[2]'
add_link = '//*[@id="folders"]/div[2]/div[1]/div[3]/a[2]'
title_input = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[2]/input'
domain_input = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[3]/input'
continue_button = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[4]/button[1]'
link_disc = '//*[@id="biolink_step2_description"]'
add_link2 = '//*[@id="create_biolink_link_step2"]/div/div/div[2]/form/div[3]/button[2]'
target_link = '//*[@id="link_full_url"]'
profil = '//*[@id="main_navbar"]/ul/li/a'
log_out = '//*[@id="main_navbar"]/ul/li/div/a[4]'
profile_name = '//*[@id="step_form"]/div[3]/div/input'
already_exists_pop_up = '//*[@id="step1_form"]/p'

head_listhead_list = []
desc_link_list = []
slash_links_list = []
bio_list = []

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")


def read(heads_path, desc_link , slah_lyanat ,bio_file):
    global head_list
    global desc_link_list
    global slash_links_list
    global bio_list

    file1 = open(heads_path , 'r' , encoding="utf8")
    Lines = file1.readlines()
    head_list = Lines
    file1.seek(0)
    file1.close()

    file1 = open(desc_link , 'r' , encoding="utf8")
    Lines = file1.readlines()
    desc_link_list = Lines
    file1.seek(0)
    file1.close()

    file1 = open(slah_lyanat , 'r' , encoding="utf8")
    Lines = file1.readlines()
    slash_links_list = Lines
    file1.seek(0)
    file1.close()

    file1 = open(bio_file , 'r' , encoding="utf8")
    Lines = file1.readlines()
    bio_list = Lines
    file1.seek(0)
    file1.close()

def init():
    if not os.path.exists('./zaplink_added.txt'):
        with open('./zaplink_added.txt' ,  'w' , encoding="utf8") as fl:
            fl.write( str(-1) )
            fl.close()

    if not os.path.exists('./results.txt'):
        open("results.txt", "w" , encoding="utf")

def kazian_sleeper():
    ##40 - 70
    ##72min
    if ((time.time() - start_time)/60) > 72.00:
        print("l bot mxa f pause mjebda !")
        sleep( random.randint(40 , 70) )
    return random.randint(2 , 4)
    # return 1

def add_link_fx(driver , title , link , desc):
    driver.find_element_by_xpath(add_link).click()
    sleep(kazian_sleeper())
    driver.find_element_by_xpath(title_input).click()
    sleep(kazian_sleeper())
    driver.find_element_by_xpath(title_input).send_keys(title)
    sleep(kazian_sleeper())
    driver.find_element_by_xpath(domain_input).click()
    sleep(kazian_sleeper())
    driver.find_element_by_xpath(domain_input).send_keys(link)
    sleep(kazian_sleeper())
    try:
        driver.find_element_by_xpath(continue_button).click()
        sleep(kazian_sleeper())
    except:
        pass
    driver.find_element_by_xpath(link_disc).click()
    sleep(kazian_sleeper())
    driver.find_element_by_xpath(link_disc).send_keys(desc)
    sleep(kazian_sleeper())
    try:
        driver.find_element_by_xpath(add_link2).click()
        sleep(kazian_sleeper())
    except:
        pass

def mail_from_tmp_mail(driver):
    print("Obtaining tmp mail...")
    driver.get(tmp_mail)
    driver.find_elements_by_class_name('mail_butt')[0].click()
    mail = driver.find_element_by_id('email-address').text
    pswd = mail
    pswd = pswd.split('@')[0]
    tmp = pswd + "123"
    pswd = tmp
    driver.find_element_by_xpath(copy_icon).click()
    driver.find_element_by_xpath(copy_icon).click()
    sleep(kazian_sleeper())
    print("mail has been created")
    return mail , pswd

if __name__ == "__main__":
    init()
    with open('./zaplink_added.txt' , 'r' , encoding="utf8") as w:
        first_line = int(w.readline())

    #params
    max_links = 5
    results_file = './results.txt'
    links_path ='C:\kaz_links.txt'
    heads_path = 'C:\headlines.txt'
    link_desc = 'C:\link_desc.txt'
    slash_links = './slash_links.txt'
    bio_file = './bio.txt'
    #End params

    max_acount_count = 1
    should_i_save_credentials= True
    c = []
    with open(results_file, 'r', encoding="utf") as qwe:
        for l in qwe:
            c.append(
                int(
                    (l.split(":")[0]).replace("acount", "")
                )
            )
    if len(c) == 0:
        max_acount_count = -1
    else:
        max_acount_count = max(c)

    num_lines = sum(1 for line in open(links_path))
    print("total link number = {}".format(num_lines))
    khessni_ncryi_new_acount = True
    with open(links_path , 'r' , encoding="utf8") as f:
        for numberlink , link in enumerate(f):
            while True:
                try:
                    if numberlink == num_lines:
                        break
                    if numberlink <= first_line:
                        print("link NO {} already has been shortlinked".format(numberlink))
                        break

                    print("link NO {}".format(numberlink))

                    if khessni_ncryi_new_acount:
                        max_acount_count += 1
                        khessni_ncryi_new_acount = False
                        try:
                            driver.quit()
                        except:
                            pass

                        read(heads_path ,link_desc  ,  slash_links , bio_file)

                        templates  = []
                        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

                        #TMP MAIL
                        faker = Faker()
                        usr = faker.name()
                        usr = usr + str( random.randint(1 , 999) )
                        # mail = faker.email()
                        # pswd = "1234567890"

                        mail,pswd= mail_from_tmp_mail(driver)

                        driver.get(zap_link_login_in_page_url)
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(usr_name).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(usr_name).send_keys(usr)
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(mail_input).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(mail_input).send_keys(mail)
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(password_input).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(password_input).send_keys(pswd)
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(register_button).click()
                        sleep(kazian_sleeper())


                        we_r_not_good = True
                        naqaz_ela_had_step = False
                        sum_d_slashat = sum(1 for line in open(slash_links))
                        while we_r_not_good:
                            for numm , sl in enumerate(slash_links_list):
                                if numm == sum_d_slashat-1:
                                    print("Profilat TSALAW !!")
                                    quit()
                                if "done-" in sl:
                                    continue
                                tmp_dict = dict()
                                tmp_dict['link'] = sl
                                tmp_dict['i'] = numm
                                break
                            if not naqaz_ela_had_step:
                                driver.find_element_by_xpath(slash_acount_link).click()
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_acount_link).send_keys(Keys.CONTROL, 'a')
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_acount_link).send_keys(Keys.BACKSPACE)
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_acount_link).send_keys(tmp_dict['link'])
                                sleep(kazian_sleeper())
                            try:
                                driver.find_element_by_xpath(next_button).click()
                                sleep(kazian_sleeper())
                            except:
                                pass

                            if 'Your selected Link URL already exists. Please choose a different one.' in driver.page_source:
                                print('Your selected Link URL already exists. Please choose a different one.')
                                slash_links_list[tmp_dict['i']] = "done-" + tmp_dict['link']
                                with open(slash_links, 'w', encoding="utf8") as qwe:
                                    qwe.writelines(slash_links_list)
                                    qwe.seek(0)
                                    qwe.close()
                            else:
                                driver.find_element_by_xpath(profil_bio).click()
                                sleep(kazian_sleeper())
                                slash_links_list[tmp_dict['i']] = "done-" + tmp_dict['link']
                                with open(slash_links , 'w' , encoding="utf8") as qwe:
                                    qwe.writelines(slash_links_list)
                                    qwe.seek(0)
                                    qwe.close()
                                we_r_not_good = False
                                naqaz_ela_had_step = True


                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(profil_bio).send_keys(bio_list[random.randint(0 , len(bio_list) -1)])
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(next_button2).click()
                        sleep(kazian_sleeper())
                        ##skip create profile
                        driver.find_element_by_xpath('//*[@id="step_form"]/div[6]/button[2]').click()
                        sleep(kazian_sleeper())
                        ##skip socials
                        driver.find_element_by_xpath('//*[@id="step_form"]/div[5]/button[2]').click()
                        sleep(kazian_sleeper())
                        ##skip fav products
                        driver.find_element_by_xpath('//*[@id="step_form"]/div[2]/button[2]').click()
                        sleep(kazian_sleeper())
                        templates = driver.find_elements_by_class_name('theme-selection-indiv')
                        templates[random.randint(1, 10)].click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(next_button3).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(remove_pop_up).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(trash_icon1).click()
                        sleep(kazian_sleeper())
                        wait(driver, 3).until(EC.alert_is_present())
                        alert = driver.switch_to.alert
                        alert.accept()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(trash_icon2).click()
                        sleep(kazian_sleeper())
                        wait(driver, 3).until(EC.alert_is_present())
                        alert = driver.switch_to.alert
                        alert.accept()
                        sleep(kazian_sleeper())
                        page = driver.find_element_by_xpath(target_link).text


                    if should_i_save_credentials:
                        with open(results_file , 'a' , encoding="utf8") as res:
                            res.write('acount' +str((max_acount_count+1))+': ' + str(mail) + " " + str(pswd) + " " + page + "\n" )
                            res.close()
                        should_i_save_credentials = False

                    hessni_ncryi_new_acount = False

                    add_link_fx(
                        driver,
                        head_list[random.randint(0 , len(head_list) -1)],
                        link,
                        desc_link_list[random.randint(0 , len(desc_link_list) -1)] ,
                    )
                    sleep(kazian_sleeper())
                    with open('./zaplink_added.txt' , 'w' , encoding="utf8" ) as state:
                        state.write(str(numberlink))
                        state.close()

                    if (numberlink/max_links).is_integer() and numberlink != 0:
                        khessni_ncryi_new_acount = True
                        should_i_save_credentials = True
                        driver.find_element_by_xpath(profil).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(log_out).click()

                    break

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    with open('./error.txt' , 'a' , encoding="utf") as mi_err:
                        mi_err.write(str(e) + "\n" + str(exc_type) +"\n" + str(exc_obj) + "\n" + str(exc_tb) + "\n===================")
                    print("Something went wrong Repeating again")

    driver.close()
    print("finished in {} min".format( (time.time()-start_time)/60 ))