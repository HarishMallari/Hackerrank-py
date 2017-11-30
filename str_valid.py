def str_valid(word):
	
	print(" ",word)
	
	for i in range(len(s)):
		if s[i:].word() :
			return "True"
	return "False"            


if __name__ == '__main__':
    s = input()
    
    print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)

for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        any(eval("c." + test + "()") for c in s)

for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print any(method(c) for c in s)

    t = type(s)
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print any(method(c) for c in s)