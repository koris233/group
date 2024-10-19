from data_analysis import DataAnalyzer

import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_boxplot(self):
        cat_col = input("Enter categorical column for boxplot: ")
        num_col = input("Enter numeric column for boxplot: ")
        if cat_col in self.df.columns and num_col in self.df.columns:
            self.df.boxplot(column=num_col, by=cat_col)
            plt.title(f'Boxplot of {num_col} by {cat_col}')
            plt.show()
        else:
            print("Invalid columns selected.")

    def plot_scatter(self):
        x_col = input("Enter column for x-axis: ")
        y_col = input("Enter column for y-axis: ")
        if x_col in self.df.columns and y_col in self.df.columns:
            self.df.plot.scatter(x=x_col, y=y_col)
            plt.title(f'Scatter Plot of {y_col} vs {x_col}')
            plt.show()
        else:
            print("Invalid columns selected.")

    def plot_histogram(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        col = input("Enter column for histogram: ")
        if col in numeric_cols:
            self.df[col].plot.hist()
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        else:
            print("Invalid column selection.")
if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    analyzer = DataAnalyzer(df)
    analyzer.describe_data()  