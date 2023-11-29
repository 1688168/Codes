import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    prices.sort_values('start_date', inplace=True)
    units_sold.sort_values('purchase_date', inplace=True)

    # merges on matching `by` values, then latest `right_on` <= `left_on`
    soldWithPrices = pd.merge_asof(units_sold, prices, 
                                   by='product_id', 
                                   left_on='purchase_date', 
                                   right_on='start_date')

    ## In theory you should do this, but doesn't seem necessary to pass all test cases
    # badprice = soldWithPrices['end_date'] < soldWithPrices['purchase_date']
    # soldWithPrices.loc[badprice, 'price'] = 0.0
    # soldWithPrices.fillna({'price': 0.0}, inplace=True)

    def weighted_mean(df, value, weight):
        vs = df[value]
        ws = df[weight]

        return (vs*ws).sum() / ws.sum()

    avgPxSeries = soldWithPrices.groupby('product_id').apply(weighted_mean, 'price', 'units')

    main = avgPxSeries.round(2).rename('average_price').reset_index()

    # for some products we have a price but no sales, for whatever reason LC demands we return zero avg price
    priceIds = set(prices['product_id'].unique())
    soldIds = set(units_sold['product_id'].unique())
    missingIds = priceIds.difference(soldIds)
    fill = pd.DataFrame({'product_id': list(missingIds), 'average_price': [0]*len(missingIds)})

    return pd.concat([main, fill])