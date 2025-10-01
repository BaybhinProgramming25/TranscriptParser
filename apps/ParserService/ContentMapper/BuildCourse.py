from ContentMapper.CourseDataObject import create_course

def build_course(semester, course_names, course_numbers, course_descriptions, course_attempted_points, course_earned_points, course_letter_grades, course_total_points):
    
    sem_courses_map = {}
    courses = []

    # zip() puts matching items together like a zipper!
    for name, number, description, attempted, earned, grade, total in zip(
        course_names,
        course_numbers,
        course_descriptions,
        course_attempted_points,
        course_earned_points,
        course_letter_grades,
        course_total_points
    ):
        
        course = create_course(name, number, description, attempted, earned, grade, total)
        courses.append(course)
        sem_courses_map[semester] = courses 
    
    return sem_courses_map 
        