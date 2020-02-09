postfix,stack,f="",[],{'+':1,'-':1,'*':2,'/':2,'(':0}
for c in list(input()):
    if ord('A')<=ord(c)<=ord('Z'):postfix+=c
    else:
        if c==')':
            while True:
                t=stack.pop()
                if t=='(':break
                postfix+=t
        elif not stack:stack.append(c)
        elif c=='('or f[c]>f[stack[-1]]:stack.append(c)
        else:
            while True:
                postfix+=stack.pop()
                if not stack or f[c]>f[stack[-1]]:break
            stack.append(c)
print(postfix+''.join(stack[::-1]))
