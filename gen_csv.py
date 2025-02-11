import pandas as pd

# Input files
input_csv = "./csv/mid-evals-passed.csv"  # Replace with your input CSV file name
output_csv_excluded = "excluded_students.csv"  # Replace with the file name for the excluded users

# List of usernames to exclude
usernames_list = [
    "tanmay0996", "N-E-W-T-O-N", "AliHassan245", "dpgaharwal", 
    "jitendrasuthar1998", "Nishakulkarni06", "akshit2434", 
    "sammy0318", "Archi-shaw", "ikcod", "neeraj10122004", 
    "garvittsingla", "dipamsen", "biswajit-sarkar-007", 
    "Adi-204", "Akshat-Shu", "abhirajadhikary06", "712Kunal", 
    "SanikaBhalerao1345", "ShreyashSri", "ys-pro-duction", 
    "productsystem", "pragna7", "SHRUTISINHA250714", 
    "ad1tyayadav", "Atharvverma1234", "wildcraft958", "Waqibsk", 
    "R2-STAR", "SGI-CAPP-AT2", "Abankita", "ankit123-jh", 
    "saurabhhsinghh", "Bhoomish-Patel", "ThePhoenix08"
]

# Step 1: Read the input CSV file
df = pd.read_csv(input_csv)

# Step 2: Filter rows where the 'username' column does not match the usernames in the list
excluded_df = df[~df['username'].isin(usernames_list)]

# Step 3: Save the filtered DataFrame (users not in the list) to a new CSV file
excluded_df.to_csv(output_csv_excluded, index=False)

print(f"Excluded data saved to {output_csv_excluded}")
