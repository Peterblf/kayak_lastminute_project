from modules.data import sample_offers
from modules.search import find_offers
from modules.utils import print_offers

def main():
    """Fonction principale du programme"""

    # On charge des offres fictives (comme une petite base de données)
    offers = sample_offers()

    # On définit les critères de recherche
    criteria = {
        'origin': 'Paris',              # ville de départ
        'destination': 'Rome',          # destination
        'max_price': 300,               # prix maximum en euros
        'days_until_departure': 2       # dans combien de jours maximum
    }

    # On cherche les offres qui correspondent à ces critères
    results = find_offers(offers, criteria)

    # On affiche le résultat à l'écran
    print("\n--- Résultats de la recherche ---\n")
    print_offers(results)

# Si ce fichier est lancé directement, on exécute la fonction main()
if __name__ == '__main__':
    main()
