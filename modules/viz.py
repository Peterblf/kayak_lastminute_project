import matplotlib.pyplot as plt


def plot_price_by_destination(summary_df, outpath="price_by_destination.png"):

    if summary_df is None or summary_df.empty:  # verif que le dataframe != vide
        print("Aucune donnée pour tracer le graphique.")
        return

    destinations = summary_df.index.tolist()
    prices = summary_df["average_price"].tolist()

    # création du graph
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(destinations, prices)
    ax.set_xlabel("Destination")
    ax.set_ylabel("Prix moyen (€)")
    ax.set_title("Prix moyen par destination (offres filtrées)")
    plt.tight_layout()

    # save
    fig.savefig(outpath)
    plt.close(fig)
