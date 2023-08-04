import requests , time


def Checkin(Cookie:str)->dict:
    return  requests.post("https://glados.rocks/api/user/checkin",headers={"User-Agent":"Mozilla/5.0","Cookie":Cookie,"Origin":"https://glados.rocks"},data={"token":"glados.one"}).json()

def SendServerChain(key,response_json):
    description = "Checkin_Records:"
    for i in response_json["list"]: description += f'{time.strftime("%Y-%M-%D %H:%M",time.localtime(i["time"]/1000))}//'
    requests.post(f"https://sctapi.ftqq.com/{key}.send?title={response_json['message']}&desp={description}")
    return True
