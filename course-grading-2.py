student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")


#reading student info file
names= {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts= line.split(";")
        if parts[0]=='id':
            continue
        name = f"{parts[1]} {parts[2]}"
        names[parts[0]]= name 

#reading exercise data file 

exercises={} 
exercise_completed={} 
with open(exercise_data) as new_file:
    for line in new_file:
        parts=line.split(";")
        if parts[0]=='id':
            continue

        exercise_done = 0
        for index in range(1,len(parts)):
            exercise_done+= int(parts[index]) 
            index+=1
        exercise_completed[parts[0]] = exercise_done

        exercise = 0
        for index in range(1,len(parts)):
            exercise+= int(parts[index]) 
            index+=1
        exercise_finished = (exercise/40)*100

 #calculating the the exercise points       
        if 0 <= exercise_finished <= 9:
            exercise_points=0
        elif 10 <= exercise_finished <= 19:
            exercise_points=1
        elif 20 <= exercise_finished <= 29:
            exercise_points=2
        elif 30 <= exercise_finished <= 39:
            exercise_points=3
        elif 40 <= exercise_finished <= 49:
            exercise_points=4
        elif 50 <= exercise_finished <= 59:
            exercise_points=5
        elif 60 <= exercise_finished <= 69:
            exercise_points=6
        elif 70 <= exercise_finished <= 79:
            exercise_points=7
        elif 80 <= exercise_finished <= 89:
            exercise_points=8
        elif 90 <= exercise_finished <= 99:
            exercise_points=9
        elif exercise_finished == 100:
            exercise_points=10
        exercises[parts[0]]= exercise_points

exams = {}
with open(exam_points) as new_file:
    for line in new_file:
        parts=line.split(";")
        if parts[0]=='id':
            continue
        exam_points = 0 
        for index in range(1,len(parts)):
            exam_points += int(parts[index]) 
            index+=1
        exams[parts[0]] = exam_points

total_points= {}
for id,exercise_points in exercises.items():
    if id in exams:
        exam_points=exams[id]
        total_point = exercise_points + exam_points 
        total_points[id] = total_point

grades = {}
for id,exercise_points in exercises.items():
    if id in exams:
        exam_points=exams[id]
        total = exercise_points + exam_points 
        if 0 <= total <= 14:
            grade = 0
        if 15 <= total <= 17:
            grade = 1
        if 18 <= total <= 20:
            grade = 2
        if 21 <= total <= 23:
            grade = 3
        if 24 <= total <= 27:
            grade = 4
        if total >= 28:
            grade = 5
        grades[id]= grade
#course info
with open(course_info) as course_file:
    course = []
    for line in course_file:
        line= line.replace("\n","")
        line= line.split(":")
        course.append(line[1])
    course[0] = course[0][1:]
with open("results.txt", "w") as result_file:
    result_file.write(f"{course[0]},{course[1]} credits\n")
    length = len(course[0])+len(course[1])+9
    result_file.write("="*length +"\n")
    result_file.write(f"""{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n""")
    for id,name in names.items():
        result_file.write(f"{name:30}")
        if id in exercise_completed :
            exercise_done = exercise_completed[id] 
            result_file.write(f"{exercise_done:<10}")
        if id in exercises:
            exercise_points=exercises[id]
            result_file.write(f"{exercise_points:<10}")
        if id in exams:
            exam_points = exams[id]
            result_file.write(f"{exam_points:<10}")
        if id in total_points:
            total_point = total_points[id]
            result_file.write(f"{total_point:<10}")
        if id in grades:
            grade=grades[id]
            result_file.write(f"{grade}\n")

with open("results.csv", "w") as result_csv:
    for id,name in names.items():
        if id in grades:
            grade=grades[id]
            result_csv.write(f"{id};{name};{grade}\n")

print("Results written to files results.txt and results.csv")
