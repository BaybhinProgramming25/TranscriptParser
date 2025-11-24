def build_course(student_id, semester, course_names, course_numbers, course_descriptions, course_attempted_points, course_earned_points, course_letter_grades, course_total_points, content_string):

    for name, number, description, attempted, earned, grade, total in zip(
        course_names,
        course_numbers,
        course_descriptions,
        course_attempted_points,
        course_earned_points,
        course_letter_grades,
        course_total_points
    ):

        tmp_string = f"Student {student_id} took {name} {number} on {semester} and it's about {description}, earned {earned} out of {attempted} points, received grade {grade}, total points is {total}. "
        content_string += tmp_string
    
    return content_string 
        