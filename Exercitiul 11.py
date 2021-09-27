n=int(input('numarul de elemente: '))
if n<10 and n>0:
    list1=list(map(lambda element:int(input('element:')),range(n)))
    print('a) afiseaza pe ecran componentele tabloului la un interval de 5 pozitii;','\n  ',*list1[:5])
    list2=list1[::-1]
    print('b) afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator;','\n  ',*list2)
    list2=list1.copy()
    list2.sort(reverse=True)
    print('c) sorteaza componentele tabloului in ordine descrescatoare;','\n  ',list2)
    list3=[x for x in list1 if x%2==0]
    print('d) afiseaza pe ecran doar componentele pare;','\n  ',*list3)
    print('e) afiseaza pe ecran media aritmetica a componentelor pare;','\n  ',sum(list3)/len(list3))
    list4=[x for x in list1 if x%2!=0]
    print('f) afiseaza pe ecran doar componentele impare;','\n  ',*list4)
    print('g) afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y;')
    x,y=int(input('x:')),int(input('y:'))
    list5=[i for i in list1 if (i>x) and (i%y!=0)] 
    print('  ',*list5)
    print('h) afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y')
    x,y=int(input('x:')),int(input('y:'))
    list6=[i for i in list1 if (i>x) and (i<y)]
    print('  ',*list6)
    list7=[list1.index(i) for i in list1 if (i<0) and (i%2!=0)]
    print('i) afiseaza pe ecran pozitiile (indicii) componentelor impare negative;','\n  ',*list7)
    list8=[list1.index(i) for i in list1 if (abs(i)//10<10) and (abs(i)//10>0)]
    print('j) afiseaza pe ecran pozitiile (indicii) componentelor ce contin doar doua cifre semnificative;','\n  ',*list8)
    print('k) inlocuieste prima componenta a tabloului cu componenta de valoare minima din tabloul respectiv;')
    list9=list1.copy()
    list9[0]=min(list9)
    print('  ',list9)
    print('l) inlocuieste componenta de valoare minima din tabloul respectiv cu prima componenta a acestuia;')
    list10=list1.copy()
    list10[list10.index(min(list10))]=list10[0]
    print('  ',list10)
    print('m) creeaza un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatura;')
    list3=[i for i in list1 if i%2==0]
    print('  ',list3)
    print('n) creeaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura;')
    list11=[i for i in list1 if i%3==0]
    print('  ',list11)
    list12=[]
    for i in list1:
        if len([j for j in range(1,i+1) if i%j==0])>=4:
            list12.append(i)
    print('o) creeaza un tablou nou, format doar din acele componente ale tabloului introdus de la tastatura care au cel mult patru divizori.','\n  ',list12)
