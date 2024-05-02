grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
st = list(students)
st.sort()
print(st)
sr1=(sum(grades[0]))/len(grades[0])
sr2=(sum(grades[1]))/len(grades[1])
sr3=(sum(grades[2]))/len(grades[2])
sr4=(sum(grades[3]))/len(grades[3])
sr5=(sum(grades[4]))/len(grades[4])
grades_new = [sr1, sr2, sr3, sr4, sr5]
print(grades_new)
dict1= dict(zip(st, grades_new))
print(dict1)
