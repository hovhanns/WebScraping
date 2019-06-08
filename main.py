from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request


def get_images_of_a_lot(lot_url):
    driver = webdriver.Chrome("/Users/hhovhannisya/PycharmProjects/CopartAutoAm/chromedriver")
    driver.get(lot_url)

    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup = BeautifulSoup(res, 'lxml')

    box = soup.find('div', {'id': "small-img-roll"})

    all_imgs = box.find_all('span', {"ng-repeat": "image in thumbNailImages"})

    hd_images = []
    for img in all_imgs:
        hd_images.append(img.find("img")['hd-url'])

    return hd_images


def download_images(img_urls):
    for i in range(len(img_urls)):
        urllib.request.urlretrieve(img_urls[i], str(i) + ".jpg")


url = "https://www.copart.com/lot/31188639"
images_urls = get_images_of_a_lot(url)
download_images(images_urls)



