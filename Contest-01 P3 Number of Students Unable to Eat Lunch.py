class Solution:
    def countStudents(self, student_preferences: list[int], sandwich_preferences: list[int]) -> int:
        unsatisfied_count = 0
        while len(student_preferences) > unsatisfied_count:
            if student_preferences[0] == sandwich_preferences[0]:
                student_preferences.pop(0)
                sandwich_preferences.pop(0)
                unsatisfied_count = 0
            else:
                removed_student = student_preferences.pop(0)
                student_preferences.append(removed_student)
                unsatisfied_count += 1
        return len(student_preferences)
