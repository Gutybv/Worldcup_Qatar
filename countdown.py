
import time
import datetime

def count():
    end_time = datetime.datetime(2022, 11, 21, 4, 0, 0)
    actual_time = datetime.datetime.now()
    if end_time != actual_time:
        time_left = end_time - actual_time
        days = time_left.days
        hours = time_left.seconds//3600
        minutes = (time_left.seconds//60)%60
        
        return('The World Cup starts in: '
                + str(days) + " days "
                + str(hours) + " hours "
                + str(minutes) + " minutes "
                '#WorldCup #WorldCup2022 #WorldCupQatar')
                # 'يبدأ كأس العالم في'
                # + str(days) + " أيام "
                # + str(hours) + " ساعات "
                # + str(minutes) + " الدقائق "
                # 'Чемпионат мира стартует в'
                # + str(days) + " дни "
                # + str(hours) + " часы "
                # + str(minutes) + " минуты "
                
    else:
        return("The World Cup start! enjoy")
    
    
    
    
count()
    
    
    
    
    
    
    
        
    # def countdown(stop):
    #     while True:
    #         difference = stop - datetime.datetime.now()
    #         count_hours, rem = divmod(difference.seconds, 3600)
    #         count_minutes, count_seconds = divmod(rem, 60)
    #         if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
    #             print("The World Cup start! enjoy")
    #             break
    #         print('The World Cup starts in: '
    #             + str(difference.days) + " day(s) "
    #             + str(count_hours) + " hour(s) "
    #             + str(count_minutes) + " minute(s) "
                
    #             )
    #         time.sleep(1)


    # end_time = datetime.datetime(2022, 11, 21, 4, 0, 0)
    # countdown(end_time)
    
