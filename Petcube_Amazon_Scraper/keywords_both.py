import numpy as np
import pandas as pd


read_data_petcube = pd.read_csv('US_Cerebro_B07QZ4BWY1.csv', encoding="ISO-8859-1")
read_data_furbo = pd.read_csv('US_Cerebro_B01FXC7JWQ.csv', encoding="ISO-8859-1")
framepetcube = [read_data_petcube]
framefurbo = [read_data_furbo]
dfp = pd.concat(framepetcube)
dff = pd.concat(framefurbo)

keywordsf = list(dff.Phrase)
keywordsp = list(dfp.Phrase)

search_volume_furbo = list(dff.Search_volume)
for i in range (0, len(search_volume_furbo)):
    if search_volume_furbo[i] == "-":
        search_volume_furbo[i] = 0
    search_volume_furbo[i] = int(search_volume_furbo[i])

organic_rank_furbo = list(dff.Organic_rank)
for i in range (0, len(organic_rank_furbo)):
    if organic_rank_furbo[i] == "-":
        organic_rank_furbo[i] = 0
    organic_rank_furbo[i] = int(organic_rank_furbo[i])

sponsored_rank_furbo = list(dff.Sponsored_rank)
for i in range (0, len(sponsored_rank_furbo)):
    if sponsored_rank_furbo[i] == "-":
        sponsored_rank_furbo[i] = 0
    sponsored_rank_furbo[i] = int(sponsored_rank_furbo[i])

search_volume_petcube = list(dfp.Search_volume)
for i in range (0, len(search_volume_petcube)):
    if search_volume_petcube[i] == "-":
        search_volume_petcube[i] = 0
    search_volume_petcube[i] = int(search_volume_petcube[i])

organic_rank_petcube = list(dfp.Organic_rank)
for i in range (0, len(organic_rank_petcube)):
    if organic_rank_petcube[i] == "-":
        organic_rank_petcube[i] = 0
    organic_rank_petcube[i] = int(organic_rank_petcube[i])

sponsored_rank_petcube = list(dfp.Sponsored_rank)
for i in range (0, len(sponsored_rank_petcube)):
    if sponsored_rank_petcube[i] == "-":
        sponsored_rank_petcube[i] = 0
    sponsored_rank_petcube[i] = int(sponsored_rank_petcube[i])


keywords_organic = []

for i in range(0, len(keywordsf)):
    for j in range(0, len(keywordsp)):
        if keywordsf[i] == keywordsp[j]:
            if search_volume_furbo[i] > 300:
                if organic_rank_furbo[i] < organic_rank_petcube[j]:
                    keywords_organic.append(organic_rank_petcube[j])


for keyword in keywords_organic:
    print(keyword)
print(len(keywords_organic))