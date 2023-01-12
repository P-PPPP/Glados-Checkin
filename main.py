import Checkin , json , time , schedule
Config = json.loads(open("./Config.json","r",encoding="utf-8").read())

def Check():
    for i in Config:
        print(f"{time.ctime()} Checking {i['Nickname']}")
        results = Checkin.Checkin(i["Cookie"])
        Checkin.SendServerChain(i["SeverChain"],results)

if __name__ == "__main__":
    schedule.every().day.at("01:20").do(Check)
    while True:
        schedule.run_pending()
        time.sleep(3)
    