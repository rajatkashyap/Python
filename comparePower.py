import requests
from bs4 import BeautifulSoup
r=requests.get('https://comparepower.com/compare/pricing/77459?u=9&g=0')
r1=requests.get('https://www.chooseenergy.com/shop/residential/electricity/TX/77459/centerpoint-energy-tx-electricity/')
soup = BeautifulSoup(r.content)
soup.find_all("a")
for l in soup.find_all("a"):
    print l.text, l.get("href")

data=soup.find_all("div",{"class":"plan"})

for item in data:
    print item.text

for item in data:
    print item.contents[2].find_all("a",{"class":"plan_PricePer1000"})

for item in data:
    print item.contents[1].find_all("a", {"class": "plan_PricePer1000 hidden"})[0].text
    print item.contents[7].find_all("div", {"class": "provider_img"})[0].text
    print item.contents[7].find("img")['alt']
    print item.contents[1].find_all("a", {"class": "plan_PricePer1000 hidden"}) [0].text


data1=soup.find_all("Pricing.Results")

r1=requests.get('https://www.chooseenergy.com/shop/residential/electricity/TX/77459/centerpoint-energy-tx-electricity/')
soup1 = BeautifulSoup(r1.content)
data1=soup1.find_all("div",{"class":"plan-overview"})

script = soup.find('script', text=lambda x:'PricePer1000' in x)
match = re.search(r'Provider = "(.*?)",', script.text)

data_s = soup.find_all("script")
print data_s[-1].text


match = re.search(r'"PricePer1000":\d+', data_s[-1].text)

match = re.search(r'"PricePer1000":\d+\.\d+', data_s[-1].text)

match_price = re.findall(r'"PricePer1000":(\d+\.\d+)', data_s[-1].text)

match_provider = re.findall(r'"Provider":"(.*?)"', data_s[-1].text)

match_plan = re.findall(r'"Description":"(.*?)"', data_s[-1].text)

match_termLength = re.findall(r'"TermLength":\d+', data_s[-1].text)


for i in range(len(match_termLength)):
    print match_termLength[i]

zipcodes=[77001, 77002, 77003, 77004, 77005, 77006, 77007, 77008, 77009, 77010, 77011, 77012, 77013, 77014, 77015, 77016, 77017, 77018, 77019, 77020, 77021, 77022, 77023, 77024, 77025, 77026, 77027, 77028, 77029, 77030, 77031, 77032, 77033, 77034, 77037, 77080, 77072, 77073, 77074, 77075, 77076, 77077, 77071, 77079, 77066, 77081, 77082, 77083, 77078, 77070, 77069, 77067, 77065, 77064, 77063, 77062, 77061, 77060, 77059, 77058, 77208, 77084, 77068, 77098, 77213, 77212, 77210, 77209, 77035, 77207, 77057, 77205, 77204, 77203, 77202, 77206, 77099, 77085, 77097, 77096, 77095, 77094, 77093, 77092, 77091, 77090, 77089, 77088, 77087, 77086, 77201, 77015, 77041, 77055, 77054, 77053, 77052, 77051, 77050, 77049, 77048, 77047, 77046, 77045, 77044, 77027, 77042, 77028, 77040, 77039, 77038, 77216, 77036, 77217, 77034, 77033, 77032, 77031, 77030, 77056, 77043, 77267, 77256, 77274, 77273, 77272, 77271, 77270, 77277, 77268, 77279, 77266, 77265, 77263, 77262, 77259, 77257, 77269, 77289, 77215, 77299, 77298, 77297, 77293, 77292, 77275, 77290, 77258, 77288, 77287, 77284, 77282, 77281, 77280, 77291, 77225, 77255, 77233, 77261, 77230, 77229, 77228, 77235, 77226, 77234, 77224, 77223, 77222, 77221, 77220, 77219, 77218, 77227, 77250, 77254, 77253, 77252, 77231, 77251, 77236, 77249, 77248, 77245, 77244, 77243, 77242, 77241, 77240, 77238, 77237,77385, 77301, 77302, 77303, 77304, 77305, 77306, 77384,77355,77546, 77549,77008,77024,77346, 77347, 77345, 77396, 77338, 77325, 77339,77040,
77492, 77493, 77491, 77450, 77449, 77494,77325, 77339, 77345, 77346,77379, 77389, 77391,77573, 77574,77353, 77354, 77355,77024, 77224, 77279,77489, 77459,77356,77501, 77502, 77503, 77504, 77505, 77506, 77507, 77508,77581, 77584, 77588,77024,77406,77471,77036, 77037, 77038, 77039, 77040, 77041, 77042, 77043, 77044, 77045, 77046, 77047, 77048, 77049, 77050, 77051, 77052, 77053, 77054, 77055, 77056, 77058, 77059, 77060, 77061, 77062, 77063, 77064, 77065, 77066, 77067, 77068, 77069, 77070, 77071, 77072, 77073, 77074, 77075, 77076, 77077, 77078, 77079,77373, 77379, 77380, 77381, 77382, 77383, 77386, 77387, 77388, 77389, 77391, 77393,77080, 77081, 77082, 77083, 77084, 77085, 77086, 77087, 77088, 77089, 77090, 77091, 77092, 77093, 77094, 77095, 77096, 77097, 77098, 77099,77024,77477,77478, 77479, 77487, 77496,77380, 77381, 77382, 77387, 77393,77337, 77375, 77377,77005]


