import unittest
import os
import shutil
from unittest.mock import MagicMock, patch
from organizer.core import FileOrganizer

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = "./test_organizer_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        self.logger = MagicMock()
        self.default_rules = {
            "Documents": ["pdf", "doc"],
            "Images": ["jpg", "png"],
            "Archives": ["zip"]
        }
        self.organizer = FileOrganizer(self.default_rules)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def _create_test_file(self, filename, content="dummy content"):
        with open(os.path.join(self.test_dir, filename), "w") as f:
            f.write(content)

    def test_organize_files_success(self):
        self._create_test_file("report.pdf")
        self._create_test_file("photo.jpg")
        self._create_test_file("archive.zip")
        self._create_test_file("text.txt") # Should not be moved

        moved_count = self.organizer.organize_files(self.test_dir, self.logger)

        self.assertEqual(moved_count, 3)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "report.pdf")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "photo.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Archives", "archive.zip")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "text.txt")))
        self.logger.info.assert_any_call("Moved: report.pdf -> Documents/")
        self.logger.info.assert_any_call("Moved: photo.jpg -> Images/")
        self.logger.info.assert_any_call("Moved: archive.zip -> Archives/")
        self.logger.debug.assert_any_call(f"No rule for extension txt: text.txt")

    def test_organize_files_empty_directory(self):
        moved_count = self.organizer.organize_files(self.test_dir, self.logger)
        self.assertEqual(moved_count, 0)
        self.logger.info.assert_called_with("Finished organizing files. Moved 0 files.")

    def test_organize_files_non_existent_path(self):
        non_existent_path = "./non_existent_dir"
        moved_count = self.organizer.organize_files(non_existent_path, self.logger)
        self.assertIsNone(moved_count) # No files moved, function returns None on error
        self.logger.error.assert_called_with(f"Source path does not exist or is not a directory: {non_existent_path}")

    def test_organize_files_with_subdirectories(self):
        os.makedirs(os.path.join(self.test_dir, "subdir"), exist_ok=True)
        self._create_test_file("subdir/nested.pdf")
        self._create_test_file("top_level.jpg")

        moved_count = self.organizer.organize_files(self.test_dir, self.logger)
        self.assertEqual(moved_count, 1)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "top_level.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "subdir", "nested.pdf")))

    @patch('shutil.move')
    def test_organize_files_move_error(self, mock_move):
        mock_move.side_effect = Exception("Permission denied")
        self._create_test_file("error.pdf")

        moved_count = self.organizer.organize_files(self.test_dir, self.logger)
        self.assertEqual(moved_count, 0)
        self.logger.error.assert_called_with("Error moving error.pdf: Permission denied")

if __name__ == '__main__':
    unittest.main()


