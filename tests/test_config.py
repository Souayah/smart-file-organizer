import unittest
import os
import json
import yaml
import shutil
from organizer.config import load_config

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.test_dir = "./test_config_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        self.json_config_path = os.path.join(self.test_dir, "test_config.json")
        self.yaml_config_path = os.path.join(self.test_dir, "test_config.yaml")

        self.sample_json_config = {
            "Documents": ["pdf", "docx"],
            "Images": ["jpg", "jpeg"]
        }
        self.sample_yaml_config = """
Documents:
  - pdf
  - docx
Images:
  - jpg
  - jpeg
"""

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_load_default_config(self):
        config = load_config()
        self.assertIn("Documents", config)
        self.assertIn("Images", config)
        self.assertIn("pdf", config["Documents"])

    def test_load_json_config(self):
        with open(self.json_config_path, "w") as f:
            json.dump(self.sample_json_config, f)
        config = load_config(self.json_config_path)
        self.assertEqual(config, self.sample_json_config)

    def test_load_yaml_config(self):
        with open(self.yaml_config_path, "w") as f:
            f.write(self.sample_yaml_config)
        config = load_config(self.yaml_config_path)
        self.assertEqual(config, yaml.safe_load(self.sample_yaml_config))

    def test_load_non_existent_config(self):
        with self.assertRaises(FileNotFoundError):
            load_config("non_existent_file.json")

    def test_load_unsupported_format(self):
        unsupported_path = os.path.join(self.test_dir, "test_config.txt")
        with open(unsupported_path, "w") as f:
            f.write("some content")
        with self.assertRaises(ValueError) as cm:
            load_config(unsupported_path)
        self.assertIn("Unsupported configuration file format", str(cm.exception))

    def test_load_malformed_json(self):
        malformed_json_path = os.path.join(self.test_dir, "malformed.json")
        with open(malformed_json_path, "w") as f:
            f.write("{\"key\": \"value\",}") # Malformed JSON with trailing comma
        with self.assertRaises(ValueError) as cm:
            load_config(malformed_json_path)
        self.assertIn("Error loading configuration", str(cm.exception))

if __name__ == '__main__':
    unittest.main()


