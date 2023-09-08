# cook your dish here
def time_parts(tstr):
    parts=tstr.split(' ')
    etime=parts[0].split(':')
    eH=int(etime[0])
    eM=int(etime[1])
    eP=parts[1]
    if eP=='PM' and eH<12:
        eH +=12 #to 24hrs format
    if eP=='AM' and eH==12:
        eH=0
    return eH,eM,eP
    
for _ in range(int(input())):
    event = input()
    evh,evm,evp= time_parts(event)
    count = int(input())
    slots=[]
    for _ in range(count):
        slots.append(input())
        
    for slot in slots:
        es = slot.split(' ')
        isND=False
        sh,sm,sp = time_parts(f'{es[0]} {es[1]}')
        eh,em,ep = time_parts(f'{es[2]} {es[3]}')
    
        st=0
        et=0
        evt=0
        if (sp =='AM' and ep=='AM'):
            if sh>eh:
                isND=True
        if (sp=='PM' and ep=='PM'):
            if sh>eh:
                isND=True
        if sp =='PM' and ep=='AM':
            isND = True
    
        st = (60 * sh) + sm
        et = (60 * eh) + em
        evt = (60 * evh) + evm
        if isND:
            et += (24*60)
        if st<= evt and evt<=et:
            print(1, end='')
        else:
            print(0,end='')
    print()