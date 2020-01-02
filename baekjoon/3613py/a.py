s=input()
def conv(s):
    m,r,t='','',False
    for c in s:
        if ord(c) in range(ord('A'),ord('Z')+1):
            if m=='J':return''
            m='C'
            r+='_'+chr(ord('a')+ord(c)-ord('A'))
            continue
        elif c=='_':
            if m=='C':return''
            m='J'
            t=True
            continue
        if t and c=='_':return ''
        r+=chr(ord('A')+ord(c)-ord('a')) if t else c
        t=False
    return r
r=conv(s)
if ord(s[0]) in range(ord('A'),ord('Z')+1) or s[0]=='_' or s[-1]=='_' or s!=conv(r):
    r='Error!'
print(r)
