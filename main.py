from modules.data import load_sample_offers, save_sample_csv
from modules.processing import filter_offers, summarize_by_destination
from modules.viz import plot_price_by_destination
import pandas as pd

def main():
    df = load_sample_offers()   # DataFrame en mémoire
    save_sample_csv(df, 'offers_sample.csv')

    
    criteria = {
        'origin': 'Paris',# critères pour filtrer
        'destination': None,
        'max_price': 300,
        'days_until_departure': 3
    }

    # filtrer avec les critères
    filtered = filter_offers(df, criteria)

    print("\n-- Offres filtrées (aperçu) --\n")
    print(filtered.to_string(index=False))
    
    summary = summarize_by_destination(filtered)# prix moyen 
    print("\n-- Prix moyen par destination --\n")
    print(summary)

    # save
    plot_price_by_destination(summary, outpath='figs/price_by_destination.png')
    print("\nGraphique sauvegardé dans 'figs/price_by_destination.png'.\n")

if __name__ == '__main__':
    main()
