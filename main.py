import requests
import urllib

response = requests.get("http://www.google.com")


def main():


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
         #readingList.append selected book 
         print('Loading seletions... Please wait')
      
      elif choice == 2:
         print('Displaying Reading List \n =====================')
         for i in range(len(readingList)):
            print(readingList)

      elif choice == 3:
         print('Terminating program')

   print('Come Back Soon!')

   
if __name__ == '__main__':
   main()