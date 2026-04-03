"""
import csv

with open('generated_data.csv', 'r') as f:

    reader = csv.DictReader(f)
    sClasses = set()
    sGrades = set()
    tClasses = set()
    jGrades = set()
    
    i=0
    for row in reader:
        if i<5000:
            sClasses.add(row['class_assigned'])
            sGrades.add(int(row['grade_level']))
            i+=1
        else:
            tCl=row['mentor_class']
            Cl=int(tCl[:-1])
            tClasses.add(tCl)
            if Cl not in jGrades and row['judge']=='True':
                jGrades.add(Cl)

    tNotClasses = {}
    for Cl in sClasses - tClasses:
        gr = int(Cl[:-1])
        secn = Cl[-1]
        try:
            tNotClasses[gr].add(secn)

        except:
            tNotClasses[gr] = {secn}
    jNotGrades = sGrades - jGrades
    #print(sGrades, jGrades, jNotGrades, sep='\n')


with open('errors.txt','w') as f:
    for gr in sorted(tNotClasses.keys()):
        for secn in sorted(tNotClasses[gr]):
            f.write(f'Class {gr}{secn}: Error TEACHER not found.\n')
    for gr in sorted(list(jNotGrades)):
        f.write(f'Class {gr}: Error JUDGE not found.\n')
"""
"""
f=open("C:\\Users\\Aviral Singh\\OneDrive\\Desktop\\CS\\VS Code\\Me.txt","w")
text=f.write("Hi, That's Me ^-^")
print(text)
f.close
f1=open("C:\\Users\\Aviral Singh\\OneDrive\\Desktop\\CS\\VS Code\\Me.txt","a")
text1=f1.write("\n"+"I've got an exam today :(")
f1.close
"""
import csv
with open("C:\\Users\\Aviral Singh\\OneDrive\\Desktop\\CS\\VS Code\\generated_data.csv","r") as Gen:
    NewGen=csv.reader(Gen)
    for column in NewGen:
        print(column[2])