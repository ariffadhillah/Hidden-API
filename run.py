import requests
import pandas as pd

url = "https://www.sunglasshut.com/wcs/resources/plp/10154/byCategoryId/3074457345626651837"

res = []
for x in range(1,16):
    querystring = {"isProductNeeded": "true", "pageSize":"100", "responseFormat":"json", "isChanelCategory": "false", "currency":"USD", "pageView": "image", "viewTaskName": "CategoryDisplayView", "beginIndex":"0", "categoryId":"3074457345626651837", "catalogId":"20602", "langId":"-25", "storeId":"10154", "top":"Y", "orderBy":"default", "currentPage":f"{x}"}

    headers = {
    'Cookie': 'ak_bmsc=71CE855EA7A8E269CF33BC72435140CC~000000000000000000000000000000~YAAQxADARVmDsfp7AQAA5vnN/g2sXHm/0n0MVFz3Ve9iGdyVNpK6OHQQMsZ14XIaH1I7vXCEFib2vdapXhwZjDDj05uPuV9ROhFiibJCImCd7wYtj2M8gMpm5QNLLy9WGkChh99YxDOccsi8t7wRXANp0D4LEV0AaoX8afVF1VgoWKEAcn/zlsaPQ0EFqJDI6GBD+6NrQ8H+zuSMsdLpmksttlxaV7LtHkbjNY4xmfJQhPxZVb0iHaq2/PBZXBXJSb1K32ICFzHnHHVsrhJKZ4PaOL6EleRbfO5GKCLfEhSlgccnt81kJjFikDP1v/tYAe9mS3ildn9FPoPY7TVYpW0pVCjslAKbpZ1meFA6v6SXl53ebgXhZwVctH1fqqvq; bm_sv=41222109CD035F04242022B682033F93~lu7dSolvCqxVAFjm+9d3cqOwktmNn7yJ79giWPSipuCVJRPGatvlIv2DRw+h6QkKolf42MdVNEg36yIakUaKDmg22C5W5+n18PdivO2RuyNrh62OK32/c8OanmUDaY1kov688eGJ2x5FvZHo1m1faGJ5aESUMsgmeXZgqAYwjWE=; JSESSIONID=0000mqrRkNqs1eD6VmmYVXoylqR:1c80pfc7n; TS011f624f=015966d2927a4a862aec27688b57a9972ff033aa663f1c5c0959afe9d1bdb30cf8cb922f414aa46cb20555cb565871dc047c5e020eec6378fea0c8f1575552c5e39ce172a3; aka-cc=US; aka-ct=ASHBURN; aka-zp=20146-20149'
    }

    r = requests.request("GET", url, headers=headers, params=querystring)

    data = r.json()
    for p in data['plpView']['products']['products']['product']:
        res.append(p)

df = pd.json_normalize(res)

df.to_csv('firstresults.csv')

