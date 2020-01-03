import sys;read=sys.stdin.readline

class Node:
    def __init__(self,n):self.n=n

for T in range(int(read())):
    s=read()[:-1]
    for i in range(len(s)):
        if s[i] not in ['<','>','-']:break
    head=Node('')
    cur=Node(s[i])
    head.r,cur.l=cur,head
    if i+1==len(s)-1:
        print(s[i])
        continue
    for c in s[i+1:]:
        if c=='<':
            try:
                if cur.l is not None:cur=cur.l
            except:pass
        elif c=='>':
            try:
                if cur.r is not None:cur=cur.r
            except:pass
        elif c=='-':
            t=cur
            try:
                try:cur.l.r=t.r
                except:
                    try:
                        cur.l.r=None
                    except:pass
                cur.r.l=t.l
            except:pass
            try:cur=t.l
            except:pass
        else:
            t=Node(c)
            try:
                t.r=cur.r
                cur.r.l=t
            except:pass
            cur.r=t
            t.l=cur
            cur=t
    r=[]
    while True:
        try:
            r.append(head.n)
            head=head.r
        except:break
    print(''.join(r))
