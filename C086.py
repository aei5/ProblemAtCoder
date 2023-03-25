vowel = "aiueoAIUEO"
name = input()
cname = ''.join(s for s in name if s not in vowel)
print(cname)
