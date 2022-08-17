import pandas as pd
from datetime import date
import Data_fetcher

date1 = Data_fetcher.start_date  # start date
today = date.today()  # end date

month_list = [i.strftime("%b-%y") for i in pd.date_range(start=date1, end=today, freq='MS')]

if __name__ == '__main__':
    print(len(month_list))