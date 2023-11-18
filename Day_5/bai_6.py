import pprint
import numpy as np

def generate_dict_student_auto(number_of_student):
    
    student_id = [str(i) for i in range(202160000, 202160000+number_of_student)]
    
    gpa_score = np.arange(0, 4.1, 0.5)
    student_gpa = np.random.choice(gpa_score,size= number_of_student)
    
    student_dict = {}
    for i, j, in zip(student_id, student_gpa):
        student_dict.update({i: j})
        
    return student_dict    

def student_GPA_ok(student_dict): 
    
    student_GPA_ok = {}
    for i, j in student_dict.items():
        if 2.5 <= j <= 3.5:
            student_GPA_ok.update({i: j})
            
    return student_GPA_ok

def student_GPA_not_ok(student_dict): 
    
    student_GPA_not_ok = {}
    for i, j in student_dict.items():
        if j < 2.0:
            student_GPA_not_ok.update({i: j})
            
    return student_GPA_not_ok

def add_student(student_dict):
        
    student_id = input("Nhập mã số sinh viên: ")
    student_gpa = float(input("Nhập điểm trung bình: "))
    
    student_dict.update({student_id: student_gpa})
    
    return student_dict

student_dict = generate_dict_student_auto(10)
print("SINH VIÊN: ")
pprint.pprint(student_dict)
print('\n\n')
print("Sinh viên GPA OK: ")
pprint.pprint(student_GPA_ok(student_dict))
print('\n\n')
print("Sinh viên GPA NOT OK: ")
pprint.pprint(student_GPA_not_ok(student_dict))
print('\n\n')