import matplotlib.pyplot as plt
import numpy as np
import numbers

class Plot:
    def __init__(self, x, y, start, end, formattype = None):
        self.dates = x
        self.df = y
        self.start = start
        self.end = end
        self.formattype = formattype
    def format_graph(self,fig, ax):
        ax.tick_params("x", rotation=0)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.yaxis.set_ticks_position("left")
        ax.xaxis.set_ticks_position("bottom")
        ax.set_ylabel("Price ($)")
        ax.set_xlabel("Days [day]")
        #ax.grid()
        ax.set_xticks(np.arange(min(self.dates),max(self.dates)+1))
    def format_stock(self, fig, ax, formattype):
        if(formattype == "stock"):
            colors = {"Open": "#1f77b4","Close": "#ff7f0e","High": "#2ca02c","Low": "#d62728"}
            ax.plot(self.dates,self.df["Open"], color = colors["Open"])
            ax.plot(self.dates,self.df["High"], color = colors["High"])
            ax.plot(self.dates,self.df["Low"], color = colors["Low"])
            ax.plot(self.dates,self.df["Close"], color = colors["Close"])
            #ax.set_title("GOOG Stock Prices: 06/05/2023 - 03/07/2025")
            fig.canvas.manager.set_window_title("GOOG Stock Prices: 06/05/2025 - 03/07/2025")
            ax.legend([])
            ax.text(self.dates[-1]*1.01, self.df["Open"].iloc[-1],"Open",color = colors["Open"],fontweight="bold",horizontalalignment="left",verticalalignment="center")
            ax.text(self.dates[-1]*1.01, self.df["Close"].iloc[-1],"Close",color = colors["Close"],fontweight="bold",horizontalalignment="left",verticalalignment="center")
            ax.text(self.dates[-1]*1.01, self.df["High"].iloc[-1],"High",color = colors["High"],fontweight="bold",horizontalalignment="left",verticalalignment="center")
            ax.text(self.dates[-1]*1.01, self.df["Low"].iloc[-1],"Low",color = colors["Low"],fontweight="bold",horizontalalignment="left",verticalalignment="center")
        elif (formattype == "vs"):
            plt.plot(self.dates[int(len(self.dates)*0.8):],(self.df)[0],"o:k")
            plt.plot(self.dates[int(len(self.dates)*0.8):],(self.df)[1], "o:m")
            #ax.set_title("Actual vs. Predicted Close Price")
            fig.canvas.manager.set_window_title("GOOG Stock Prices: Actual vs. Predicted Close Price [06/27/2025 - 03/07/2025]")
            ax.text(self.dates[-1]*1.01, (self.df)[0][-1],"Actual",color = "k",fontweight="bold",horizontalalignment="left",verticalalignment="center")
            ax.text(self.dates[-1]*1.01, (self.df)[1][-1],"Predicted",color = "m",fontweight="bold",horizontalalignment="left",verticalalignment="center")
    def create_graph(self):
        # Set default parameters
        SIZE_DEFAULT = 16
        plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["font.size"] = SIZE_DEFAULT
        plt.rcParams["axes.titlesize"] = SIZE_DEFAULT
        plt.rcParams["axes.labelsize"] = SIZE_DEFAULT
        plt.rcParams["xtick.labelsize"] = SIZE_DEFAULT
        plt.rcParams["ytick.labelsize"] = SIZE_DEFAULT
        # Create the graph
        fig,ax = plt.subplots(figsize = (10,10))
        # Format the graph
        self.format_graph(fig, ax)
        if self.formattype != None:
            self.format_stock(fig,ax,self.formattype)               


        
