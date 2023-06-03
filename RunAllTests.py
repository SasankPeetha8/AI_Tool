from pathlib import Path
import os, subprocess

# Defining method to read and write the data
# Modify the file Game.py
def ReadRequiredFile(filename):
    data = None
    with open(file=filename, mode="r") as file:
        # Reading all the lines
        data = file.readlines()
        new_data = []
        # Iterating through all the lines
        for each_line in data:
        # Checking if the template exists
            if f"<TEMPLATE>" in each_line:
                # Replacing the string value
                temp = each_line.replace(f"<TEMPLATE>", f"{each_test}")
                new_data = new_data + [ temp ]
                # print(f"Replaced successfully")
            else:
                new_data = new_data + [ each_line ]
    # Returning the data
    return new_data

def WriteFile(filename, data):
    with open(file=filename, mode="w") as file:
        # Writing lines into the file
        file.writelines(data)

# Specifying the required test cases
required_test_cases = [ 0.0001, 0.001, 0.01, 0.1, 1]
# Iterating through all the test cases
for each_test in required_test_cases:
    contents = ReadRequiredFile(f"Game.py")
    WriteFile(f"GameTest.py", contents)
    contents = None
    contents = ReadRequiredFile(f"Generate_Games.py")
    WriteFile(f"Generate_Games_Test.py", contents)
    # Running the python test case:
    subprocess.run(['python', f".\Generate_Games_Test.py"], stdout=open(f"TestResults", "a"))
    # Deleting the file
    os.remove(f"GameTest.py")
    os.remove(f"Generate_Games_Test.py")
    