import requests
import re
from bs4 import BeautifulSoup
zip=77459
url='https://comparepower.com/compare/pricing/' +str(zip) + '?u=9&g=0'
r=requests.get('https://comparepower.com/compare/pricing/77459?u=9&g=0')
soup = BeautifulSoup(r.content)
data_s = soup.find_all("script")

match_price = re.findall(r'"PricePer1000":(\d+\.\d+)', data_s[-1].text)

match_provider = re.findall(r'"Provider":"(.*?)"', data_s[-1].text)

match_plan = re.findall(r'"Description":"(.*?)"', data_s[-1].text)

match_termLength = re.findall(r'"TermLength":(\d+)', data_s[-1].text)

for i in range(len(match_termLength)):
    print "Provider: %s Plan: %s Price: %s Term Length: %s" %(match_provider[i], match_plan[i], match_price[i], match_termLength[i])



import sqlite3
import datetime
conn = sqlite3.connect('ElecPlans_0923.db')
cur=conn.cursor()
cur.execute("CREATE TABLE ElectrictyPlans (Provider text,Plan text, Price text, TermLength text)")
cur.execute("Insert into ElectrictyPlans values ('dummy','dummy','dummy','dummy')")
dt=datetime.datetime.now().date()

for i in range(len(match_termLength)):
    print "Provider: %s Plan: %s Price: %s Term Length: %s" %(match_provider[i], match_plan[i], match_price[i], match_termLength[i])
    cur.execute("Insert into ElectrictyPlans (Provider ,Plan , Price , TermLength , ExtractDate ) values (?,?,?,?,?)", (match_provider[i], match_plan[i], match_price[i], match_termLength[i], dt))
conn.commit()
cur.execute("Insert into ElectrictyPlans (Provider ,Plan , Price , TermLength ) values (?,?,?,?)", (match_provider[i], match_plan[i], match_price[i], match_termLength[i]))

if match:
    description_html = html.fromstring(unquote(match.group(0)))
    print description_html.text_content()





#***************************************************************************************************

import requests
import re
from bs4 import BeautifulSoup
import sqlite3
import datetime

