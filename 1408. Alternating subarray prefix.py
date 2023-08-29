# cook your dish here
for _ in range(int(input())):
    n=int(input())
    ints=list(map(int,input().split()))
    
    ans=[0]*n
    ans[-1]=1
    j=0
    # for j in range(size-1):
    while(j<n-1):
        # m_count=1
        count=1
        for i in range(j,n-1):
            if(ints[i]<0):
                if(ints[i+1]>0):
                    count+=1
                else:
                    # If both ints are having same sign then, just compare with m_count and
                    # update it
                    # if(count>=m_count):
                    # m_count=count
                    break
            else:
                if(ints[i+1]<0):
                    count+=1
                else:
                    # Same sign so, now check and update
                    # if(count>=m_count):
                    # m_count=count
                    break
        itr=count
        while(itr>0):
            ans[j]=itr
            j+=1
            itr-=1
            
    print(*ans)