def time():
    while(0 == 0):
        from datetime import datetime
        week = ""
        day = datetime.today().weekday()
        if day == 0:
            week = "星期一"

        if day == 1:
            week = "星期二"

        if day == 2:
            week = "星期三"
            
        if day == 3:
            week = "星期四"
            
        if day == 4:
            week = "星期五"
            
        if day == 5:
            week = "星期六"

        if day == 6:
            week = "星期日"

        import datetime
        Date_and_time =  datetime.datetime.now()
        
        print("今天是:" + str(Date_and_time) + " " + str(week), end='\r')

time()