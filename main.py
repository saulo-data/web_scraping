import pandas as pd
import json
from time import sleep
import requests

minute = []
home_xgs = []
away_xgs = []
home_possession = []
away_possession = []
home_goals = []
away_goals = []

url = "https://www.fotmob.com/api/matchDetails"

querystring = {"matchId":"4060610"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.fotmob.com/match/4060610/matchfacts/borussia-dortmund-vs-chelsea",
    "x-fm-req": "eyJib2R5Ijp7ImNvZGUiOjE2NzY0OTM2MTgyMzR9LCJzaWduYXR1cmUiOiIyRDM2N0Q2RjI0ODlGOUVGNTA4QzZBQ0RCNDE0RTI1MiJ9",
    "Connection": "keep-alive",
    "Cookie": "_ga_G0V1WDW9B2=GS1.1.1676490927.15.1.1676493592.15.0.0; _ga=GA1.1.698120331.1674519502; _hjSessionUser_2585474=eyJpZCI6IjVmOGJkZTRmLTljOGMtNWEyZS1iNzA3LTRkNDBlNDRiMjExMyIsImNyZWF0ZWQiOjE2NzQ1MTk1MDIzMTgsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=1de0fca9f0e9128b-2220a67f92da0015:T=1674519503:RT=1674519503:S=ALNI_MYbH37Nn4LPLuxnQ2h3jqmzPGJ-Uw; __gpi=UID=000005783bc7c9af:T=1674519503:RT=1676490928:S=ALNI_MZi-w5NEZSyk9_kcJhPDjVdGGYkFg; g_state={'i_l':0}; CookieConsent=true; _ga_K2ECMCJBFQ=GS1.1.1676490996.7.1.1676493599.0.0.0; _ga_SQ24F7Q7YW=GS1.1.1676490996.7.1.1676493599.0.0.0; u:location=%7B%22countryCode%22%3A%22BR%22%2C%22ccode3%22%3A%22BRA%22%2C%22timezone%22%3A%22America%2FSao_Paulo%22%2C%22ip%22%3A%22179.95.77.53%22%2C%22regionId%22%3A%22PB%22%2C%22regionName%22%3A%22Para%25C3%25ADba%22%7D; _gid=GA1.2.1915860361.1676319436; user=rErSMNYm5ir-m-MqI28-bA.uZZz5-XiKkNnqAt9vLb2TwtMjRzwTvGBHpqcNNEeGrtuX4oJJP7GzV2LYeiaYYNPN6l0NNEOD7xeeVOrH3Y7EPugn8Z2w7KKsN2DfHSqA3VSfeCmEAzXMIAV5aXLdlg7OjxgSvHVSB0lpEGdZGAqXsY-oEL5k1G6xQYEDrFSKDvfRBXxhAxdLn2VfA3Q5L-GZegNEOWq9lDpD3S-TBxTzw9TyJF7eu9NtNlGhn2xh1y_nqGA_oI4i43d_HzkiqFntfWpt1FWrCRDH3_3oh8SeHMGfw5vb83Yr87VFV5YQnTj08HYaxPZTw8siIUBnjRHKN3gY-tkz1NMkBDVB-UqXEi9mgBLcBFkFJy_XNaT0XsXPJRQQhpVp4QcskI5nlzmDhGXx-z-ztaapbMobaVWSV3LQx8aB_MFKDsGrfYI1F0FCijnKuJpoZdbQ27VTG7YWT85LSDmy5TSAL9UOdAM9gwRW49XqCJmgrigfvm5M9Tr1g9yGpLe7vKFcRYUmF3Zce-XtSRukDIBy2xEyxZ82ZneN-YHhj-0zSVricyt6H4XDw2sH6i-hJ-biwS8pNKxt7D-YPbIu-F1eG6PHhAfhbIT6QnOelfkTej9icFgUpTYCf9VBPJkqoOiVobXzmQEtn6aD-Bd7MIQDiW_KElNqk7BYPOQ6hCX41LSXcYbK4BzpmL0OIMpwzssjyPj9g4PVlmcoZm7ZXSH2bZD9NYnnjZbax2ohTdNsGaAaXOyHcERzL0uGIhr2iDozHE-qjRbMY_4635Gjf3f_1qpeap_wI42ZJbUsieXw4F0fJ1DEd9KVMLvmf8dGaIHucAAqQMhppcuTkJ_U26VZiaOhedJjimv2djykmGTgBF-CsjbnuuWRZ069nrug-nQakwrf-vMcYHryHcLNW5qR5cOt0CMcUX11oLIS1fcxXOUgUCimiacfaM8Pvv2wFcvN3ocxh47YXKn7NDEX_AO9qqFRRlJxhQWJmEsSvnr-BVim620kU6lv1pKY0q47GhqKKfkAT8Gte359I4Na6mVavwciiJnGtte3DdiYYLgnZ9saih-r2PFHk5ezZeBbqfjJp7asJjwFbHz46DB51XKEEPOBFnpwNc4qTBOg4-ojKwOO_gKi5Ug_CPumbYVKsMNTe4_ZbJYApZ0CQi_cGizv_3LOw8BkLUSvIAu2M1vgF5YxfsArBnG4BVCGoVVV93g3EF4nABC3EymjDEOjCRTHnL1jd46sEqQ1LpjlRajum0rYegCEtk2DeiJNjYO-pa1gX-TNj0cGwyIa1Bmm0hV8H3ZOTHO8gns_VnDlROxCip9sKcNYpLmyh17Pz6f-SvXq3ktN3QuuZHhPP3-nmezE-KR-ya5m9ElT60fZBoRQaGWuNV1XUgNMdU9_tFwcgGzElgxLHkZco9Q2X68gsjTSd63XZSM8CiqGDh30YeDieCD9WX-OAJ95hZHCCCfqo3SkxKf4OfeAGj2FSxhy9CkalBwXhFba9tm1wBCv--zMRHNJuyb8boZgmwG3GhbAlhb7cuTko9tIbeb4Xg-8jDT6rD11lrMlHP2VKpHcA1kznpWNcNCkRG-iEkbNoU36wmAfxiQydQgq1yDHK5iQOsfUPkmghZ8l9fZhVYqym2JVEFhcrfWVvkR-41cKCOVto7uggqxVbwCV58gJgnmOKa3nsapLMZc53BRH1R9JSbLDETQYYwtEzZtKzP1EU8cPz4HLQJ3MfST-XjEHXWvvWsjmiqrWZtqKsVtHK6bnFwcZrz8whnJgx-n3tkb8pYpyFshjyP-8VZkVapTVvpTh3qDPD-lo2wqQeTh3fFBkpbK_AbOIiH8HLk98LbnJANhaW3viwfUV0synN6b2WhLZGgcAkz9QOnftyz0JeFrzYnTEJJ6jGjxM7KW7vEnkFf-PHgvs1l_w1F-3ZTgR3hOl1WpGT1h7jznfA.1676319446233.2592000000.kEMzRXSMV6GGL2dxsd8C9rtSt5hL6ZBlg-ulGZ1khoI; guser=%7B%22name%22%3A%22Saulo%20Faria%22%2C%22image%22%3A%22https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAEdFTp5_3TphZrsdJFO-oY7L6Emg4Zv7ILv-CsLa5G-Jsg%3Ds96-c%22%2C%22id%22%3A%22105139251330377859466%22%2C%22email%22%3A%22saulo82faria%40gmail.com%22%7D; _hjSession_2585474=eyJpZCI6IjI3MzZlYTBlLWU3M2UtNDIzMC05ZjFlLTFiNDUxODUzM2FlZCIsImNyZWF0ZWQiOjE2NzY0OTA5Mjc1MjQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _hjIncludedInSessionSample_2585474=0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "If-None-Match": "'7clb63lnwt44ii'"
}


