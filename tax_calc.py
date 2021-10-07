class Company:
    mem=0
    y=0
    nall1=0
    def _init_(self):
        numbers=['.','0','1','2','3','4','5','6','7','8','9']
        sum2=0
        s=[]
        tabis=[]
        mzp=42500
        nall=[]
        y=input("Жалақыны енгізіңіз: ")
        a=y.split(',')
        for each in a:
            set_split=set(each)
            sum2=0
            for i in set_split:
                if i in numbers:
                    sum2+=1
            if len(set_split)==sum2:
                s.append(each)             
        print(s)
        for i in range(len(s)):
            opv=int(s[i])*0.1
            ipn=(int(s[i])-opv-mzp)*0.1
            so=(int(s[i])-opv)*0.035
            sn=(int(s[i])-opv)*0.095-so
            ms=int(s[i])*0.015
            Company.y=int(s[i])-(opv+ipn)
            nald=so+sn+ms
            print("\nҚызметкер таза жалақысы: %d\t опв=%d\t ипн=%d\t со=%d\t сн=%d\t мед.стр=%d\t Компания налогы: %d\n "%(Company.y,opv,ipn,so,sn,ms,nald))
            nall.append(nald)
            tabis.append(Company .y)
        for item1 in range(len(nall)):
            Company.nall1+=int(nall[item1])
        for item in range(len(tabis)):
            Company.mem+=int(tabis[item]) 
        print("\nҚызметкерлерге берілетін жалақы: %d\t|  Компания жалпы налогы: %d\n "%(Company.mem,Company.nall1))
    def taza(self):
        numbers=['.','0','1','2','3','4','5','6','7','8','9']
        y1=input("Таза жалақыны енгізіңіз: ")
        a1=y1.split(',')
        s1=[]
        t=[]
        for each in a1:
            set_split=set(each)
            sum2=0
            for i in set_split:
                if i in numbers:
                    sum2+=1
            if len(set_split)==sum2:
                s1.append(each)
        print("\n Таза жалақы мөлшері: --> --> --> ---> {}".format(s1))
        for i in range(len(s1)):
            x=(100*int(s1[i])-425000)/81
            t.append(int(x))
        print("\n Қызметкерлерге берілетін жалақы : ---> {}".format(t))

    def method(task):
        t=int(input("\nКомпания табысы: "))
        sh=int(input("\nКомпания шығыны: "))
        nal=t*0.03
        nal1=(t-sh)*0.1
        jsh=(sh+nal+nal1+Company.nall1+Company.mem+sh)
        jt=t-jsh
        print("\nКомпания шығыны: %d\t| Жалпы компания табысы: %d "%(jsh,jt))

c=Company()
c.taza()
c.method()
