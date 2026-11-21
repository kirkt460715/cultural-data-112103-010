import json
import unittest
from pathlib import Path

from app.io import read_records


class FixtureTests(unittest.TestCase):
    def test_records_match_the_declared_fields(self):
        root = Path(__file__).resolve().parents[1]
        records = read_records(root / "fixtures" / "records.json")
        schema = json.loads((root / "schema.json").read_text(encoding="utf-8"))
        self.assertGreater(len(records), 0)
        self.assertTrue(set(schema["fields"]).issubset(records[0]))
        self.assertTrue(all(isinstance(record, dict) for record in records))

    def test_loader_rejects_missing_record_collection(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "invalid.json"
            path.write_text("{}", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_records(path)


if __name__ == "__main__":
    unittest.main()
