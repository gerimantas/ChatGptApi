import unittest
import os
from APS_project_manager.AI_assistant.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.txt"
        self.file_manager = FileManager()

    def test_create_file(self):
        self.file_manager.write_file(self.file_path, "Test content")
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_file(self):
        self.file_manager.write_file(self.file_path, "Test content")
        content = self.file_manager.read_file(self.file_path)
        self.assertEqual(content, "Test content")

    def test_delete_file(self):
        self.file_manager.write_file(self.file_path, "Test content")
        self.file_manager.delete_file(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.file_manager.read_file("nonexistent.txt")

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == '__main__':
    unittest.main()

