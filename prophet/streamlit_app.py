import pandas as pd
from fbprophet import Prophet
import time

df = pd.read_csv('example_wp_log_peyton_manning.csv')

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
start = time.time()
forecast = m.predict(future)
end = time.time()

print(f"Elapsed time: {end - start}")