class Course:
    def __init__(self, name, number, description, attempted_points, earned_points, letter_grade, total_points):
        self.name = name
        self.number = number
        self.description = description
        self.attempted_points = attempted_points
        self.earned_points = earned_points
        self.letter_grade = letter_grade
        self.total_points = total_points

# Simple factory function to build it
def create_course(name, number, description, attempted, earned, letter, total):
    return Course(name, number, description, attempted, earned, letter, total)