import sys
import os

# function to extract logs by specific date
# change log_file route with your log file path
def extract_logs_by_date(log_file="../logs_2024.log", date=None, output_dir="../output"):
    # If date is none sending a text to provide date.
    if date is None:
        print("Please provide a date in YYYY-MM-DD format.")
        sys.exit(1)

    # creating output file to save logs
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    # opening output_file with write condition
    with open(output_file, "w") as out_f:

        #opening log_file with read condition
        with open(log_file, "r") as log_f:

            #checking each line of log, if it stars with given date write it into output_file
            for line in log_f:
                if line.startswith(date):
                    out_f.write(line)
    
    #printing the confirmation message of saving the logs
    print(f"Log entries for {date} have been saved to {output_file}.")

#main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)
    
    date = sys.argv[1]
    extract_logs_by_date(date=date)
