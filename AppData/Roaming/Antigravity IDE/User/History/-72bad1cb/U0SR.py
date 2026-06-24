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
print("\n[INFO] Raw Student Database Loaded:")
print(df.to_string(index=False))
print("-"*50)
cgpa_criteria = df['CGPA']>= 7.5
backlog_criteria = df['Backlogs'] == 0
coding_criteria = df['Coding_Score_Pct'] >= 70
eligible_df = df[cgpa_criteria & backlog_criteria & coding_criteria]
final_shortlist = eligible_df.sort_values(by='Coding_Score_Pct', ascending=False)
print("\n ELIGIBLE STUDENTS SHORTLISTED FOR TECH DRIVE (Sorted by coding Merit):")
if final_shortlist.empty:
    print("No students met the eligible criteria.")
else:
    print(final_shortlist[['Student_ID','Name','Branch','CGPA','Coding_Score_Pct']].to_string(index=False))
print("-"*50)
final_shortlist.to_csv('placement_shortlist.csv', index=False)
print("SUCCESS: Shortlist exported securely to 'placement_shortlist.csv'!")
print("=============================================")