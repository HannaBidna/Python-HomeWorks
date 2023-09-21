b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode()
print(s)

s_latin = s.encode('latin1')
print(s_latin)

s_str = s_latin.decode('latin1')
print(s_str)