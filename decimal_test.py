from decimal import Decimal

import pandas as pd
import streamlit as st

d = {'name': ["A", "B", "C"], 'amount': [0.1, 0.2, 0.3]}
df = pd.DataFrame(data=d)
st.write(df)
for col in df:
    if "amount" in col or "eur" in col:
        df[col] = list(df[col])
        df[col] = [Decimal(str(round(i,2))) for i in df[col]]

#Output dataframe
st.write(df)
#Testing Condition
st.write(df['amount'][0]+df['amount'][1]==df['amount'][2])
