# Assuming that the input file is named data.txt,
# we use the following command in Unix to extract
# the scheme name and net asset value and save it 
# in a CSV file named output.csv:





awk -F';' 'NR>2 {print $4","$5}' data.txt | sed '1 i\Scheme Name,Net Asset Value' > output.csv





# Here's what each part of the command does:

# awk -F';': Sets the delimiter to ; for the input file.
# NR>2: Skips the first two lines of the input file.
# print $4","$5: Prints the fourth and fifth fields separated by a comma.
# sed '1 i\Scheme Name,Net Asset Value': Inserts the header row at the beginning of the output.
# > output.csv: Redirects the output to a CSV file named output.csv.
