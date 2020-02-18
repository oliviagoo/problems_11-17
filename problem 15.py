#problem 15
#olivia g 19/2/20
#this program will calculate how many pages have been printed


sheets = int(input("How many sheets printed before the printer jammed? "))
page_num = int(input("How many pages are there in a book? "))

books = sheets // page_num
pages = sheets % page_num

print("---------------")
print("Complete books printed: {}".format(books))
print("Unfinished book pages printed: {}".format(pages))
