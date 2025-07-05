## GOOG Stock Price prediction model using ML Regression in Python

The model was created using sklearn built-in regression model from the current data of GOOG Stock. 

The program can be started via `gooogstock_predict.exe`. After running it, it gives out two graphs, one at a time, then the evaluation of the actual and predicted datas. If you want to run the program without the .exe file, you will need to have the following Python libraries installed: `matplotlib`, `pandas`, `numpy` and `sklearn`.

In case you want to try the model out with your own data, please pay attention to the following:

- The file name must be named as `goog_stock`.
- The fileformat should be `.csv`.
- There must be columns with the same name and format as in `goog_stock.csv`. For instance: columns with the name of `Date`, `Open`, `High`, `Low`, `Close`, `Volume` are excepted to be in it.
