def length_of_last_word(s):
    s=s.strip()
    a=s.split()
    if len(a)==0:
        return 0
    else:
        return len(a[-1])
input_string="hello world"
r=length_of_last_word(input_string)
print(r)
