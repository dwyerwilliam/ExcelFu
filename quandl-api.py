import quandl
quandl.ApiConfig.api_key = 'txDvNGyg7w2YzThKidzk'

#data = quandl.get('EOD/HD', start_date='2017-12-28', end_date='2017-12-28')
data = quandl.get('EOD/HD')
print(data.loc['20130903', ['Close']][0])
print(data)