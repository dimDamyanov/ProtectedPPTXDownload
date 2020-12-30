from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import json
import shutil

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)


def get_slide_images(p_url, index):
    driver.get(p_url)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ndfHFb-c4YZDc-cYSp0e-DARUcf')))
    slides = driver.find_elements_by_class_name('ndfHFb-c4YZDc-cYSp0e-DARUcf')
    js = "document.getElementsByClassName('ndfHFb-c4YZDc-q77wGc')[0].remove();"
    driver.execute_script(js)
    os.mkdir(f'output/p{index+1}')
    for ind, slide in enumerate(slides):
        with open(f'output/p{index+1}/slide{ind + 1}.png', 'wb') as outfile:
            WebDriverWait(slide, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ndfHFb-c4YZDc-cYSp0e-DARUcf-PLDbbf')))
            outfile.write(slide.screenshot_as_png)
    slides[1].screenshot(f'output/p{index+1}/slide2.png')


try:
    shutil.rmtree('output')
except OSError:
    pass
os.mkdir('output')
with open('data.json', 'r') as infile:
    urls = json.load(infile)

for ind, url in enumerate(urls):
    get_slide_images(url, ind)