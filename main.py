#Reading the datas into variables from csv files and cleaning it.
import FileRead
file = "goog_stock.csv"
FR = FileRead.FileRead(file)
df = FR.read()
df = FR.clean(df)

dates = FR.dates
#We create a graph about the stock prices.
import Plot
import matplotlib.pyplot as plt
dates_int = []
for i in range(1, len(dates)+1):
        dates_int.append(i)
screen = Plot.Plot(dates_int, df, 1, len(dates), "stock")
screen.create_graph()
plt.show()


X = df[['Open','High','Low', 'Volume']]

close_price = df[['Close']].values # = y


#Creating training (80%), testing (20%) datas and using them to train the model, evaluating the outcome.
import Model
dates_int = [i for i in range(1,len(dates)+1)]

mymodel = Model.Model(X, close_price, dates_int)
mymodel.train()

input("\nPress enter to close...")
