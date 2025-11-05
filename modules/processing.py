import pandas as pd
from datetime import datetime


def filter_offers(
    df: pd.DataFrame, criteria: dict
) -> pd.DataFrame:  # filtre avec criteres simples

    result = df.copy()

    # filtrer par origin
    origin = criteria.get("origin")
    if origin:
        result = result[result["origin"].str.lower() == origin.lower()]

    # par destination
    destination = criteria.get("destination")
    if destination:
        result = result[result["destination"].str.lower() == destination.lower()]

    # par prix max
    max_price = criteria.get("max_price")
    if max_price is not None:
        result = result[result["price"] <= float(max_price)]

    # par jours avant départ
    days = criteria.get("days_until_departure")
    if days is not None:
        today = datetime.now().date()
        result = result[
            result["departure_date"].apply(lambda d: 0 <= (d - today).days <= int(days))
        ]

    # par prix croissant
    result = result.sort_values(by="price")
    return result.reset_index(drop=True)


def summarize_by_destination(
    df: pd.DataFrame,
) -> (
    pd.DataFrame
):  # retourne un dataframe avec prix moyen et nombre d'offres par destination

    if df.empty:
        return pd.DataFrame(
            columns=["destination", "average_price", "count"]
        ).set_index("destination")

    summary = df.groupby("destination").agg(
        average_price=("price", "mean"), count=("price", "size")
    )
    # arrondir le prix moyen pour lisibilité
    summary["average_price"] = summary["average_price"].round(2)
    return summary
