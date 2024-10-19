from scipy.stats import f_oneway, ttest_ind, chi2_contingency
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def describe_data(self):
        print("Descriptive Statistics:")
        print(self.df.describe())

    def ask_for_correlation(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        x_col = input("Choose first column for correlation: ")
        y_col = input("Choose second column for correlation: ")
        if x_col in numeric_cols and y_col in numeric_cols:
            correlation = self.df[x_col].corr(self.df[y_col])
            print(f"Correlation between {x_col} and {y_col}: {correlation}")
        else:
            print("Invalid column selection.")

    def ask_for_standard_deviation(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        col = input("Choose a column for standard deviation: ")
        if col in numeric_cols:
            std_dev = self.df[col].std()
            print(f"Standard deviation of {col}: {std_dev}")
        else:
            print("Invalid column selection.")

    def ask_for_skewness(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        col = input("Choose a column for skewness: ")
        if col in numeric_cols:
            skewness = self.df[col].skew()
            print(f"Skewness of {col}: {skewness}")
        else:
            print("Invalid column selection.")

    def ask_for_kurtosis(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        col = input("Choose a column for kurtosis: ")
        if col in numeric_cols:
            kurtosis = self.df[col].kurt()
            print(f"Kurtosis of {col}: {kurtosis}")
        else:
            print("Invalid column selection.")

    def perform_anova(self):
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        numeric_cols = self.df.select_dtypes(include=['number']).columns

        if len(categorical_cols) == 0 or len(numeric_cols) == 0:
            print("Not enough columns for ANOVA.")
            return

        print(f"Categorical columns: {list(categorical_cols)}")
        cat_col = input("Choose categorical column for ANOVA: ")
        print(f"Numeric columns: {list(numeric_cols)}")
        num_col = input("Choose numeric column for ANOVA: ")

        if cat_col in categorical_cols and num_col in numeric_cols:
            groups = [group[num_col].values for name, group in self.df.groupby(cat_col)]
            if len(groups) < 2:
                print("Not enough groups for ANOVA.")
                return

            f_stat, p_value = f_oneway(*groups)
            print(f"ANOVA results: F-statistic = {f_stat}, p-value = {p_value}")

            if p_value < 0.05:
                print("The means are significantly different (p < 0.05).")
            else:
                print("The means are not significantly different (p >= 0.05).")
        else:
            print("Invalid column selection.")

    def perform_t_test(self):
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        numeric_cols = self.df.select_dtypes(include=['number']).columns

        if len(categorical_cols) == 0 or len(numeric_cols) == 0:
            print("Not enough columns for t-test.")
            return

        print(f"Categorical columns: {list(categorical_cols)}")
        cat_col = input("Choose categorical column for t-test: ")
        print(f"Numeric columns: {list(numeric_cols)}")
        num_col = input("Choose numeric column for t-test: ")

        if cat_col in categorical_cols and num_col in numeric_cols:
            groups = [group[num_col].values for name, group in self.df.groupby(cat_col)]
            if len(groups) != 2:
                print("t-test requires exactly two groups.")
                return

            t_stat, p_value = ttest_ind(*groups)
            print(f"t-test results: t-statistic = {t_stat}, p-value = {p_value}")

            if p_value < 0.05:
                print("The means are significantly different (p < 0.05).")
            else:
                print("The means are not significantly different (p >= 0.05).")
        else:
            print("Invalid column selection.")

    def perform_chi_square_test(self):
        categorical_cols = self.df.select_dtypes(include=['object']).columns

        if len(categorical_cols) < 2:
            print("Not enough categorical columns for chi-square test.")
            return

        print(f"Categorical columns: {list(categorical_cols)}")
        col1 = input("Choose first categorical column for chi-square test: ")
        col2 = input("Choose second categorical column for chi-square test: ")

        if col1 in categorical_cols and col2 in categorical_cols:
            contingency_table = pd.crosstab(self.df[col1], self.df[col2])
            chi2, p_value, dof, expected = chi2_contingency(contingency_table)
            print(f"Chi-square test results: chi2 = {chi2}, p-value = {p_value}, dof = {dof}")

            if p_value < 0.05:
                print("The variables are significantly associated (p < 0.05).")
            else:
                print("The variables are not significantly associated (p >= 0.05).")
        else:
            print("Invalid column selection.")

    def plot_qq(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        print(f"Numeric columns: {list(numeric_cols)}")
        col = input("Choose a numeric column for Q-Q plot: ")
        if col in numeric_cols:
            stats.probplot(self.df[col], dist="norm", plot=plt)
            plt.title(f'Q-Q Plot of {col}')
            plt.show()
        else:
            print("Invalid column selection.")



if __name__ == "__main__":
    import pandas as pd
    
    # 创建测试数据
    data = {
        'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 12, 15, 17, 20, 25]
    }
    df = pd.DataFrame(data)

    # 创建 DataAnalyzer 实例并调用 perform_anova
    analyzer = DataAnalyzer(df)
    analyzer.perform_anova()

if __name__ == "__main__":
    df = pd.DataFrame({
        'Category': ['A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25]
    })
    analyzer = DataAnalyzer(df)
    analyzer.perform_t_test()  # 测试 t-test 方法


