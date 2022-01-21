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

search_volume = list(dff.Search_volume)
for i in range (0, len(search_volume)):
    if search_volume[i] == "-":
        search_volume[i] = 0
    search_volume[i] = int(search_volume[i])

organic_rank = list(dff.Organic_rank)
for i in range (0, len(organic_rank)):
    if organic_rank[i] == "-":
        organic_rank[i] = 0
    organic_rank[i] = int(organic_rank[i])

sponsored_rank = list(dff.Sponsored_rank)
for i in range (0, len(sponsored_rank)):
    if sponsored_rank[i] == "-":
        sponsored_rank[i] = 0
    sponsored_rank[i] = int(sponsored_rank[i])

keywords_only_furbo = []
org_rank_only_furbo = []
spons_rank_only_furbo = []
search_volume_only_furbo = []


for i in range(0, len(keywordsf)):
    containes = False
    for j in range(0, len(keywordsp)):
        if keywordsf[i] == keywordsp[j]:
            containes = True
    if containes == False:
        if search_volume[i] > 300:
            if (organic_rank[i] < 10 and organic_rank[i] > 0) or (sponsored_rank[i] > 0 and sponsored_rank[i] < 5):
                keywords_only_furbo.append(keywordsf[i])
                org_rank_only_furbo.append(organic_rank[i])
                spons_rank_only_furbo.append(sponsored_rank[i])
                search_volume_only_furbo.append(search_volume[i])
                cerebro_score_only_furbo.append(search_volume[i])


for volume in search_volume_only_furbo:
    print(volume)
print(len(search_volume_only_furbo))