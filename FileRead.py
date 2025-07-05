import pandas as pd

class FileRead:
    def __init__(self, file):
        self.file = file
        self.dates = []
        self.close_price = []
    def read(self):
        df = pd.read_csv(self.file)
        string = df.to_string()
        for i in range(0, len(df["Date"])):
            self.dates.append((df["Date"])[i])
            self.close_price.append(df["Close"][i])
        return df
    def clean(self, df):
        df["Date"] = pd.to_datetime(df['Date'],format='mixed')
        df = df.dropna() # Cleaning empty Cells
        df['Volume'] = df['Volume'].str.replace(",","",regex = False)
        return df
    
