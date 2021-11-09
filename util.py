
import numpy as np
import pandas as pd

from prophet import Prophet

import os
import sys

# from https://stackoverflow.com/questions/11130156/suppress-stdout-stderr-print-from-python-functions
class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).

    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])


def CreateTimeSeries(id, df_sale, dates_s, date_columns, window_size):
    item_series =  df_sale[df_sale['id'] == id]
    dates = pd.DataFrame({'ds': dates_s[:window_size]}, index=range(len(dates_s[:window_size])))
    dates['y'] = item_series[date_columns[:window_size]].values.transpose()  
    return dates

# Without holiday
def run_prophet(id, df_sale, dates_s, date_columns, window_size=0):
    w_size = window_size if window_size > 0 else len(date_columns)
    timeserie = CreateTimeSeries(id, df_sale, dates_s, date_columns, w_size)
    model = Prophet(uncertainty_samples=False)
    
    with suppress_stdout_stderr():
        model.fit(timeserie)
    forecast = model.make_future_dataframe(periods=28, include_history=False)
    forecast = model.predict(forecast)
    # return np.append(np.array([id]),forecast['yhat'].values.transpose())
    return forecast

# With holiday
def run_prophet_with_holidays_infomation(id, df_sale, dates_s, date_columns, holidays, window_size=0):
    w_size = window_size if window_size > 0 else len(date_columns)
    timeserie = CreateTimeSeries(id, df_sale, dates_s, date_columns, w_size)
    model = Prophet(
        holidays=holidays,
        uncertainty_samples=False,
        n_changepoints=50,
        changepoint_range=0.8,
        changepoint_prior_scale=0.7
    )
    # changepoint_prior_scale default is 0.5. Increasing it will make the trend more flexible   
    with suppress_stdout_stderr():
        model.fit(timeserie)
    forecast = model.make_future_dataframe(periods=28, include_history=False)
    forecast = model.predict(forecast)
    # return np.append(np.array([id]),forecast['yhat'].values.transpose())
    return forecast