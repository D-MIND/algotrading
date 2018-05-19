import configargparse
from backfill.candles import Candles
from backfill.trades import Trades
import pandas as pd


arg_parser = configargparse.get_argument_parser()
options = arg_parser.parse_known_args()[0]

print(options)
# Trades vs Canldes -> don't know the difference
if options.backfilltrades:
    backfill_client = Trades()
    backfill_client.run()
else:
    backfill_client = Candles()
    backfill_client.run()



# print mongodb collection
print(backfill_client.db_ticker)
print(backfill_client)

# print first 10 canldes of mongodb

# save mongodb to csv
cursor = backfill_client.db_ticker.find({})
df = pd.DataFrame(list(cursor))
df.to_csv('db_BTC_30min_240days.csv')


for document in cursor[:10]:
    print(document, '\n')
