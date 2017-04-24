import pytz
import pandas as pd
import datetime


class TimeTimestamp(object):

    goal_time = 0.5

    def setup(self):
        self.ts = pd.Timestamp("2016-03-28")  # after DST
        self.tzinfo = pytz.timezone("CET")

    def time_replace(self):
        self.ts.replace(tzinfo=self.tzinfo).replace(tzinfo=None)


