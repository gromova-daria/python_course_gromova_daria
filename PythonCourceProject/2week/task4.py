"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/validate-ip-address/?envType=problem-list-v2&envId=string
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.is_valid_ipv4(queryIP):
            return "IPv4"
        elif self.is_valid_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

    def is_valid_ipv4(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                return False
            if len(part) > 1 and part[0] == '0':
                return False

        return True

    def is_valid_ipv6(self, ip: str) -> bool:
        parts = ip.split(':')
        if len(parts) != 8:
            return False

        hex_digits = re.compile(r'^[0-9a-fA-F]{1,4}$')
        for part in parts:
            if not hex_digits.match(part):
                return False

        return True   
