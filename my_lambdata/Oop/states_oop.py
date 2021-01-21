# my_lambdata/assignment.py
# OOP APPROACH

import pandas
 # how can
class DataFrameTransformer():
    def __init__(self, df):
        """
        Parameters (df) a DataFrame with a column called "abbrev" that has state affreviations.
        """        
        self.df = df

    def inspect_data(self):
        print(self.df.head())
        
    def add_state_names(self):
        """
        State abbreviation -> Full Name and visa versa.
        FL -> Florida, etc.
        """
        names_map = {
            "CA": "Cali",
            "CO": "Colo",
            "CT": "Conn",
            "DC": "Wash DC",
            "TX": "Texas"
        }
        #breakpoint()
        my_col = self.df["abbrevs"]
        other_col = my_col.map(names_map)
        self.df["state_name"] = other_col

if __name__ == "__main__":

    df = pandas.DataFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})

    transformer = DataFrameTransformer(df)
    transformer.inspect_data()

    transformer.add_state_names()
    transformer.inspect_data()