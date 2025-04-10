import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

negative =  ["dirty", "uncomfortable", "noisy", "rude", "disappointing", "poor", "expensive", "unfriendly", "stale", "inadequate", "smelly", "outdated", "misleading", "unresponsive", "unhygienic", "chaotic", "horrible", "bad", "frustrating", "unsafe", "cold"]
    
positive = ["clean", "comfortable", "quiet", "friendly", "enjoyable", "excellent", "affordable", "welcoming", "good", "modern", "fresh", "helpful", "responsive", "convenient", "hygienic", "charming", "nice", "pleasant", "satisfying", "safe", "perfect"]    

noises = [".",",","?",")","(",":",";","_", "-", " ́", "*", "!", "[", "]", "{", "}", "@", "%"]

df = pd.read_csv("Hotel.csv")

def Task1():
    # (a) Find the name of the hotel with the highest number of records and print it (H1).
    loc = df["hotel_name"].value_counts().dropna() # use value_counts to to order the hotel_name column by the number of occurences of each hotel it contains and use dropna to remove any empty row to clean the data
    print("Most visited Hotel: ",loc.head(1)) #print statement thats takes my filtered datadrame and prints the first head value which will displaythe most visited hotel
    
    # (b) Extract rows/records where the hotel name is the one found in the last step (H1) and, from these extracted rows, print the unique country names (Nationality).
    cnt = df.loc[df["hotel_name"] == loc.index[0]] # use the loc function to extract all rows where the hotel name column value is equal to loc.index[0] which is the hotel i found in the last task
    print(cnt["nationality"].dropna().unique()) # print statement utilising the unique() function to print all unique countries found in the extracted rows
    
    # (c) Find the name of the hotel with the second-highest number of records and print it (H2).
    loc2 = df["hotel_name"].value_counts().dropna() 
    name = loc2.index[1] # creates a variable containing the name of tne 2nd most visited hotel
    count = loc2.iloc[1] # creates a variable containing the count of the 2nd most visited hotel
    print("Second most visited hotel: ",name,count)
    
    # (d) Extract rows/records where the hotel name is the one found in the last step (H2) and, from these extracted rows, print the unique country names (Nationality).
    cnt2 = df.loc[df["hotel_name"] == loc2.index[1]] # pretty much does the same as my code for part b just the index is swapped to the 2nd most visited instead of the first
    print(cnt2["nationality"].dropna().unique())    
Task1()

