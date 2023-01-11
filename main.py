import requests

class Book:
   def __init__(self, title, author, publisher):
      self.title = title
      self.author = author
      self.publisher = publisher
   @staticmethod
   def get_book_info(user_search):
      api_url = 'https://www.googleapis.com/books/v1/volumes?q='+user_search+'&maxResults=5'
      response = requests.get(api_url).json()
      items = response['items']
      book_list = []
      for i in range(0,len(response['items'])):
        title = items[i]['volumeInfo'].get('title', 'Not Listed')
        #only grabbing first author in array
        author = items[i]['volumeInfo'].get('authors', ['Not Listed'])[0]
        publisher = items[i]['volumeInfo'].get('publisher', 'Not Listed') 
        book_info = [title, author, publisher]
        book_list.append (book_info)
      return book_list
   
def main():
   try:
      # creating book list 
      readingList = []
      infile = open('userBooks.txt', 'r')
      line = infile.readline()
      while line:
         readingList.append(line.rstrip('\n').split(',')
         )
         line = infile.readline()
      infile.close()

   except FileNotFoundError :
      print('the <userBooks.txt> file is not found!')
      print('initializing <userBooks.txt>...')
      readingList = []

   #menu options for user to pick
   choice = 0
   while choice !=3:
      print ("***PY Book Search***")
      print('1) Search a book')
      print('2) Display Reading List')
      print('3) Quit')
      choice = int(input())
     
      if choice == 1: 
         user_search = input ('What would you like to search?\n')
         print('Loading seletions... Please wait')
         print(user_search)
         print()
       
         book_list= Book.get_book_info(user_search)

         for i in range(0,len(book_list)):
            title = book_list[i][0]
            author = book_list[i][1]
            publisher = book_list[i][2]
            print('title: ',title)
            print('author: ',author)
            print('publisher: ',publisher)
            print()

         while True:
            user_selection= int(input('Like these books? Enter number between 0-4 to save\n book to your Reading List. \nIf not, press 5 to return to menu.\n'))
            if user_selection >= 0 and user_selection <=4:
               title = book_list[user_selection][0]
               author = book_list[user_selection][1]
               publisher = book_list[user_selection][2]
               book_info = [title, author, publisher]
               readingList.append (book_info)
 
            elif user_selection == 5:
               print('Back to menu...')
               break

            else:
               print('Please enter number between 0 and 4\n to save a book or 5  to return to menu')
      
      elif choice == 2:
         print('Displaying Reading List \n =====================')
         for i in range(len(readingList)):
            print('Title: '+ readingList[i][0])
            print('Author: '+ readingList[i][1])
            print('Publisher: '+ readingList[i][2])
            print()

      elif choice == 3:
         print('Terminating program')

   print('Come Back Soon!')

   outfile = open('userBooks.txt', 'w')
   for book_info in readingList:
      outfile.write(','.join(book_info) + '\n')
   outfile.close()

   
if __name__ == '__main__':
   main()