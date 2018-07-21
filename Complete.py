import random
class Matrix():
    
    def A(self,row,cols):
        self.list=[]
        self.n1=row
        self.m1=cols
        self.index=int(row)*int(cols)
        for i in range(self.index):
            self.list.append(random.randint(0,9))
        self.list

        print('Matrix A('+self.n1+','+self.m1+'):')
        for ii in range(int(self.n1)):
            for jj in range(int(self.m1)):
                print(self.list[jj+ii*int(self.m1)],end=' ')
            print('')
        
    def B(self,row,cols):
        self.list2=[]
        self.n2=row
        self.m2=cols
        self.index2=int(row)*int(cols)
        for i in range(self.index2):
            self.list2.append(random.randint(0,9))
        self.list2

        print('Matrix B('+self.n2+','+self.m2+'):')
        for ii in range(int(self.n2)):
            for jj in range(int(self.m2)):
                print(self.list2[jj+ii*int(self.m2)],end=' ')
            print('')
   
    def add(self):
        self.addlist=[]
        for i in range(self.index2):
            self.addlist.append(self.list[i]+self.list2[i])
        self.addlist

        print('='*10+' A + B '+'='*10)
        if self.n1==self.n2 and self.m1==self.m2:
            for ii in range(int(self.n1)):
                for jj in range(int(self.m1)):
                    print(self.addlist[jj+ii*int(self.m1)],end=' ')
                print('')
        else:
            print("Matrixs' size should be in the same size")

    def plus(self):
        self.pluslist=[]
        for i in range(self.index2):
            self.pluslist.append(self.list[i]-self.list2[i])
        self.pluslist

        print('='*10+' A - B '+'='*10)
        if self.n1==self.n2 and self.m1==self.m2:
            for ii in range(int(self.n1)):
                for jj in range(int(self.m1)):
                    print(self.pluslist[jj+ii*int(self.m1)],end=' ')
                print('')
        else:
            print("Matrixs' size should be in the same size")

    def cross(self):
        a=0
        self.crosslist=[]
        n1=int(self.n1)
        m1=int(self.m1)
        n2=int(self.n2)
        m2=int(self.m2)
        for j in range(n1):
            for k in range(m2):
                for l in range(m1):
                    self.element=self.list[l+j*m1]*self.list2[0+m2*l+k*1]
                    a=a+int(self.element)
                self.crosslist.append(a)
                a=0

        print('='*10+' A * B '+'='*10)
        for ii in range(int(self.n1)):
            for jj in range(int(self.m2)):
                print(self.crosslist[jj+ii*int(self.m2)],end=' ')
            print('')

    def transpose(self):
        self.tralist=[]
        n1=int(self.n1)
        m2=int(self.m2)
        for i in range(n1*m2):
            self.tralist.append(0)
       
        for j in range(n1):
            for k in range(m2):
                self.tralist[j+k*n1]=self.crosslist[k+j*m2]

        print('='*5+' the transpose of A * B '+'='*5)
        for ii in range(int(self.m2)):
            for jj in range(int(self.n1)):
                print(self.tralist[jj+ii*int(self.n1)],end=' ')
            print('')
 
a=Matrix()
a.A(input("Enter A matrix's row:"),input("Enter A matrix's cols:"))
a.B(input("Enter B matrix's row:"),input("Enter B matrix's cols:"))
a.add()
a.plus()
a.cross()
a.transpose()

