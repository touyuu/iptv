import hashlib
import time


class PhoenixShow:

    #凤凰中文 246pcc72, 凤凰资讯 246pin72, 凤凰香港 246phk72
    def __init__(self, rid):
        self.rid = str(rid)

    def get_real_url(self):
        hexString = format(int(time.time()) + 1800, 'x')
        subString = '/live/' + self.rid
        str2 = 'obb9Lxyv5C' + subString + hexString
        
        return 'http://tlive.fengshows.cn' + subString + '.flv?txSecret=' + hashlib.md5(str2.encode('utf-8')).hexdigest() + '&txTime=' + hexString


if __name__ == '__main__':
    r = input('输入凤凰名称：\n')
    s = PhoenixShow(r)
    print(s.get_real_url())