import hashlib
import os
import shutil
from pathlib import Path

import pytest

from azure.ai.ml._utils._asset_utils import get_content_hash


@pytest.mark.unittest
class TestGetContentHash:
    def test_get_content_hash_should_not_change(self, tmp_path: Path):
        content1 = b"test\n"
        content2 = b"file2 content\n"
        content3 = b"file3 content\n"
        content4 = b"file4 content\n"
        test_files = [
            ("file1.txt", content1),
            ("folder1/file2.txt", content2),
            ("Folder2/folder1/file4.txt", content4),
            ("Folder2/file3.txt", content3),
        ]
        for test_file_name, test_file_contents in test_files:
            full_file_path = tmp_path / test_file_name
            full_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(full_file_path, "wb") as f:
                f.write(test_file_contents)

        hash = get_content_hash(tmp_path)
        actual_hash = hashlib.sha256()
        actual_hash.update(b"4")
        actual_hash.update(b"#file1.txt#" + str(len(content1)).encode())
        actual_hash.update(b"#folder1/file2.txt#" + str(len(content2)).encode())
        actual_hash.update(b"#Folder2/file3.txt#" + str(len(content3)).encode())
        actual_hash.update(b"#Folder2/folder1/file4.txt#" + str(len(content4)).encode())
        actual_hash.update(content1)
        actual_hash.update(content2)
        actual_hash.update(content3)
        actual_hash.update(content4)
        assert actual_hash.hexdigest() == hash == "3f99429630ebd5882337eedef79dc029a9b406338cd6f466206aef2c951453be"
