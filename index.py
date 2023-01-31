# -*- coding: utf-8 -*-
import Checkin , json , time
Config = json.loads(open("./Config.json","r",encoding="utf-8").read())
# Demo for AliYun Fc Code

def handler(event, context):
    for i in Config:
        print(f"{time.ctime()} Checking {i['Nickname']}")
        results = Checkin.Checkin(i["Cookie"])
        Checkin.SendServerChain(i["SeverChain"],results)