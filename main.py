import requests
import json
# ZJU低分定点选课选课脚本 v1.0 by：Tenderness
# 免责声明：本脚本仅供内部学习研究使用，请勿将其用作任何违法用途，否则后果自负，作者将不为其承担任何法律责任，下载后请24h内删除  
# 本脚本使用API均为开放API，权限与正常选课没有区别，唯一用途仅为代替人力，请勿盲目自信自己的运气

#使用前请先安装python3和requests模块，推荐使用python3.75及以上版本运行
#requests安装：pip3 install requests (pip install requests)

# url无需修改，这个url不需要内网
url = "http://zdbk.zju.edu.cn/jwglxt/xsxk/zzxkghb_xkBcZyZzxkGhb.html"

# params改成自己的学号，gnmkdm应该是功能模块代码？似乎与学校有关？ZJU应该所有人都是N253530，不用改
params = "gnmkdm=N253530&su=31X010XXXX"

data = {
    "xn": "2019-2020",  # 学年
    "xq": "2",  # 学期，猜测1是秋冬，2是春夏
    "nj": "201X",  # 年级
    "xkkh": "(2019-2020-2)-21120491-0096205-1",  # 课号
    "tabname": "xkrw2006view",  # 未知，但不用改
    "xkzys": "3",  # 选课专业数？疑似是优先级排序？不用改
}

# cookie换成自己的cookie，一般一个cookie很长时间都不会失效（教务网的迷幻操作）
# 如果失效了就更新一次cookie
# 注意：请不要泄漏自己的cookie，这是非常危险的行为
headers = {
    "cookie": "JSESSIONID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX; route=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

# 下面都不用改
if __name__ == "__main__":
    while(True):
        req = requests.post(url=url, params=params, data=data, headers=headers)
        res = json.loads(req.text)
        print(res)
        if (res['flag'] == '1'):
            print('哈哈哈，选课成功！不用退学了')
            break
        if (res['msg'] == '上课时间冲突！0'):
            print('这个时间段似乎课表已经有课了！')
            break
        if (res['msg'] == '人数超过限制！'):
            continue
        if (res['flag'] == '0'):
            print('啊哦，发生了意外情况，请检查课表情况')
            break
