#problem 15
#olivia g 19/2/20
#this program will calculate how many pages have been printed

#getting input - sheets before jam and pages per book
sheets = int(input("How many sheets printed before the printer jammed? "))
page_num = int(input("How many pages are there in a book? "))

#process - calculating whole books and unfinished book pages
books = sheets // page_num
pages = sheets % page_num

#formatted output
print("---------------")
print("Complete books printed: {}".format(books))
print("Unfinished book pages printed: {}".format(pages))
