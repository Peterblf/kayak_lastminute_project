import unittest
import pandas as pd
from modules.data import load_sample_offers
from modules.processing import filter_offers, summarize_by_destination


class TestPandasProject(unittest.TestCase):
    def test_load_and_filter(self):
        df = load_sample_offers()
        criteria = {
            "origin": "Paris",
            "destination": "Rome",
            "max_price": 300,
            "days_until_departure": 3,
        }
        filtered = filter_offers(df, criteria)  # on doit trouver au moins une offre
        self.assertTrue(len(filtered) >= 1)
        # toutes les lignes doivent respecter les critères
        for _, row in filtered.iterrows():
            self.assertEqual(row["origin"], "Paris")
            self.assertEqual(row["destination"], "Rome")
            self.assertLessEqual(row["price"], 300)

    def test_summarize(self):
        df = load_sample_offers()
        summary = summarize_by_destination(df)
        # summary doit être dataframe avec index non vide
        self.assertIn("average_price", summary.columns)
        self.assertIn("count", summary.columns)


if __name__ == "__main__":
    unittest.main()
