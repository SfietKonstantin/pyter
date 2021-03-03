import pandas
import matplotlib.pyplot as plt


def config_plot():
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['figure.dpi'] = 100


def load_covid() -> pandas.DataFrame:
    df = load_covid_raw()
    fixed_df = df.drop(labels=["Province/State", "Lat", "Long"], axis=1)
    return fixed_df.groupby("Country/Region").sum().transpose()


def load_covid_raw() -> pandas.DataFrame:
    csv = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    return pandas.read_csv(csv)


def get_worst(df: pandas.DataFrame, count):
    return df.sum().sort_values().take(range(-count, 0)).index
