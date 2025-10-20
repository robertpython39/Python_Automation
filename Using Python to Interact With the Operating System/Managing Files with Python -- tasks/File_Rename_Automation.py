"""
Create a script that renames all files in a folder by adding a prefix (e.g., project_) or a timestamp to their names.
Goal:
Use os.rename() and string manipulation.
Bonus:
Save both the old and new filenames to a CSV file (rename_log.csv).
"""

import os
import datetime
import csv

def file_rename(file_path):
    # If folder doesn't exist, stop the process
    if not os.path.isdir(file_path):
        print("Folder does not exist")
        return

    # Retrieve the datetime and format it to: YYYYMMDD
    current_date = datetime.datetime.now()
    formated_date = current_date.strftime("%Y%m%d")

    #Collect old name from files
    old_names = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        # Ignore directories and hidden files
        if (os.path.isfile(path=full_path) and not file.startswith('.')) and (not file.startswith('_') and not file.endswith('.csv')):
            old_names.append(file)
            print(old_names)

    # Generate the report file (in the root of the folder path)
    report_path = os.path.join(file_path, "report.csv")

    # Write to the csv file the datetime, old name, new name and rename the files inside the folder with the new name
    with open(report_path, "w") as report_file:
        report_writer = csv.writer(report_file)
        report_writer.writerow([formated_date, "old_name", "new_name"])
        for old_name in old_names:
            new_name = f"{formated_date}_{old_name}"
            old_full_path = os.path.join(file_path, old_name)
            new_full_path = os.path.join(file_path, new_name)

            try:
                os.rename(old_full_path, new_full_path)
                report_writer.writerow([formated_date, old_name, new_name])

            except Exception as e:
                print(f"Could not rename {old_name}: {e}")


if __name__ == "__main__":
    folder_path = r"folder_path"
    file_rename(folder_path)