from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='ZIG4W4JU7J4QXF1O', output_format='pandas', indexing_type='date')
data, meta_data = ts.get_daily('GOOGL')
print(data.axes)
print(data.loc["2020-08-21","4. close"][0])