zipcodes=[77001, 77002, 77003, 77004, 77005, 77006, 77007, 77008, 77009, 77010, 77011, 77012, 77013, 77014, 77015, 77016, 77017, 77018, 77019, 77020, 77021, 77022, 77023, 77024, 77025, 77026, 77027, 77028, 77029, 77030, 77031, 77032, 77033, 77034, 77037, 77080, 77072, 77073, 77074, 77075, 77076, 77077, 77071, 77079, 77066, 77081, 77082, 77083, 77078, 77070, 77069, 77067, 77065, 77064, 77063, 77062, 77061, 77060, 77059, 77058, 77208, 77084, 77068, 77098, 77213, 77212, 77210, 77209, 77035, 77207, 77057, 77205, 77204, 77203, 77202, 77206, 77099, 77085, 77097, 77096, 77095, 77094, 77093, 77092, 77091, 77090, 77089, 77088, 77087, 77086, 77201, 77015, 77041, 77055, 77054, 77053, 77052, 77051, 77050, 77049, 77048, 77047, 77046, 77045, 77044, 77027, 77042, 77028, 77040, 77039, 77038, 77216, 77036, 77217, 77034, 77033, 77032, 77031, 77030, 77056, 77043, 77267, 77256, 77274, 77273, 77272, 77271, 77270, 77277, 77268, 77279, 77266, 77265, 77263, 77262, 77259, 77257, 77269, 77289, 77215, 77299, 77298, 77297, 77293, 77292, 77275, 77290, 77258, 77288, 77287, 77284, 77282, 77281, 77280, 77291, 77225, 77255, 77233, 77261, 77230, 77229, 77228, 77235, 77226, 77234, 77224, 77223, 77222, 77221, 77220, 77219, 77218, 77227, 77250, 77254, 77253, 77252, 77231, 77251, 77236, 77249, 77248, 77245, 77244, 77243, 77242, 77241, 77240, 77238, 77237,77385, 77301, 77302, 77303, 77304, 77305, 77306, 77384,77355,77546, 77549,77008,77024,77346, 77347, 77345, 77396, 77338, 77325, 77339,77040,77492, 77493, 77491, 77450, 77449, 77494,77325, 77339, 77345, 77346,77379, 77389, 77391,77573, 77574,77353, 77354, 77355,77024, 77224, 77279,77489, 77459,77356,77501, 77502, 77503, 77504, 77505, 77506, 77507, 77508,77581, 77584, 77588,77024,77406,77471,77036, 77037, 77038, 77039, 77040, 77041, 77042, 77043, 77044, 77045, 77046, 77047, 77048, 77049, 77050, 77051, 77052, 77053, 77054, 77055, 77056, 77058, 77059, 77060, 77061, 77062, 77063, 77064, 77065, 77066, 77067, 77068, 77069, 77070, 77071, 77072, 77073, 77074, 77075, 77076, 77077, 77078, 77079,77373, 77379, 77380, 77381, 77382, 77383, 77386, 77387, 77388, 77389, 77391, 77393,77080, 77081, 77082, 77083, 77084, 77085, 77086, 77087, 77088, 77089, 77090, 77091, 77092, 77093, 77094, 77095, 77096, 77097, 77098, 77099,77024,77477,77478, 77479, 77487, 77496,77380, 77381, 77382, 77387, 77393,77337, 77375, 77377,77005]
#zipcodes=[77001, 77002, 77003]
conn = sqlite3.connect('ElectricityPlans.db')
cur=conn.cursor()
cur.execute("CREATE TABLE ElectricityPlans (ZipCode text, Provider text,Plan text, Price_500 text,Price_1000 text, Price_2000 text,TermLength text,PercRenewable text, ExtractDate date)")


for zip in zipcodes:
    url = 'https://comparepower.com/compare/pricing/' + str(zip) + '?u=9&g=0'
    r=requests.get(url)
    soup = BeautifulSoup(r.content)
    data_s = soup.find_all("script")

    match_price_1000 = re.findall(r'"PricePer1000":(\d+\.\d+)', data_s[-1].text)
    match_price_500 = re.findall(r'"PricePer500":(\d+\.\d+)', data_s[-1].text)
    match_price_2000 = re.findall(r'"PricePer2000":(\d+\.\d+)', data_s[-1].text)

    match_provider = re.findall(r'"Provider":"(.*?)"', data_s[-1].text)

    match_plan = re.findall(r'"Description":"(.*?)"', data_s[-1].text)

    match_termLength = re.findall(r'"TermLength":(\d+)', data_s[-1].text)

    match_renew = re.findall(r'"PercentRenewable":(\d+\.\d+)', data_s[-1].text)

    dt = datetime.datetime.now().date()

    for i in range(len(match_termLength)):
        cur.execute("Insert into ElectricityPlans (ZipCode, Provider ,Plan , Price_500 , Price_1000 , Price_2000,TermLength , PercRenewable,ExtractDate ) values (?,?,?,?,?,?,?,?,?)",   (zip,match_provider[i], match_plan[i], match_price_500[i],match_price_1000[i], match_price_2000[i],match_termLength[i], match_renew[i],dt))

    conn.commit()


