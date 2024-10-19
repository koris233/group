from data_analysis import DataAnalyzer
from visualization import DataVisualizer
from sentiment_analysis import SentimentAnalyzer
from utils import load_data

def main():
    print("Welcome to the Laptop Analysis Project!")
    data_path = input("Enter the path to your dataset: ")
    df = load_data(data_path)

    if df is None:
        return

    while True:
        print("\nChoose an option:")
        print("1. Descriptive Statistics")
        print("2. Data Visualization")
        print("3. Sentiment Analysis")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            analyzer = DataAnalyzer(df)
            print("\nChoose a descriptive analysis option:")
            print("1. General Description")
            print("2. Correlation")
            print("3. Standard Deviation")
            print("4. Skewness")
            print("5. Kurtosis")
            print("6. ANOVA Test")
            print("7. t-Test")
            print("8. Chi-square Test")
            analysis_choice = input("Enter your choice: ")
            if analysis_choice == '1':
                analyzer.describe_data()
            elif analysis_choice == '2':
                analyzer.ask_for_correlation()
            elif analysis_choice == '3':
                analyzer.ask_for_standard_deviation()
            elif analysis_choice == '4':
                analyzer.ask_for_skewness()
            elif analysis_choice == '5':
                analyzer.ask_for_kurtosis()
            elif analysis_choice == '6':
                analyzer.perform_anova()
            elif analysis_choice == '7':
                analyzer.perform_t_test()
            elif analysis_choice == '8':
                analyzer.perform_chi_square_test()
            else:
                print("Invalid choice.")
        elif choice == '2':
            visualizer = DataVisualizer(df)
            print("\nChoose a visualization type:")
            print("1. Boxplot")
            print("2. Scatter Plot")
            print("3. Histogram")
            print("4. Q-Q Plot")
            viz_choice = input("Enter your choice: ")
            if viz_choice == '1':
                visualizer.plot_boxplot()
            elif viz_choice == '2':
                visualizer.plot_scatter()
            elif viz_choice == '3':
                visualizer.plot_histogram()
            elif viz_choice == '4':
                analyzer = DataAnalyzer(df)  
                analyzer.plot_qq()
            else:
                print("Invalid choice.")
        elif choice == '3':
            sentiment_analyzer = SentimentAnalyzer(df)
            sentiment_analyzer.perform_analysis()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

