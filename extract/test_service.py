import os
from unittest import TestCase

from service import get_address_files, extract_data


class TestExtract(TestCase):

    def test_get_address_files(self):
        file_names = [
            "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/bitquery.json",
            "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/blacklist.json",
            "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/dexscreener.json",
            "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/transactions.json",
            "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/transactions_summary.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/bitquery.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/blacklist.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/dexscreener.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/transactions.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/transactions_summary.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/bitquery.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/blacklist.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/dexscreener.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/holders.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/transactions.json",
            "ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc/transactions_summary.json"
        ]
        address_files = get_address_files(file_names)
        self.assertEqual(3, len(address_files.keys()))
        self.assertIsNotNone(address_files["ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000"])
        self.assertIsNotNone(address_files["ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9"])
        self.assertIsNotNone(address_files["ethereum/0x0f20c7da17e5a58a0441a20910d85f2eb80eaafc"])

    def test_extract_data(self):
        os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", "polizoa_credentials.json")
        address = "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9"
        files = [
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/bitquery.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/blacklist.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/dexscreener.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/transactions.json",
            "ethereum/0x01d7f32b6e463c96c00575fa97b8224326c6a6b9/transactions_summary.json"
        ]
        contract = extract_data(address, files)
        self.assertIsNotNone(contract)
        self.assertTrue(contract.is_blacklisted)
        self.assertEqual(7722, contract.transaction_number)
        self.assertFalse(contract.has_pair)
