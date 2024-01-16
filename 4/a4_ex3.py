# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:31:25 2023

@author: TheoS
"""
#Exercise Grading

# 10 assignments: 100 points each = 1000 assignment points

#  Exam: 100 points (this is the lecture exam, i.e., there is no
# separate exercise exam)

def grade_calculator(
        assignments: list,
        bonus_assignment: int,
        exam: int) -> tuple([bool, int]):
    
# check None
    for i in range(len(assignments)):
        if assignments[i] is None:
            assignments[i] = 0
    if bonus_assignment is None:
        bonus_assignment = 0
    if exam is None:
        exam = 0
        
#  Rules to pass the course (must fulfill all!):
# A) ≥ 25% of the achievable points for ≥ 8 assignments
    count_assign = 0
    for assign_point in assignments:
        if assign_point >= 25:
            count_assign += 1
    if count_assign < 8 and bonus_assignment < 25:
            return tuple([False, 5])
    else : 
        # print(count_assign)
        # pass rule A, check Rule B
        # B) ≥ 50% of all achievable assignment points (10 combined)
        achiv_point = 0
        for assign_point in assignments:
            achiv_point += assign_point
        if achiv_point < 500:
            return tuple([False, 5])
        else : 
            # print(achiv_point)
            # pass rule B, check Rule C
            # C) ≥ 50% of the achievable exam points
            if exam < 50 :
                return tuple([False, 5])
            else :
                # pass rule C, check Bonus
                # add the bonus point
                course_percent = 0
                achiv_point += (bonus_assignment + exam)
                # The grade is determined based on 1100 points
                course_percent = (achiv_point/1100)*100
                # print(course_percent)
                # cal grade
                # ≥ 87.5% (1) Sehr Gut
                if course_percent >= 87.5:
                    return tuple([True, 1])
                # ≥ 75% and < 87.5% (2) Gut
                elif course_percent >= 75:
                    return tuple([True, 2])
                # ≥ 62.5% and < 75% (3) Befriedigend
                elif course_percent >= 62.5:
                    return tuple([True, 3])
                # ≥ 50% and < 62.5% (4) Genügend
                elif course_percent >= 50:
                    return tuple([True, 4])
                # < 50% (5) Nicht Genügend
                else:
                    return tuple([False, 5])
     
                
# print(grade_calculator([95,100,39,13,86,71,20,100,83,100], None, 82))
# print(grade_calculator([95,100,39,13,86,71,20,100,83,100], 51, 82))
# print(grade_calculator([0,100,100,13,100,100,20,100,100,100], 0, 100))
# print(grade_calculator([0,100,100,13,100,100,20,100,100,100], 100, 100))
# print(grade_calculator([0,100,100,13,100,100,None,100,100,100], 100, 100))
# print(grade_calculator([100,100,100,100,100,100,100,100,100,100], 100, 49))

