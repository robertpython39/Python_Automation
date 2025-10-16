"""
Write a script that lists all files in a given folder along with their sizes, then calculates the total folder size.
Goal:
Use os.path.getsize() and format file sizes (KB, MB).
Bonus:
Generate a report.txt file with the sum of results and sorted files in descending order by size.
"""

# --------------- Imports ---------------
import os

def file_size_reporter(folder_path):
    """
    Formula:
    B / 1048576 = MB
    Calculation:
    1024 B / 1,048,576 = 0.000977 MB
    End result:
    1024 B is equal to 0.000977 MB
    """
        size = 0
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                file_path = os.path.join(root, f)
                    file_size = os.path.getsize(file_path)
                    # Calculate total size of files:
                    size += file_size
            report_file.write("\n")
            report_file.write("\n")
            for f in files:
                file_path = os.path.join(root, f)
                file_size = os.path.getsize(file_path)


if __name__ == "__main__":
    path = r"C:\Users\Intel Test\Desktop\Wallpapers"
    file_size_reporter(path)