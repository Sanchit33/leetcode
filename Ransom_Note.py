# My Soluttion 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        val = None
        k = len(magazine)
        n = len(ransomNote)
        ransomNot = sorted(ransomNote)
        magazin = sorted(magazine)
        for i in range(0, k-1,n):
            u = 0
            v = 0
            if ransomNot[0:n+1] in magazin[u:k+1]:
                val = True
                break
            else:
                val = False
            u = i
        return val   

# Others Solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False
        return True
        
