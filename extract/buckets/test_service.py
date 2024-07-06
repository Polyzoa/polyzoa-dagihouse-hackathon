import os
from unittest import TestCase
import buckets


class TestBuckets(TestCase):

    def test_list(self):
        os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", "../polizoa_credentials.json")
        files = buckets.list("data-wrangler", "ethereum")
        self.assertIsNotNone(files)
        for file in files:
            print(file.name)

    def test_get(self):
        os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", "../polizoa_credentials.json")
        data = buckets.get("data-wrangler", "ethereum/0x0001efcc64bdbcee3db071f42f1a5072965f0000/blacklist.json")
        self.assertIsNotNone(data)
        self.assertTrue(data["is_blacklisted"])

