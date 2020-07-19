input()
s=input()
d={'A':{'A':'A','G':'C','C':'A','T':'G'},
   'G':{'A':'C','G':'G','C':'T','T':'A'},
   'C':{'A':'A','G':'T','C':'C','T':'G'},
   'T':{'A':'G','G':'A','C':'G','T':'T'}}
while len(s)>1: s=s[:-2]+d[s[-1]][s[-2]]
print(s)
