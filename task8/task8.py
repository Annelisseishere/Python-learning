strings = ["flower","flow","flight"]

def longest_common_prefix(strings):
	# TODO: compute a longest common prefix of the strings provided. In other words, you need to find a longest string which appears at the begging of each string in strings.
	prefix = ""
	for i,ch in enumerate(strings[0]):
		for j in range(1, len(strings)):
			if i >= len(strings[j]):
				return prefix
			if ch != strings[j][i]:
				return prefix
		prefix += ch

	return prefix

# Should print 'fl'
print(longest_common_prefix(strings))