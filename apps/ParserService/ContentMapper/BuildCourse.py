
def build_course(semester, course_names, course_numbers, course_descriptions, course_attempted_points, course_earned_points, course_letter_grades, course_total_points):
        
    sem_courses_map = {}
    courses = []

    for name, number, description, attempted, earned, grade, total in zip(
        course_names,
        course_numbers,
        course_descriptions,
        course_attempted_points,
        course_earned_points,
        course_letter_grades,
        course_total_points
    ):
        
        course = {
            "name": name,
            "number": number,
            "description": description,
            "attempted_points": attempted,
            "earned_points": earned,
            "letter_grade": grade,
            "total_points": total
        }
        
        courses.append(course)
        sem_courses_map[semester] = courses 
    
    return sem_courses_map 
        