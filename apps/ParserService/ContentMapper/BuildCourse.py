def build_course(student_id, semester, course_names, course_numbers, course_descriptions, course_attempted_points, course_earned_points, course_letter_grades, course_total_points, semesters_map):

    for name, number, description, attempted, earned, grade, total in zip(
        course_names,
        course_numbers,
        course_descriptions,
        course_attempted_points,
        course_earned_points,
        course_letter_grades,
        course_total_points
    ):

        class_str = f"{name}{number} is about {description}, earned {earned} out of {attempted} points, received grade {grade}, total points is {total}"
        key = f"{student_id}_{semester}_{name}{number}"
        semesters_map[key] = class_str 
    
    return semesters_map 
        