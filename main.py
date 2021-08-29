import datetime
from getTweets import get_all_tweets


# Analysis the date and fetches the user inputs.
def newAnalysis():
    today_date = datetime.datetime.now()
    print("***************************************************")
    print("Day Before Yesterday was:              ", datetime.date.today() - datetime.timedelta(days=2))
    print("Yesterday was:                         ", datetime.date.today() - datetime.timedelta(days=1))
    print("Today is:                              ", str(today_date).split(' ')[0])
    date_ = input(''' Enter which day's news you are interested in 
         1. Day Before Yesterday 
         2. Yesterday
         3. Today 
         Input : ''')
    print(" PLease wait while we fetch the data ...... ")

    if date_ == '1':
        start_date = datetime.date.today() - datetime.timedelta(days=2)
        end_date = datetime.date.today() - datetime.timedelta(days=1)
    elif date_ == '2':
        start_date = datetime.date.today() - datetime.timedelta(days=1)
        end_date = datetime.date.today()
    else:
        start_date = datetime.date.today()
        end_date = datetime.date.today() + datetime.timedelta(days=1)

    get_all_tweets(start_date, end_date)


if __name__ == '__main__':
    newAnalysis()
