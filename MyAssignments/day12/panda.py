# cred_tran.csv and cust_name.csv, accnum is common. need to read both the data as two different data frame and join both using accnum. find out the agregate sum of transanction.out put is customer name and his total sum of transaction.

import  pandas as pd

txn_df = pd.read_csv(r'D:\Data\Study\data\workspace\rdd-examples-master\data\cred_txn.csv', sep='~')
cust_df = pd.read_csv(r'D:\Data\Study\data\workspace\rdd-examples-master\data\cust_name.csv', sep='~')

txn_cust_df = txn_df.set_index('AccNum').join(cust_df.set_index('AccNum'))
print(txn_cust_df)
print(txn_cust_df.groupby('AccNum')['Amount'].agg('sum'))