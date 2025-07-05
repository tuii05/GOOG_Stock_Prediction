import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import Plot

class Model:
    def __init__(self, x: object, y: object, dates_int: object):
        self.x = x
        self.y = y
        self.y_pred = []
        self.y_test = []
        self.dates_int = dates_int
    def calc(self):
        r2 = r2_score(self.y_test, self.y_pred)
        print("R^2 score = ", r2)
        print("Mean Squared Error = ", mean_squared_error(self.y_test, self.y_pred),"\n")
    def create_table(self):
        y_test_tab = np.array([val[0] for val in self.y_test])
        y_pred_tab = np.array([val[0] for val in self.y_pred])
        rel_change = []
        for i in range(0, len(y_test_tab)):
            rel_change.append((y_test_tab[i]/y_pred_tab[i]-1)*100)
        print("Data Evaluation \n---------------")
        table = pd.DataFrame({'Actual Close Price($)':y_test_tab, 'Predicted Close Price ($)':y_pred_tab, 'Relative Change (%)':rel_change})
        print(table)
    #Confusion Matrix (not needed right now)
    #def create_cm(self):
        #actual_norm = np.array([val[0] for val in self.y_test])
        #threshold = np.mean(actual_norm)
        #actual_norm = [1 if i >= threshold else 0 for i in actual_norm]
        #pred_norm = np.array([val[0] for val in self.y_pred])
        #pred_norm = [1 if i >= threshold else 0 for i in pred_norm]
        #confusion_matrix = metrics.confusion_matrix(actual_norm,pred_norm)
        #cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix)
        #cm_display.plot(cmap="Blues")
        #fig = plt.gcf()
        #fig.canvas.manager.set_window_title("Confusion Matrix of Evaluated Data")
        #cm_display.ax_.set_xlabel("")
        #cm_display.ax_.set_ylabel("")
        #plt.show()
        #print("\n")
        #print("Accuracy = ", metrics.accuracy_score(actual_norm,pred_norm))
        #print("Precision = ", metrics.precision_score(actual_norm, pred_norm))
        #print("Sensitivity = ", metrics.recall_score(actual_norm, pred_norm))
    def evaluate_data(self):
        #Calculating accuracy, R2, MSE
        self.calc()
        #Creating a table to compare tested vs predicted datas.
        self.create_table()
    def plot(self, x_test):
        y_test_tab = np.array([val[0] for val in self.y_test])
        y_pred_tab = np.array([val[0] for val in self.y_pred])
        x_test_tab = np.array([val[0] for val in x_test])
        y = [y_test_tab,y_pred_tab]
        screen = Plot.Plot(self.dates_int,y,self.dates_int[int(len(self.dates_int)*0.8):],len(self.dates_int), "vs")
        screen.create_graph()
        plt.show()
    def train(self):
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size = 0.2, random_state = 0)
        regr = linear_model.LinearRegression()
        mymodel = regr.fit(x_train, y_train)
        self.y_test = y_test
        self.y_pred = regr.predict(x_test)
        self.plot(x_test)
        self.evaluate_data()
        
        
