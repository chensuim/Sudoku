import numpy as np
from copy import deepcopy
from src.utils import SolverUtils as SV
from src.utils import GeneratorUtils as GU
from src.checkers import SudoCheck as SC
from src.solver import solver as SL
from random import randint


def RandGenerator(A,Known,n):
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandGenerator(Arec,Known,2)
    else:
        print(Arec)
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        print(lenPos)
        if (lenPos==Known):
            return Arec
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGenerator(A3,Known,2)
                lenKn=np.array(np.where(A2!=0))
                #lenKn2=lenKn[0,:].size
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec


def RandGenerator2(A,Known,n):   #almost useless
    #print("hello")
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandGenerator2(Arec,Known,2)
    else:
        print(Arec)
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        print(lenPos)
        if (lenPos==Known):
            return Arec
        #print("hi")
        if (Known<24):
            if (lenPos==24):
                r=randint(1, 10)
                print(r)
                if (r==1 or r==2):
                    print("done24")
                    Crec=SV.ConstructC(Arec)
                    Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
                    Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
            elif(lenPos==25):
                r=randint(1, 10)
                if (r==1):
                    print("done25")
                    Crec=SV.ConstructC(Arec)
                    Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
                    Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGenerator2(A3,Known,2)
                lenKn=np.array(np.where(A2!=0))
                #lenKn2=lenKn[0,:].size
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec


def RandGenerator3(A,Known,n,Abeg):   #Simulated Annealing
    #print("hello")
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandGenerator3(Arec,Known,2,Arec)
    else:
        print(Arec)
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        print(lenPos)
        if (lenPos==Known):
            return Arec
        #print("hi")
        if (lenPos<27):
            p=(lenPos)/(81*2.2)
            x=np.random.uniform(0.0,1.0)
            if (x<=p):
                for i in range(2):
                    pos2fill=np.array(np.where(Arec==0))
                    lenFill=pos2fill[0,:].size
                    pick=randint(0, lenFill-1)
                    Arec[pos2fill[0,pick],pos2fill[1,pick]]=Abeg[pos2fill[0,pick],pos2fill[1,pick]]
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGenerator3(A3,Known,2,Abeg)
                lenKn=np.array(np.where(A2!=0))
                #lenKn2=lenKn[0,:].size
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec
