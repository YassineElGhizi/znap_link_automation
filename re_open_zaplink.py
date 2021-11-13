import random
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys, os
from selenium.webdriver.common.keys import Keys

start_time = time.time()
once_a_run = True
add_new_page = '//*[@id="create_biolink"]/div/div/div[2]/form/div[3]/button'
slash_link = '//*[@id="create_biolink"]/div/div/div[2]/form/div[2]/div/input'
new_page = '/html/body/main/section/div[3]/div/button'
mail_name = '/html/body/main/div/div/div/div/div/form/div[1]/div/input'
zap_link_login_in_page_url = 'https://app.znaplink.com/login'
password_input = '/html/body/main/div/div/div/div/div/form/div[2]/div/input'
slash_acount_link = '//*[@id="step1_form"]/div[1]/div/input'
log_in = '/html/body/main/div/div/div/div/div/form/div[4]/button'
next_button = '//*[@id="step1_form"]/div[2]/button'
skip_button = '//*[@id="step_form"]/div[6]/button[2]'
add_link = '//*[@id="folders"]/div/div[1]/div[3]/a[2]'
title_input = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[2]/input'
domain_input = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[3]/input'
continue_button = '//*[@id="create_biolink_link"]/div/div/div[2]/form/div[4]/button[1]'
link_disc = '//*[@id="biolink_step2_description"]'
add_link2 = '//*[@id="create_biolink_link_step2"]/div/div/div[2]/form/div[3]/button[2]'

profil = '//*[@id="main_navbar"]/ul/li/a'
log_out = '//*[@id="main_navbar"]/ul/li/div/a[4]'


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
    if not os.path.exists('./re_opened_zaplink_added.txt'):
        with open('./re_opened_zaplink_added.txt' ,  'w' , encoding="utf8") as fl:
            fl.write( str(-1) )
            fl.close()

    if not os.path.exists('./results.txt'):
        open("results.txt", "w" , encoding="utf")

    if not os.path.exists('./xhal_drabna_mn_acount.txt'):
        with open('./xhal_drabna_mn_acount.txt', 'w', encoding="utf8") as fl:
            fl.write(str(-1))
            fl.close()

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

if __name__ == "__main__":
    init()
    with open('./re_opened_zaplink_added.txt' , 'r' , encoding="utf8") as w:
        first_line = int(w.readline())
    with open('./xhal_drabna_mn_acount.txt' , 'r' , encoding="utf8") as t:
        xhal_wsalna = int( t.readline() )

    #params
    max_links = 5
    results_file = './results.txt'
    links_path ='C:\kaz_links.txt'
    heads_path = 'C:\headlines.txt'
    link_desc = 'C:\link_desc.txt'
    slash_links = './slash_links.txt'
    bio_file = './bio.txt'
    #End params

    with open(results_file , 'r' , encoding="utf8") as r:
        acount_list = r.readlines()
        r.seek(0)
        r.close()

    sum_d_slashat = sum(1 for line in open(slash_links))
    num_lines = sum(1 for line in open(links_path))
    print("total link number = {}".format(num_lines))
    khessni_n_log_out_onrj3_nlogi_b_acount_jdid = True
    with open(links_path , 'r' , encoding="utf8") as f:
        for numberlink , link in enumerate(f):
            while True:
                try:
                    for nn , acount in enumerate( acount_list ):
                        dict_acount = dict()
                        if nn <= xhal_wsalna:
                            continue
                        if  nn == len( acount_list ) - 1:
                            print("tsalaw l acounts !!")
                            quit()
                        dict_acount['mail'] = acount.split(" ")[1]
                        dict_acount['password'] = acount.split(" ")[2]
                        break

                    if numberlink == num_lines:
                        break
                    if numberlink <= first_line:
                        print("link NO {} already has been shortlinked".format(numberlink))
                        break

                    print("link NO {}".format(numberlink))

                    if khessni_n_log_out_onrj3_nlogi_b_acount_jdid:
                        # max_acount_count += 1
                        khessni_n_log_out_onrj3_nlogi_b_acount_jdid = False
                        try:
                            driver.quit()
                        except:
                            pass

                        read(heads_path,link_desc,slash_links,bio_file)

                        templates  = []
                        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

                        #log in
                        driver.get(zap_link_login_in_page_url)
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(mail_name).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(mail_name).send_keys(dict_acount['mail'])
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(password_input).send_keys(dict_acount['password'])
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(log_in).click()

                    if once_a_run:
                        tnakt =True
                        while tnakt:
                                for x in range(2 , 99):
                                    try:
                                        driver.find_element_by_xpath('/html/body/main/section/div['+ str(x) +']/div/button').click()
                                        tnakt = False
                                        break
                                    except:
                                        pass

                    sleep(kazian_sleeper())
                    print("once_a_run = {}".format(once_a_run))
                    if once_a_run:
                        we_r_not_good = True
                        while we_r_not_good:
                            for numm, sl in enumerate(slash_links_list):
                                if numm == sum_d_slashat - 1:
                                    print("Profilat TSALAW !!")
                                    quit()
                                if "done-" in sl:
                                    continue
                                tmp_dict = dict()
                                tmp_dict['link'] = sl
                                tmp_dict['i'] = numm
                                driver.find_element_by_xpath(slash_link).click()
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_link).send_keys(Keys.CONTROL, 'a')
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_link).send_keys(Keys.BACKSPACE)
                                sleep(kazian_sleeper())
                                driver.find_element_by_xpath(slash_link).send_keys( tmp_dict['link'] )
                                sleep(kazian_sleeper())
                                try:
                                    driver.find_element_by_xpath(add_new_page).click()
                                except:
                                    pass

                                slash_links_list[tmp_dict['i']] = "done-" + tmp_dict['link']
                                with open(slash_links, 'w', encoding="utf8") as qwe:
                                    qwe.writelines(slash_links_list)
                                    qwe.seek(0)
                                    qwe.close()
                                try:
                                    driver.find_element_by_xpath(slash_link)
                                except:
                                    we_r_not_good = False
                                    once_a_run = False
                                    break

                    add_link_fx(
                        driver,
                        head_list[random.randint(0 , len(head_list) -1)],
                        link,
                        desc_link_list[random.randint(0 , len(desc_link_list) -1)] ,
                    )

                    sleep(kazian_sleeper())

                    with open('./re_opened_zaplink_added.txt' , 'w' , encoding="utf8" ) as state:
                        state.write(str(numberlink))
                        state.close()

                    if (numberlink/max_links).is_integer() and numberlink != 0:
                        once_a_run = True
                        khessni_n_log_out_onrj3_nlogi_b_acount_jdid = True
                        should_i_save_credentials = True
                        driver.find_element_by_xpath(profil).click()
                        sleep(kazian_sleeper())
                        driver.find_element_by_xpath(log_out).click()

                    break

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    with open('./error_re_open_zaplink.txt' , 'a' , encoding="utf") as mi_err:
                        mi_err.write(str(e) + "\n" + str(exc_type) +"\n" + str(exc_obj) + "\n" + str(exc_tb.tb_lineno) + "\n===================\n")
                    print("Something went wrong Repeating again")

    driver.close()
    print("finished in {} min".format( (time.time()-start_time)/60 ))