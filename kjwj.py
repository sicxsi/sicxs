# name: 科技玩家
# Author: sicxs
# Date: 2024-11-4
# export kjwj="authorization" @,&分割 不需要 Bearer 
# cron: 15 8 * * *
# new Env('科技玩家');
import requests
import re,os,sys,json,time


def getUserInfo(authorization):#我的信息
    url = "https://www.kejiwanjia.net/wp-json/b2/v1/getUserInfo"
    header = {
     "authority": "www.kejiwanjia.net",
     "method": "POST",
     "path": "/wp-json/b2/v1/getUserInfo",
     "scheme": "https",
     "authorization": f"Bearer {authorization}",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
     "origin": "https://www.kejiwanjia.net",
     "referer": "https://www.kejiwanjia.net/",
       }
    try:
        response = requests.post(url=url,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        print(f"用户名: {info['user_data']['name']}")
        time.sleep(3)
        getUserMission(authorization)
        time.sleep(5)
        userMission(authorization)  
    except Exception as e:
          print(e)

def getGoldList(authorization):#积分查询
    url = "https://www.kejiwanjia.net/wp-json/b2/v1/getGoldList"
    header = {
     "authority": "www.kejiwanjia.net",
     "method": "POST",
     "path": "/wp-json/b2/v1/getGoldList",
     "scheme": "https",
     "authorization": f"Bearer {authorization}",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
     "origin": "https://www.kejiwanjia.net",
     "referer": "https://www.kejiwanjia.net/",
        }
    try:
        response = requests.post(url=url,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        print(f"最近一次签到：{info['data'][0]['date']},获得积分；{info['data'][0]['no']},总积分：{info['data'][0]['total']}")
    except Exception as e:
          print(e)

def getUserMission(authorization):#更新签到
    url = "https://www.kejiwanjia.net/wp-json/b2/v1/getUserMission"
    header = {
     "authority": "www.kejiwanjia.net",
     "method": "POST",
     "path": "/wp-json/b2/v1/getUserMission",
     "scheme": "https",
     "authorization": f"Bearer {authorization}",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
     "origin": "https://www.kejiwanjia.net",
     "referer": "https://www.kejiwanjia.net/",
        }
    try:
        response = requests.post(url=url,headers=header)
        s1 = response.status_code 
        if 200 ==s1:
            print("正在初始签到，请稍等。")
    except Exception as e:
          print(e)
def userMission(authorization): #签到
    url = "https://www.kejiwanjia.net/wp-json/b2/v1/userMission"
    header = {
     "authority": "www.kejiwanjia.net",
     "method": "POST",
     "path": "/wp-json/b2/v1/userMission",
     "scheme": "https",
     "authorization": f"Bearer {authorization}",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
     "origin": "https://www.kejiwanjia.net",
     "referer": "https://www.kejiwanjia.net/",
        }
    try:
        response = requests.post(url=url,headers=header)
        response.encoding = "utf-8"
        info = json.loads(response.text)
        if "message" in  info :
          print("你的authorization可能过期了，请检查。")
        elif "credit" in info:
          print(f"恭喜您，签到获得,{info['credit']}积分")
          time.sleep(5)
          getGoldList(authorization)
        else:
            print("请勿重复签到")
            time.sleep(5)
           # getGoldList(authorization)  
         #print(f"最近一次签到：{info['data'][0]['date']},获得积分；{info['data'][0]['no']},总积分：{info['data'][0]['total']}")
    except Exception as e:
          print(e)

def sicxs():
    if os.environ.get("kjwj"):
        ck = os.environ.get("kjwj")
    else:
        ck = ""
        if ck == "":
            print("请设置变量")

            sys.exit()

    ck_run = re.split(r'&|@|\n',ck)

    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 账号【{i + 1}/{len(ck_run)}】执行 -----------')
        try:
            
            getUserInfo(ck_run_n)
        except Exception as e:
            print(e)

    print(f'\n-----------  执 行  结 束 -----------')
 
if __name__ == '__main__':
  sicxs()