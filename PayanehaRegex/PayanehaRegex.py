from selenium import webdriver
import re
import time
emptysit = False


options = webdriver.ChromeOptions()
options.page_load_strategy = 'none'
print('Please turn on your VPN and make sure your telegram is connected.')
print('Make sure that you have chrome web driver!')
y = input('enter year:')
m = input('enter month:')
d = input('enter day:') 
global stime
stime = input('enter sleep time (recommand +60):')
global date
date = y + '-' + m + '-' + d

def app():
# Load the webpage
    
    driver = webdriver.Chrome(options=options)
    #changed to baragah.com. because it is easier.
    driver.get('https://bazargah.com/bus-ticket/search/esfahan-to-khansar/%s' %date)

    time.sleep(float(stime))
# Get the page source after it's loaded
    page_source = driver.page_source
    global emptysit
    emptysit = False
# Print or use the page source as needed
    for item in re.findall(r'"FreeChairsNum">(\d+)', page_source):
        if(int(item) > 0):
            emptysit = True
            
    driver.quit()

def call():
    #chat IDs
    ids = ['']
    for id in ids:
        driver = webdriver.Chrome(options=options)
        driver.get('https://api.telegram.org/botTICKET/sendMessage?chat_id=%s&text=bilit%s' %(id, date))
        time.sleep(10)
        driver.quit()

def check ():
    if(emptysit):
        call()
        call()
        call()
    else:
        app()
        check()

check()