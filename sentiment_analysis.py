from textblob import TextBlob
import pandas as pd

class SentimentAnalyzer:
    def __init__(self, df):
        self.df = df

    def perform_analysis(self):
        column_name = input("Enter the column name for sentiment analysis: ")
        if column_name not in self.df.columns:
            print("Invalid column name.")
            return
        text_data = self.df[column_name]

        sentiments = []
        subjectivities = []
        for text in text_data:
            analysis = TextBlob(str(text))
            sentiments.append(analysis.sentiment.polarity)
            subjectivities.append(analysis.sentiment.subjectivity)
        
        result_df = pd.DataFrame({'Text': text_data, 'Sentiment Polarity': sentiments, 'Subjectivity': subjectivities})
        print(result_df.head())
if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    analyzer = DataAnalyzer(df)
    analyzer.describe_data()  