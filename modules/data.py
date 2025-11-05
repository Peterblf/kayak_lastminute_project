import pandas as pd
from datetime import datetime, timedelta


def load_sample_offers():  # dataframe pandas pour des fausses offres

    today = datetime.now().date()
    data = [
        (1, "Paris", "Rome", 199, today + timedelta(days=1), "flight"),
        (2, "Paris", "Madrid", 149, today + timedelta(days=3), "flight"),
        (3, "Lyon", "Rome", 89, today + timedelta(days=1), "hotel"),
        (4, "Paris", "Rome", 320, today + timedelta(days=5), "flight"),
        (5, "Paris", "Rome", 250, today + timedelta(days=2), "flight"),
        (6, "Lille", "Berlin", 120, today + timedelta(days=2), "flight"),
        (7, "Paris", "Berlin", 180, today + timedelta(days=2), "flight"),
        (8, "Lyon", "Madrid", 95, today + timedelta(days=4), "hotel"),
    ]
    df = pd.DataFrame(
        data, columns=["id", "origin", "destination", "price", "departure_date", "type"]
    )
    return df


def save_sample_csv(df, filename="offers_sample.csv"):  # save dans un csv

    df.to_csv(filename, index=False, date_format="%Y-%m-%d")
