class Square:
    l=b=r=t=0
    def __init__(self,l,b,r,t): self.l,self.b,self.r,self.t=l,b,r,t
    def __str__(self):return f'Square(l:{self.l}, b:{self.b}, r:{self.r}, t:{self.t})'
    def area(self): return (self.r-self.l)*(self.t-self.b)
    def stack(self, other):
        # self가 other의 꼭짓점 0개 포함 - 안겹치는 경우
        if self.l >= other.r or\
           self.b >= other.t or\
           self.r <= other.l or\
           self.t <= other.b:
            return [self]
        # self가 other의 꼭짓점 0개 포함 - self가 other에 포함
        elif self.l >= other.l and\
             self.b >= other.b and\
             self.r <= other.r and\
             self.t <= other.t:
            return []
        # self가 other의 꼭짓점 0개 포함 - self가 other에 의해 작은 하나로 잘림
            # other이 왼쪽
        elif self.l >= other.l and\
             self.l <= other.r <= self.r and\
             self.b >= other.b and\
             self.t <= other.t:
            return [Square(other.r, self.b, self.r, self.t)]
            # other이 아랫쪽
        elif self.b >= other.b and\
             self.b <= other.t <= self.t and\
             self.l >= other.l and\
             self.r <= other.r:
            return [Square(self.l, other.t, self.r, self.t)]
            # other이 오른쪽
        elif self.r <= other.r and\
             self.l <= other.l <= self.r and\
             self.b >= other.b and\
             self.t <= other.t:
            return [Square(self.l, self.b, other.l, self.t)]
            # other이 위쪽
        elif self.t <= other.t and\
             self.b <= other.b <= self.t and\
             self.l >= other.l and\
             self.r <= other.r:
            return [Square(self.l, self.b, self.r, other.b)]
        # self가 other의 꼭짓점 0개 포함 - self가 other에 의해 작은 둘로 잘림
            # self가 other에 비해 가로로 긴 경우
        elif self.l <= other.l <= other.r <= self.r and\
             self.b >= other.b and\
             self.t <= other.t:
            return [Square(self.l, self.b, other.l, self.t),
                    Square(other.r, self.b, self.r, self.t)]
            # self가 other에 비해 세로로 긴 경우
        elif self.b <= other.b <= other.t <= self.t and\
             self.l >= other.l and\
             self.r <= other.r:
            return [Square(self.l, other.t, self.r, self.t),
                    Square(self.l, self.b, self.r, other.b)]
        # self가 other의 꼭짓점 4개 포함
        elif self.l <= other.l and\
             self.b <= other.b and\
             self.r >= other.r and\
             self.t >= other.t:
            return [Square(self.l, other.t, self.r, self.t),
                    Square(self.l, other.b, other.l, other.t),
                    Square(other.r, other.b, self.r, other.t),
                    Square(self.l, self.b, self.r, other.b)]
        else:
            # self 내부에 other의 좌상단이 포함
            lt = self.l <= other.l <= self.r and\
                 self.b <= other.t <= self.t
            # self 내부에 other의 우상단이 포함
            rt = self.l <= other.r <= self.r and\
                 self.b <= other.t <= self.t
            # self 내부에 other의 우하단이 포함
            rb = self.l <= other.r <= self.r and\
                 self.b <= other.b <= self.t
            # self 내부에 other의 좌하단이 포함
            lb = self.l <= other.l <= self.r and\
                 self.b <= other.b <= self.t
            if lt:
                # 좌상단과 우상단이 포함
                if rt:
                    return [Square(self.l, self.b, other.l, other.t),
                            Square(other.r, self.b, self.r, other.t),
                            Square(self.l, other.t, self.r, self.t)]
                # 좌상단과 좌하단이 포함
                elif lb:
                    return [Square(self.l, other.t, self.r, self.t),
                            Square(self.l, other.b, other.l, other.t),
                            Square(self.l, self.b, self.r, other.b)]
                # 좌상단만 포함
                else:
                    return [Square(self.l, self.b, other.l, self.t),
                            Square(other.l, other.t, self.r, self.t)]
            elif rt:
                # 우상단과 우하단이 포함
                if rb:
                    return [Square(self.l, other.t, self.r, self.t),
                            Square(other.r, other.b, self.r, other.t),
                            Square(self.l, self.b, self.r, other.b)]
                # 우상단만 포함
                else:
                    return [Square(self.l, other.t, other.r, self.t),
                            Square(other.r, self.b, self.r, self.t)]
            elif rb:
                # 우하단과 좌하단이 포함
                if lb:
                    return [Square(self.l, other.b, other.l, self.t),
                            Square(other.r, other.b, self.r, self.t),
                            Square(self.l, self.b, self.r, other.b)]
                # 우하단만 포함
                else:
                    return [Square(self.l, self.b, other.r, other.b),
                            Square(other.r, self.b, self.r, self.t)]
            elif lb:
                # 좌하단만 포함
                return [Square(self.l, self.b, other.l, self.t),
                        Square(other.l, self.b, self.r, other.b)]
        
n,k=map(int,input().split())
l=[]

for _ in range(n):
    newSquare = Square(*map(int,input().split()))
    for i in range(len(l)):
        tmp = []
        for j in range(len(l[i])):
            tmp+=l[i][j].stack(newSquare)
        l[i]=tmp
    l.append([newSquare])
size = []
for i in range(n):
    #print(*map(str,l[i]))
    size.append((sum(map(lambda square:square.area(),l[i])),i+1))
size.sort(key=lambda x:(-x[0],x[1]))
size=list(map(lambda x:x[1],size[:k]))
size.sort()
print(*size)
