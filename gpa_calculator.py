def quality_points(grade, level):
    points = 0.0

    if grade > 50:
        points += (grade - 50) * 0.1

    if level == 'H':
        points += 0.5
    elif level in ['AP', 'IB', 'DC']:
        points += 1

    return round(points, 1)


with open('transcript.txt', 'r') as f:
    lines = f.read().splitlines()

total_points = 0
total_units = 0

for line in lines:
    course_data = line.split(',')
    course_data = [d.strip() for d in course_data] # get rid of extra spaces around commas
    
    title = course_data[0]
    level = course_data[1]
    units = float(course_data[2])
    grade = int(course_data[3])
    points = quality_points(grade, level)
    
    print(f"{title:<30}  {level:<2}  {units:1}  {grade:>3}  {points:>3}")

    total_points += points * units
    total_units += units

gpa = total_points / total_units
gpa = round(gpa, 3)

print("GPA: " +  str(gpa))


    
