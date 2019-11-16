# naive-time-series-forecasting
Predicting tomorrow's weather 
Input data: weather record of the last n days. 0s( no rain) and 1s(rain).
k: number of records (days) to use for producing forecasts
forecast will be 1 if the number of 1s in the previous k time periods is at least k/2. 0 otherwise
OUTPUT: MAE -- mean absolute error = average of |actual - forecast|
