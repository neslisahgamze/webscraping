from bs4 import BeautifulSoup
import requests

url = "http://www.hepsiburada.com/asus-r510vx-dm508t-intel-core-i7-6700hq-2-6ghz-3-5ghz-8gb-1tb-gtx950m-15-6-fhd-tasinabilir-bilgisayar-p-HBV000004FYEO"
url2= " http://www.hepsiburada.com/asus-n552vw-fw171t-intel-core-i7-6700hq-16gb-1tb-hdd-128gb-ssd-gtx960m-windows-10-home-15-6-fhd-tasinabilir-bilgisayar-p-HBV000001FZ6Z"

url_list = [url, url2]

for i in url_list:
    results = requests.get(i)
    soup = BeautifulSoup(results.content, 'html.parser')
    soup2=soup.find("span", {"id": "offering-price"}).find_next("span").text
    print(soup2)
