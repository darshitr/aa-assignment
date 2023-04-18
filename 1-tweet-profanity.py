# The input file contains tweets in text format, with each tweet on a new line.
# The set of racial slurs provided is in lowercase.
# The degree of profanity for each sentence will be calculated based on the number of racial slurs present in it.




# Set of racial slurs
racial_slurs = {'slur1', 'slur2', 'slur3'}

# Function to calculate degree of profanity
def profanity_degree(tweet):
    words = tweet.split()
    num_slurs = sum([1 for word in words if word in racial_slurs])
    return num_slurs / len(words)

# Open input file and process each line
with open('tweets.txt', 'r') as file:
    for line in file:
        tweet = line.strip()
        degree = profanity_degree(tweet)
        print(f"Tweet: {tweet}\nDegree of profanity: {degree}\n")
