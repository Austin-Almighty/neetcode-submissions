class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        student_queue = Counter(students) 

        for sandwich in sandwiches:
            if student_queue[sandwich] > 0:
                student_queue[sandwich] -=1
                res -=1
            else:
                return res
        
        return res