while True:
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = json.loads(response.text)
    if data['ongoing'] is not True:
        df = pd.DataFrame({
            'Timestamp': minute,
            'Home Goals': home_goals,
            'Home Possession': home_possession,
            'Home xG': home_xgs,
            'Away Goals': away_goals,
            'Away Possession': away_possession,
            'Away xG': away_xgs
        })
        df.to_csv('match.csv')
        print("Fim de Jogo")
        break
    else:
        timestamp = data['header']['status']['liveTime']['long']
        home_score = data['header']['teams'][0]['score']
        away_score = data['header']['teams'][1]['score']
        home_team = data['general']['homeTeam']['name']
        away_team = data['general']['awayTeam']['name']
        home_pos = data['content']['stats']['stats'][0]['stats'][0]['stats'][0]
        away_pos = data['content']['stats']['stats'][0]['stats'][0]['stats'][1]
        home_xg = data['content']['stats']['stats'][0]['stats'][1]['stats'][0]
        away_xg = data['content']['stats']['stats'][0]['stats'][1]['stats'][1]
        print(
            f'Time: {timestamp} | Scoreline: {home_score} - {away_score}\nxG: {home_team} - {home_xg} | {away_team} - {away_xg} \nPossession (%): {home_team} - {home_pos} | '
            f'{away_team} - {away_pos}\n')
        minute.append(timestamp)
        home_goals.append(home_score)
        away_goals.append(away_score)
        home_xgs.append(home_xg)
        away_xgs.append(away_xg)
        home_possession.append(home_pos)
        away_possession.append(away_pos)
        sleep(60)
        continue
