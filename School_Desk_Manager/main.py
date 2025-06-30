from school import School
from person import Student, Teacher
from subject import Subject
from classRoom import ClassRoom

school= School("CSTU","Chandpur")

#classes
six=ClassRoom("Six")
seven=ClassRoom("Seven")
eight=ClassRoom("Eight")
nine=ClassRoom("Nine")
ten=ClassRoom("Ten")

school.add_classroom(six)
school.add_classroom(seven)
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#students
priya=Student("Priya",six)
jannatul=Student("Jannatul",nine)
fahima=Student("Fahima",nine)
mahi=Student("Mahi",eight)
poly=Student("Poly",ten)
maisha=Student("Maisha",seven)
anisha=Student("Anisha",ten)
wasifa=Student("Wasifa",six)
sadia=Student("Sadia",seven)
maliha=Student("Maliha",nine)

school.student_admission(priya)
school.student_admission(jannatul)
school.student_admission(fahima)
school.student_admission(mahi)
school.student_admission(poly)
school.student_admission(maisha)
school.student_admission(anisha)
school.student_admission(wasifa)
school.student_admission(sadia)
school.student_admission(maliha)

#teachers
abdul=Teacher("Abdul Hannan")
rofiq=Teacher("Rofique Uddin")
muhib=Teacher("Muhibul Islam")

school.add_teacher("math",muhib)
school.add_teacher("biology",rofiq)
school.add_teacher("english",abdul)

#subjects
math=Subject("Math",muhib)
biology=Subject("Biology",rofiq)
physics=Subject("Physics",muhib)
chemistry=Subject("Chemistry",abdul)
bangla=Subject("Bangla",rofiq)
english=Subject("English",abdul)

six.add_subject(bangla)
six.add_subject(english)
seven.add_subject(bangla)
seven.add_subject(english)
seven.add_subject(math)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(biology)
ten.add_subject(english)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)

six.take_semester_final_exam()
seven.take_semester_final_exam()
eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)