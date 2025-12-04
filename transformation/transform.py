import pandas as pd
from utilities.utility import clean_data_and_create_sub_tables as table_creator

def transform_data(raw_data):
    ## Drop missing customer_id and order_id
    raw_data.dropna( subset=['Order_ID', 'Customer_ID'], inplace=True )

    ## convert order date to datetime
    raw_data['Order_Date'] = pd.to_datetime( raw_data['Order_Date'], format='mixed')
    
    ## create tables
    customer_df = table_creator(raw_data, ['Customer_ID', 'Customer_Name', 'Email', 'Phone_Number'])
    product_df = table_creator(raw_data, ['Product_ID', 'Product_Name', 'Brand', 'Category', 'Price'])
    orders_df = table_creator(raw_data, ['Order_ID', 'Customer_ID', 'Product_ID', 'Quantity', 'Order_Date'])
    payment_df = table_creator(raw_data, ['Order_ID', 'Payment_Method', 'Transaction_Status', 'Total_Price'])
    shipping_df = table_creator(raw_data, ['Shipping_Address', 'City', 'State', 'Country', 'Postal_Code'])
    #add shipping id using index. make shipping id first column
    shipping_df['Shipping_ID'] = shipping_df.index + 1
    shipping_df = shipping_df[
        ['Shipping_ID', 'Shipping_Address', 'City', 'State', 'Country', 'Postal_Code']
    ]
    
    return customer_df, product_df, orders_df, payment_df, shipping_df