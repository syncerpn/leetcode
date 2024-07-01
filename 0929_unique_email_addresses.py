# string filtering/processing
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        u = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0]
            name = name.replace(".", "")
            u.add((name, domain))
        return len(u)