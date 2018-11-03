import datetime
import time
import sys
import Index_Overview
import XueQiuSpider_Find3Pages


if __name__ == "__main__":
    DATE = input('请输入想要导出的日期（如20181030）：')
    weekday = datetime.datetime(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8])).weekday()
    if weekday == 5 or weekday == 6:
        print('日期不在周一至周五的范围内，程序即将结束。')
        time.sleep(2)
        sys.exit(0)
    else:
        pass

    print('全球市场')
    Stock_ID_CN = '000001.SH,399001.SZ,399006.SZ'
    Stock_ID_List_CN = Stock_ID_CN.split(',')
    Index_Overview.market_overview(Stock_ID_List_CN, DATE)
    Stock_ID_Asia = "N225.GI,KS11.GI,AS51.GI"
    Stock_ID_List_Asia = Stock_ID_Asia.split(',')
    Index_Overview.market_overview(Stock_ID_List_Asia, DATE)

    print('\n成交量')
    Stock_ID_CN = '000001.SH,399001.SZ,399006.SZ'
    Stock_ID_List_CN = Stock_ID_CN.split(',')
    Index_Overview.volume_detector(Stock_ID_List_CN, DATE)

    print('\n宏观策略')
    XueQiuSpider_Find3Pages.get_comment(date=DATE)