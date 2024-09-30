"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-duplicate-file-in-system/?envType=problem-list-v2&envId=string
"""


from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            directory = parts[0]

            for file_info in parts[1:]:
                filename, content = self.extract_file_info(file_info)
                full_path = f"{directory}/{filename}"
                content_map[content].append(full_path)

        return [files for files in content_map.values() if len(files) > 1]

    def extract_file_info(self, file_info: str) -> tuple[str, str]:
        filename, content = file_info.split("(")
        content = content[:-1]  
        return filename, content
