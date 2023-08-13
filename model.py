class Model:
    def __init__(self):
        self.course_letter_grades = []
        self.course_credits = []
        self.letter_grade_dict = {"AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, "CC": 2.0, "DC": 1.5, "DD": 1.0, "FF": 0.0, "VF": 0.0, "BL": 0.0, "BZ": 0.0}

    def calculate_gpa(self):
        index = 0
        total = 0.0
        for x in self.course_letter_grades:
            total += self.letter_grade_dict[x] * float(self.course_credits[index])
            index += 1
        return total / sum(self.course_credits)
