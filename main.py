import requests
import urllib


def main():

   userSearch = 'more than a carpenter'
   api_url = 'https://www.googleapis.com/books/v1/volumes?q='+userSearch+'&maxResults=5'
   response = requests.get(api_url).json()
   items = response['items']
  
   for i in range(2,len(response)+1):
      title = items[i]['volumeInfo']['title']
      author = items[i]['volumeInfo']['authors']
     # publisher = items[i]['volumeInfo']['publisher']  For some reason the publisher would not work...

   
   print(title)
   print(author)
   #print(publisher)

   try:
      # creating book list 
      readingList = []
      infile = open('userBooks.txt', 'r')
      line = infile.readline()
      while line:
         readingList.append(line.rstrip('\n').split(','))
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
         userSearch = input ('What would you like to search?')

         print('Loading seletions... Please wait')
         print(userSearch)

         api_url = 'https://www.googleapis.com/books/v1/volumes?q='+userSearch+'&maxResults=5'
         response = requests.get(api_url).json()
         items = response['items']
      
         for i in range(5,len(response)+1):
            title = items[i]['volumeInfo']['title']
            author = items[i]['volumeInfo']['authors']
            book = [title, author]
        
            return(book)
         book = [items[i]['volumeInfo']['title'], items[i]['volumeInfo']['authors']]
         print(book)

        
      
      elif choice == 2:
         print('Displaying Reading List \n =====================')
         for i in range(len(readingList)):
            print(readingList)

      elif choice == 3:
         print('Terminating program')

   print('Come Back Soon!')

   outfile = open('userBooks.txt', 'w')
   for book in readingList:
      outfile.write(','.join(book) + '\n')
   outfile.close()

   
if __name__ == '__main__':
   main()