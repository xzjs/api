from selenium import webdriver
from pyquery import PyQuery as pq
from pymongo import MongoClient
import platform


def start(str):
    city = str
    conn=MongoClient('localhost',27017)
    db=conn.weather
    sysstr=platform.system()
    if sysstr=="Windows":
        driver = webdriver.PhantomJS(executable_path="tool\\phantomjs-windows\\phantomjs.exe")
    else:
        driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs-windows")

    try:
        driver.get("http://e.weather.com.cn/d/index/" + city + ".shtml")
        doc = pq(driver.page_source)
        today={}
        today['update_time'] = doc('.weather-data').text()
        today['weather'] = doc('.weather-tq').text()
        today['tempmax'] = doc('#tempmax').text()
        today['tempmin'] = doc('#tempmin').text()
        today['wind'] = doc('.wea-three01').find('span').text()
        today['pollute'] = doc('.wea-three02').find('span').text()
        today['warning'] = doc('.wea-three03').find('span').text()
        my_set=db.today
        my_set.insert(today)
        # sql = "INSERT INTO `spider`.`today`(`update_time`,`weather`,`tempmax`,`tempmin`,`wind`,`pollute`,`warning`,`city`,`time`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        #     update_time, weather, tempmax, tempmin, wind, pollute, warning, city, time.time())
        #
        # cursor.execute(sql)
        # db.commit()

        # driver.get("http://e.weather.com.cn/d/15days/" + city + ".shtml")
        # doc = pq(driver.page_source)
        # lis = doc('.days-list').find('li')
        # for li in lis.items():
        #     date = li.find(".days-list-top").find('time').text()
        #     pollute = li.find(".days-list-top").find('p').text()
        #     temp = li.find(".days-list-foot").find(".days-wd").text()
        #     weather = li.find(".days-list-foot").find(".days-qingkuang").text()
        #     sql = "INSERT INTO `spider`.`future`(`date`,`pollute`,`temp`,`weather`,`city`,`time`)VALUES('%s','%s','%s','%s','%s','%s')" % (
        #         date, pollute, temp, weather, city, time.time())
        #     # print sql
        #
        #     cursor.execute(sql)
        #     db.commit()
        #
        # driver.get("http://e.weather.com.cn/d/mcy/" + city + ".shtml")
        # doc = pq(driver.page_source)
        # today = doc(".weather-bar-title").text()
        # today = today.split(' ')[0]
        # advice = doc("#datebox").text()
        # sql = "INSERT INTO `spider`.`advice`(`today`,`advice`,`city`,`time`)VALUES('%s','%s','%s','%s')" % (
        #     today, advice, city, time.time())
        # cursor.execute(sql)
        # db.commit()
        #
        # driver.get("http://e.weather.com.cn/d/air/" + city + ".shtml")
        # doc = pq(driver.page_source)
        # dls = doc('dl')
        # l = []
        # for dl in dls.items():
        #     l.append(dl.find('dt').text())
        # sql = "INSERT INTO `spider`.`aqi`(`pm10`,`pm2_5`,`no2`,`so2`,`co`,`o3`,`time`,`city`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        #     l[0], l[1], l[2], l[3], l[4], l[5], time.time(), city)
        # cursor.execute(sql)
        # db.commit()
        # db.close()
        print "true"
        # return True
    except Exception, e:
        db.rollback()
        print Exception, ":", e
        db.close()
        return False

if __name__=='__main__':
    start('101100603')
