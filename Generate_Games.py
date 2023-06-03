# Importing os module
import os
from pathlib import Path
import math
import subprocess
# Importing alive progress bar
# from alive_progress import alive_bar
# Importing spicy
import scipy.stats as stats

# Specifying the number of game runs
GAME_RUNS = 100
# Specifying the Script Name
SCRIPT_NAME = "./GameTest.py"

# Fetching the current working directory
WORKING_DIR = os.getcwd()
# Specifying the Output Directory
# OUTPUT_DIR = WORKING_DIR + "\\" + r"Logs\Time\1Sec_Vs_1Sec\\"
OUTPUT_DIR = Path(f"{WORKING_DIR}/Logs/Time/<TEMPLATE>")

# Specifying the Output Name
FILENAME = f"Game_"


# Builing String for the command
# COMMAND = f"python {SCRIPT_NAME} >> {OUTPUT_DIR}\\{FILENAME}"

# Checking if the directory exists
if os.path.exists(OUTPUT_DIR):
    # Deletable Files
    files_list = os.listdir(OUTPUT_DIR)
    # Iterating through each file in files list
    for each_file in files_list:
        # Removing the files
        os.remove(Path(f"{OUTPUT_DIR}/{each_file}"))
else:
    os.makedirs(OUTPUT_DIR)


# Storing the game results
game_results = []
flags = []
total_Avg = 0
avg_count = 0


def Find_Counts(lines):
    # This method is used to count the moves made and the iterations count per each move:
    count_of_moves = []
    count_of_iterations = []
    # Iterating through all the lines
    for each_line in lines:
        # Checking if the moves count line is present
        if "---------- Move Count:" in each_line:
            count_of_moves.append(each_line)
        elif "========== Total Iteration Count:" in each_line:
            # Creating a temporary string and removing un-necessary componenets
            temp = each_line.replace("========== Total Iteration Count:", "")
            temp = temp.replace("==========", "")
            temp = temp.strip()
            count_of_iterations.append(int(temp))

    return count_of_moves, count_of_iterations


def Check_Counts(moves_count, iteration_count):
    # Checking if both the lists are of same length
    if len(moves_count) == len(iteration_count):
        temp = 0
        # Adding all the values
        for each_value in iteration_count:
            temp = temp + each_value
        return temp/len(iteration_count), True

    else:
        return None, False

# Defining method to calculate the mean


def CalculateMean(list_data):
    # Initialising the total score
    total = 0
    # Iterating through all the elements to find the total
    for each_value in list_data:
        total = total + each_value
    # Calculating the mean
    total = total / len(list_data)
    # Returning the calculated mean value
    return total

# Defining method to calculate the median


def CalculateStandardDeviation(list_data, mean):
    """
    https://www.scribbr.co.uk/stats/standard-deviation-meaning/
    """
    # Initialising the deviation list
    deviation_list = []
    # Initialising the sum of squares
    sum_of_squares = 0
    # Iterating through all the sample values
    for each_value in list_data:
        # Calculating the deviation for each value
        deviation_value = each_value - mean
        # Squaring the deviation value value to remove the negatives
        deviation_value = deviation_value * deviation_value
        # Squarign the deviation value and adding to the list
        deviation_list = deviation_list + [deviation_value]
        # Calculating the sum of squares
        sum_of_squares = sum_of_squares + deviation_value

    # Finding the variance value
    variance = sum_of_squares / (len(deviation_list) - 1)
    # Finding the square root of the variance
    variance = math.sqrt(variance)
    # Returning the value
    return variance


# Initialising the Iterations
average_list = []
# Initializing the game run
# with alive_bar(GAME_RUNS, force_tty=True) as bar:
for num in range(1, GAME_RUNS+1):
    # Executing the 
    file = Path(f"{OUTPUT_DIR}/{FILENAME}{num}.txt")
    # with open(f"")
    subprocess.run(['python', f'{SCRIPT_NAME}'], stdout=open(f"{file}", "w"))
    # print(f"Command: {COMMAND}{num}.txt\n\n")
    # os.system(f"{COMMAND}{num}.txt")
    # print(f"Output Dir: {OUTPUT_DIR}, Filename: {FILENAME}, Number: {num}")
    # Opening the text file
    file = open(f"{file}", 'r')
    # Reading the contents of the file
    file_content = file.readlines()
    # Extracting the last line in the file
    end_line = file_content[-1]
    # Removing the new line character at the end
    new_line = end_line.replace("\n", "")
    # Adding the game result to the list
    game_results.append(new_line)
    # Finding the total number of moves and iterations
    moves, iterations = Find_Counts(file_content)
    # Fetching the required count from the lines
    avg_count, Correct_count = Check_Counts(moves, iterations)
    # Checking if count is correct or not
    if Correct_count:
        # Appending the average count to the list
        average_list = average_list + [avg_count]
        # Updating the total average
        total_Avg = total_Avg + avg_count
    # Appending the flags
    flags.append(Correct_count)
    # Closing the file
    file.close()
    # Displaying the progress
    # bar()
    print(f"Total Number of Games Played: {(num/(GAME_RUNS+1)) * 100}", end="\r")

# Calculating the probability of the win rate of each player
player_1_count = 0
player_2_count = 0
game_draw_rate = 0
for each_line in game_results:
    # each_line.replace("\n", "")
    # print(each_line)
    if each_line.lstrip() == "The game is won by Player X.":
        player_1_count += 1
    elif each_line.lstrip() == "The game is won by Player O.":
        player_2_count += 1
    elif each_line.lstrip() == "The game is draw.":
        game_draw_rate += 1

# Extracing unique elements
flags = list(set(flags))
all_checks = False
# Checking if the flags list contains only one element i.e., True
if (len(flags) == 1) and (flags[0] == True):
    all_checks = True

# Building game statistics string
game_statistics = f"Player 1 win rate: {((player_1_count/len(game_results))*100):.3f}, Player 2 win rate:{((player_2_count/len(game_results))*100):.3f}, Game Draw rate: {((game_draw_rate/len(game_results))*100):.3f}\nAverage Iteration count: {(total_Avg/GAME_RUNS):.3f} ...... {all_checks}"
# Displaying the game statistics string
print(game_statistics)

# Calculating Confidence interval
# Specifying the required confidence level
confidence_level = (1 - 0.95)/2
# Calculating the degrees of freedom i.e., game_runs - 1
df = GAME_RUNS - 1
# Calculating the t-statistics
t_value = abs(stats.t.ppf(confidence_level, df))
# Calculating the mean
mean_value = CalculateMean(average_list)
# Calculating the standard deviation
standard_deviation_value = CalculateStandardDeviation(average_list, mean_value)
# Calcuating Confidence Interval values
# mean +- t_value * (standard_deviation / sqrt(n))
std_error = t_value * (standard_deviation_value / math.sqrt(GAME_RUNS))
# Displaying the mean value and standard error
print(f"Mean Value: {(mean_value):.3f}, Standard Error: {(std_error):.3f}")
print(
    f"Confidence Interval: {(mean_value-std_error):.3f} , {(mean_value+std_error):.3f}")

# Creating the output CSV File
# Extracting the output to new file
file = open(Path(f"{OUTPUT_DIR}/GameResults.csv"), 'w')
for each_line in game_results:
    if each_line == 'The game is won by Player X.':
        file.write(f"Yes,No,No\n")
    elif each_line == "The game is won by Player O.":
        file.write(f"No,Yes,No\n")
    elif each_line == "The game is draw.":
        file.write(f"No,No,Yes\n")
# Adding the game statistics line
file.write(f"{game_statistics}")
# closing the required file
file.close()
