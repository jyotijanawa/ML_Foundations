import pandas as pd
print("=== Starting Smart Student Analytics Pipeline ===")
student_data = {
    'Roll_No': [101,102,103,104,105],
    'Name': ['Abc','Bcd','Cde','Def','Efg'],
    'Attendence_Pct': [92,64,88,55,95],
    'Assignment_Score': [85,42,78,90,35]
}
df = pd.DataFrame(student_data)
print("\n--- Full Student Roster---")
print(df)
low_attendence_filter = df['Attendence_Pct'] < 75
short_attendence_students = df[low_attendence_filter]
print("\n Alert: Students with Short Attendence(< 75%):")
print(short_attendence_students[['Name','Attendence_Pct']])
top_performancers = df[(df['Attendence_Pct'] >= 90)&(df['Assignment_Score'] >= 80)]
print("\n Permium Performers  (Attendence >= 90% AND Score >= 80%):")
print(top_performancers)
print("==============================================")