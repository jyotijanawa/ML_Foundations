import pandas as pd
print("=================================")
print("CAMPUS PLACEMENT ELIGIBILITY ENGINE STARTING")
print("=================================")
raw_data = {
    'Student_ID':[201,202,203,204,205,206],
    'Name':['A','B','C','D','E','F'],
    'Branch':['CSE','ECE','CSE','ME','CSE','ECE'],
    'CGPA':[8.2,6.4,7.9,8.5,5.8,9.1],
    'Backlogs':[0,2,0,0,1,0],
    'Coding_Score_Pct':[85,40,75,30,90,95]
}
df = pd.DataFrame(raw_data)
print("\n[INFO] Raw ")