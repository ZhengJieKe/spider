import requests
import sys
import json
import jsonpath


send_data = sys.argv[1]
send_num = sys.argv[2]

if send_num == "1":
    zh = "zh"
    en = "en"
elif send_num == "2":
    zh = "en"
    en = "zh"

Baidu_FanYi_url = "https://fanyi.baidu.com/basetrans"
Heard = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Mobile Safari/537.36"}
Data = {
    "query": send_data,
    "from": zh,
    "to": en

      }


def main():
    respon = requests.post(Baidu_FanYi_url, data=Data, headers=Heard)
    js_data = json.loads(respon.text)
    dst_data = jsonpath.jsonpath(js_data,"$..dst")

    print("the result:",dst_data[0])






if __name__ == "__main__":

    main()