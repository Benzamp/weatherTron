# Benjamin Harrison
# bah26627@email.vccs.edu 


import calendar
import datetime

def main():
  banner()
  
  menuInput()

def banner():
  banner = '''
_______________________________________________________________
 _       __           __  __             ______               
| |     / /__  ____ _/ /_/ /_  ___  ____/_  __/________  ____ 
| | /| / / _ \/ __ `/ __/ __ \/ _ \/ ___// / / ___/ __ \/ __ \\
| |/ |/ /  __/ /_/ / /_/ / / /  __/ /   / / / /  / /_/ / / / /
|__/|__/\___/\__,_/\__/_/ /_/\___/_/   /_/ /_/   \____/_/ /_/ 
                                                              
_______________________________________________________________
  '''
  print(banner)

def userYearRanges():
  try:
    yearStart = int(input('Enter start year:'))
    yearEnd = int(input('Enter end year:'))
    if yearStart > yearEnd:
      print('The start year must be smaller than the end year. Try again.')
    return yearStart, yearEnd
  except ValueError:
    print('Your input was invalid. \nRestart the program and enter the year in the following format: YYYY\n(ex. 1985)')
    quit()
    

def menu():
  print('Welcome!  Please make a choice from the following menu\n')
  
  menu =''' 
  1. Show the banner again\n\
  2. View just a selected date range\n\
  3. Select a date range and show highest temperature\n\
  4. Select a date range and show lowest temperature\n\
  5. Select a date range and show the highest rainfall\n\
  6. Test text\n\
  7. See this menu again\n\
  8. QUIT the program\n'''
  print(menu)

def menuInput():

  try:
    
    menu()
    print('Your choice:\n')
    selection = int(input('Please make a selection:\n'))
    
    while True:
      
      if selection == 1:
        banner()
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()
        break
        
      elif selection == 2:
        yearStart, yearEnd = userYearRanges()
        showSelectedYearData(yearStart, yearEnd)
        
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()

      elif selection == 3:
        yearStart, yearEnd = userYearRanges()
        maxrain, maxtemp, mintemp = findHigh(yearStart, yearEnd)
        print(maxtemp)
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()

      elif selection == 4:
        yearStart, yearEnd = userYearRanges()
        maxrain, maxtemp, mintemp = findHigh(yearStart, yearEnd)
        print(mintemp)
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()

      elif selection == 5:
        yearStart, yearEnd = userYearRanges()
        maxrain, maxtemp, mintemp = findHigh(yearStart, yearEnd)
        print(maxrain)

        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()

      elif selection == 6:
        print('quack \n')
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()
      elif selection == 7:
        menuInput()
        # end the loop
        break
      elif selection == 8:
        print('Program Exiting. Thank you.\n')
        quit()
      else:
        print('invalid choice. Try again.\n')
        menuInput()
        break
  except ValueError:
    print('You must enter a number:\n')
    menuInput()

def getDataPref():
  selection = str(input('Enter \"R\" for rain, \"H\" for high temp, \"L\" for low temp:'))
  return selection.upper()
  
def openFile():
  file = open('weatherdata.txt', 'r')
  next(file)
  next(file)
  file = file.readlines()
  file = file[:-1]
  return file

def showSelectedYearData(yearStart, yearEnd):
  myList = wDataIntoList()
  header = ''' Date                   Rain    High T    Low T
-----                  ------    ----     ----'''
  
  print(header)
  for line in myList:
    date = line[0]
    year = date[-4:]
    if (int(year) >= int(yearStart) and int(year) <= int(yearEnd)):
      formatted = ('{}      {}      {}       {}'.format(line[0], line[1], line[2], line[3]))
      print(formatted)

def wDataIntoList():
  file = openFile()
  myList = []
  for line in file:
    date = line[102:110]
    dateFormat = datetime.datetime.strptime(date, "%Y%m%d").strftime("%B   %m, %Y")
    rain = line[111:115]
    hTemp = line[120:122]
    lTemp = line[129:131]
    data = (dateFormat, rain, hTemp, lTemp)
    myList.append(data)
  return(myList)
    
# determine the high temp, low temp and highest daily rainfall and print it out
# define the findHigh function with yearStart and yearEnd as parameters
def findHigh(yearStart, yearEnd):
  try:
    myList = wDataIntoList()
    message = 'The {} for the selected years was: {}{}'
    rain= []
    hTemp = []
    lTemp =[]
    for item in myList:
      date = item[0]
      year = date[-4:]
      if (int(year) >= int(yearStart) and int(year) <= int(yearEnd)):
        rain.append(item[1])
        hTemp.append(item[2])
        lTemp.append(item[3])
    maxrain = (message.format('highest rainfall', max(rain), '\"'))
    maxtemp = (message.format('highest temperature', max(hTemp), u'\N{DEGREE SIGN}'+'F'))
    mintemp = (message.format('lowest temperature', min(lTemp), u'\N{DEGREE SIGN}'+'F'))
    return maxrain, maxtemp, mintemp
  except ValueError:
    print('There is no data for the selected dates.\nMake sure that you enter valid years.')

main()