def Task2():
    # (a) Find and print the list of unique "M" values from the entire dataset in the "reviewed_at" column
    loc = pd.to_datetime(df["reviewed_at"],errors="coerce").dt.month_name().dropna().unique() # converts the reviewed_at column to a date object which alows me to extract the month value then use dropna to clean empty rows and use unique to print the unique months listed
    print(loc)
    
    # (b) Replace each "M" with its corresponding numerical value. For instance, "Aug" should be replaced with 08. Print the updated "reviewed_at" column
    months = {"Jan":"01", "Febuary":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"} # created a dictionary of months to use to swap out the string month value withthe new int month value
    date = pd.to_datetime(df["reviewed_at"], errors="coerce").replace(months) # convert the reviewed_at column to a date object then use replace() to replace the string months wtih int months using the months dictionary for values
    print(date)
    
    #(c) Fill empty cells with the least frequent year in the column
    df['reviewed_at'] = pd.to_datetime(df['reviewed_at'], errors='coerce')
    yearsna = df["reviewed_at"].dt.year # extract only the year value from the reviewed_at column
    leastyear = yearsna.value_counts().idxmin() # use value_counts to count each year and use idxmin to extract to oldest year 
    leastdate = pd.to_datetime(f"01-01-{int(leastyear)}") # create a  new date object called leastyear 
    df["reviewed_at"] = df["reviewed_at"].fillna(leastdate) # use fillna() to fill each nan row value with the oldest year
    print(pd.to_datetime(df["reviewed_at"]).dt.year) # print statement returning the the column of year values from reviewed_at
    
    # (d) graph visually
    
    labels = ["2018","2019","2020","2021"] # graph labels for x axis
    index = np.arange(1, len(labels)+1) # index for the graph
    width = 0.35 # width value for bar chart
    
    yearcount = df["reviewed_at"].dt.year.value_counts() # returns a dataframe of the years found in the reviewed_at column
    yearcount = yearcount.loc[yearcount.index.isin([2018,2019,2020,2021])].reindex([2018,2019,2020,2021], fill_value=0) # use loc to find the years then use reindex to match the correct year not using reindex would create a graph going from biggest to smallest
    
    colors = ["red","green","blue","orange"] # colors for each bar i nthe graph
    plt.bar(index, yearcount, width, color=colors, label=labels) # plots a bar graph using the previously defined values
    plt.xlabel("Year") # sets the xlabels name to "year"
    plt.ylabel("# of bookings") # sets the ylabel name to "# of bookings"
    plt.title("# of hotel bookings by year") # sets the title of the graph
    plt.legend(labels) # create a legend to indcate each bars meaning
    plt.xticks(index, labels) # sets the xticks to the labels list using index to specify hjow many xticks needed
    plt.show() # displays the graph
Task2()
    
def Task3():
    # (a) cleaning
    def cleaning(words): # make a nested function to apply data cleaning using the provided noises list
        for i in noises: # for loop to iterate through each word 
            words = words.replace(i,"") # replaces every word with the same word but missing any noises found inside the noise list
        return words # returns the cleaned word
    
    # (b) Extract rows/records where the review (in the "review_text" column) contains at least two terms from the positive hard-coded list.
    df["clean_review"] = df["review_text"].dropna().apply(cleaning) # create a clean dataframe by using apply() to clean the review_text column and use dropna to get rid of empty rows
    data = df["clean_review"]
    
    pos = data.str.count('|'.join(positive)) >= 2 # converts to a string then counts each word before comparing against the positive list and finally returns all rows where the count of positive words is greater than or equal to 2
    print(data[pos],"\n")
    
    # (c) average for positive
    posdf = df[pos] # create a dataframe of postive reviews
    pos_avg = posdf["rating"].mean() # create a dataframe of the ratings from only positive reviews
    print(f"Average rating of positive shows is: {pos_avg:.2f}","\n") # print the average to 2 decimal points
    
    # (d) Extract rows/records where the review (in the "review_text" column) contains at least two terms from the negative hard-coded list
    ngtv = data.str.count('|'.join(negative)) >= 2 # the following code is the same as how i got the positive values just reversed to find the negative reviews and average
    print(data[ngtv],"\n")
    
    # (e) average for negative
    ngtvdf = df[ngtv]
    ngtv_avg = ngtvdf["rating"].mean()
    print(f"Average rating of megative shows is: {ngtv_avg:.2f}")   
Task3()

def Task4():
    # (a) There is a column in the dataset named tags. Remove rows/records where the tags column has no content.
    tag = df.dropna(subset=["tags"]) #use dropna to remove empty rows from the data
    
    #(b) The tags column explains the details of the trip. Extract those rows/records where the value in tags starts with either Business, Leisure, or Solo.
    tag = tag[tag["tags"].str.startswith(("Business","Leisure","Solo"))] # create a new tag dataframewhich converts the tags columnto string then checks every row for rows that start with the given strngs and returns them
    print(tag) # print the filtered tag column
    
    # (c) For each of the above categories, calculate the average rating and display the results visually.
    business = tag[tag["tags"].str.startswith("Business")] # create 3 dataframes for each keyword
    Leisure =  tag[tag["tags"].str.startswith("Leisure")]
    Solo = tag[tag["tags"].str.startswith("Solo")]
    #print("Average for business: ",business["rating"].mean())
    #print("Average for Leisure: ",Leisure["rating"].mean())
    #print("Average for Solo: ",Solo["rating"].mean())
    
    labels = ["Business","Leisure","Solo"] # graph labels
    fig,ax = plt.subplots() # use subplots to plot multiple graphs
    ax.boxplot([business["rating"],Leisure["rating"],Solo["rating"]], labels=labels) # create 3 boxplots to visuaize the data for the 3 keywords to be compared
    ax.set_xlabel("Average ratings")
    ax.set_ylabel("Score")
    ax.set_title("Comparison of the Mean value between Business, Leisure and Solo")
    
    plt.show()
    # (d) Write a one-line comment explaining the findings
    # All 3 plots have similiar median values indicating the average review score all greater than 8 so the hotels were well liked, also the interquartile range on each plot are small so the majority of the data is close tothe median and all 3 plots contain outliars but they arent frequent enough to skew the data.
Task4()    

def Task5():
    
    # extract nationality and rating then print the average rating of every country going from highest rating to lowest
    cnt = df.dropna(subset=["nationality"]) # use dropna to clean the data
    avg = cnt.groupby("nationality")["rating"].mean() # use groupby to group the data based on nationality then get the averatge rating of each country
    sortavg = avg.sort_values(ascending=False) # order the values going from highest average review to the lowest
    print(sortavg)
    # extract 2 vatiables where one is the row of ratings greater than 7.0 and the other is the rows of ratings less than 7.0
    
    gt = cnt[cnt["rating"] >=7.0] # create a dataframe which contans only the rows where the rating is higher than 7/10
    greater = gt["rating"]
    lt = cnt[cnt["rating"] <=7.0] # creates a dtaframe which contans only the rows where the rating is lower than 7/10
    less = lt["rating"]
    # Displaying the values extracted visually
   
    fig,(ax1,ax2) = plt.subplots(1,2) # use subplots so i can plot mutiple graphs
    ax1.boxplot(sortavg) # create a boxplot of the country averages
    ax1.set_title("Average rating by country")
    ax1.set_ylabel("Average rating")
    ax1.set_xlabel("Countries")
    
    pievalue = [len(greater),len(less)] # values for the piechart
    pielabels = ["Greater than 7.0","Less than 7.0"] # piechart labels
    
    ax2.pie(pievalue, labels=pielabels, autopct='%1.1f%%') # create a piechart that display the % of positive review score >7 and % of negative review scores <7, i use autopct to add the % of both to the chart
    ax2.legend(pielabels, loc="upper right")
    ax2.set_title("Comparison of ratings less than or greater than a given value (7.0)")
    plt.show()   
Task5()

    