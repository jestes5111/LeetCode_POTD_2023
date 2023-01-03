# DID NOT SOLVE THIS ON MY OWN 
class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		hash_map = {}
		s = s.split()

		if len(s) != len(pattern):
			return False

		for index in range(len(pattern)):
			if s[index] not in hash_map:
				if pattern[index] not in hash_map.values():
					hash_map[s[index]] = pattern[index]
				else:
					return False
			else:
				if hash_map[s[index]] != pattern[index]:
					return False
		return True
		