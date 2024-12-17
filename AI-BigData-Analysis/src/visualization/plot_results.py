import pandas as pd
import matplotlib.pyplot as plt

def plot_sales(file_path):
    df = pd.read_csv(file_path)
    df.groupby("region")["sales"].sum().plot(kind="bar", title="Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.savefig("../results/sales_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_sales("../data/raw/sales_data.csv")