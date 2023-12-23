from btree.core.reader_txt import file_reader_txt


def test_file_reader_txt(sample_data):
    # Test reading and processing a sample data file
    path = "sample_data.txt"
    dfs_processed = file_reader_txt(path)

    assert len(dfs_processed) == 1
    df = dfs_processed[0]

    # Check if the dataframe has the expected columns
    expected_columns = [
        'reg_quotes', 'trading_date', 'bdi_id', 'stock_id', 'market_type',
        'company', 'stock_specif', 'forward_market_term_days', 'currency', 'open_price',
        'high_price', 'low_price', 'average_price', 'close_price', 'best_purchase_price',
        'best_sale_price', 'number_trades_stock', 'number_shares_stock', 'volume', 'price_or_amount',
        'price_or_amount_corr_ind', 'maturity_date', 'stock_quotation', 'price_or_amount_points', 'stock_isin_id',
        'stock_distr']
    assert all(column in df.columns for column in expected_columns)

    # # Check data types and transformations
    # assert df["date"].dtype == pd.datetime
    # assert df["price"].dtype == float
    # assert df["volume"].dtype == float
    # assert df["market_value"].dtype == float