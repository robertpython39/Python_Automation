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
    # If folder doesn't exist, stop the process
    if not os.path.isdir(folder_path):
        print("Folder does not exist")
        return

    report_path = os.path.join(folder_path, "report.txt")

    with open(report_path, "w") as report_file:
        size = 0
        sorted_files = dict()
        for root, dirs, files in os.walk(folder_path):
            report_file.write(f"Selected folder:'{root}' has {str(len(files))} files\n\n")
            report_file.write(f"Files [with size]:\n")
            for f in files:
                # Exclude the report file
                if os.path.abspath(folder_path) == os.path.abspath(report_path):
                    continue

                try:
                    file_path = os.path.join(root, f)
                    file_size = os.path.getsize(file_path)
                    report_file.write(f"\t- {f}: {str(round(file_size / 1048576,2))} MB\n")
                    # Calculate total size of files:
                    size += file_size
                except OSError:
                    # pass over the inaccessible files
                    continue

            report_file.write("\n")
            report_file.write("Total Size:")
            report_file.write("\n")
            report_file.write(f"\t- {round(size / 1048576,2)} MB\n\n")
            report_file.write("Sorted files in descending order:\n")

            for f in files:
                file_path = os.path.join(root, f)
                file_size = os.path.getsize(file_path)
                sorted_files[f] = file_size

        for key in sorted(sorted_files, key=sorted_files.get, reverse=True):
            report_file.write(f"\t- {key}: {sorted_files[key]}\n\n")


if __name__ == "__main__":
    path = r"folder_path"
    file_size_reporter(path)