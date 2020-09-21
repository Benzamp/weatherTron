# Benjamin Harrison
# bah26627@email.vccs.edu 

# Purpose: find data based on user input.


# imports.  Probably should leave this alone!
import calendar
import datetime
# ************ 

# Control the flow of the program
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

# Ask the user for year ranges
def userYearRanges():
  # test for valid input
  try:
    # ask the user for input and store it as an iteger to the
    # variable yearStart
    yearStart = int(input('Enter start year:'))
    # ask the user for input and store it as an iteger to the
    # variable yearEnd
    yearEnd = int(input('Enter end year:'))
    # if the value for yearStart is greater than teh value of yearEnd..
    if yearStart > yearEnd:
      # display a message to the screen
      print('The start year must be smaller than the end year. Try again.')
    # return the variables yearStart and yearEnd
    return yearStart, yearEnd
  # if a ValueError is triggered...
  except ValueError:
    # display a message to the screen
    print('Your input was invalid. \nRestart the program and enter the year in the following format: YYYY\n(ex. 1985)')
    # end the program
    quit()
    

# define the menu function
def menu():
  # display a welcome message to the screen
  print('Welcome!  Please make a choice from the following menu\n')
  # display the menu to the screen, each on separate lines
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

# define the menuInput function
def menuInput():
  
  # put the code in a try statement to test for bad input
  try:
    
    # call the menu function to display the menu
    menu()
    # display a message to the screen
    print('Your choice:\n')
    
    # display a message, take user input, and save the input as
    # a integer to the variable selection
    selection = int(input('Please make a selection:\n'))
    
    # begin a while True loop
    while True:
      
      # if the user enters the number 1
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
        # end the loop
        break
      # if the user enters the number 2
      elif selection == 2:
        yearStart, yearEnd = userYearRanges()
        showSelectedYearData(yearStart, yearEnd)
        # end the loop
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()
      # if the user enters the number 3
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
      # if the user enters the number 4
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
      # if the user enters the number 4
      elif selection == 5:
        yearStart, yearEnd = userYearRanges()
        maxrain, maxtemp, mintemp = findHigh(yearStart, yearEnd)
        print(maxrain)
        # end the loop
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()
      # if the user enters the number 6
      elif selection == 6:
        # display a message
        print('quack \n')
        # end the loop
        select = str(input('Press \'q\' to quit or \'m\' to return to menu'))
        if select == 'q':
          quit()
        if select == 'm':
          menuInput()
        else:
          print('You have entered an invalid character. Quitting...')
          quit()
      # if the user enters the number 7
      elif selection == 7:
        # call the menuInput function
        menuInput()
        # end the loop
        break
      # if the user enters the number 8
      elif selection == 8:
        # display a message
        print('Program Exiting. Thank you.\n')
        # end the loop
        quit()
      # if none of the above conditions are met
      else:
        # display a message
        print('invalid choice. Try again.\n')
        # call the menuInput function
        menuInput()
        # end the loop
        break
  # if a ValueError is raised
  except ValueError:
    # display a message
    print('You must enter a number:\n')
    # call the menuInput function
    menuInput()



# ask the user what what data to gather (rain, high temp, low temp)
def getDataPref():
  # ask the user for input and storeit to the variable selection
  selection = str(input('Enter \"R\" for rain, \"H\" for high temp, \"L\" for low temp:'))
  # make sure the value of selection is uppercase and return it
  return selection.upper()
  
# opens the character file
# returns one file handler containing file by lines
def openFile():
  # create a handler file for the text file and open it in read mode
  file = open('weatherdata.txt', 'r')
  # use the code on the next two lines to remove the heading
  # from the file
  next(file)
  next(file)
  # read each line of the file individually
  file = file.readlines()
  # remove the last line from the file (it was blank and creating 
  # errors with the code)
  file = file[:-1]
  # return the file
  return file

# shows all days, and data for that year
# hint: include text headers at the beginning to get pretty columns
def showSelectedYearData(yearStart, yearEnd):
  # call the wDataIntoList function and store the output to the
  # variable myList
  myList = wDataIntoList()
  # create a heading for the ouput and store it to the variable header
  header = ''' Date                   Rain    High T    Low T
-----                  ------    ----     ----'''
  # display the header to the screen
  print(header)
  # iterate through the contents of myList
  for line in myList:
    # find the first object in line and store it to the 
    # variable date
    date = line[0]
    # find the last four characters of the date object and store it
    # to the variable year
    year = date[-4:]
    # if the year is greater than yearStart and less than yearEnd...
    if (int(year) >= int(yearStart) and int(year) <= int(yearEnd)):
      # properly format the lines of the list that fit within the
      # desired dates
      formatted = ('{}      {}      {}       {}'.format(line[0], line[1], line[2], line[3]))
      # display this formatted text to the screen
      print(formatted)

#****************** Data to list **************
# Reads selected weather data into a list to be used by other functions
# Receives the start year, end year, and type of data required
#hints: accept the start year, end year and the user selection.
#     Call to open the file
#     Create a list
#     Check each line to see if it contains the date you need to gather data from
#     Use a loop to pull the relevant data for each user selection into a list
#     Return the list of just the dates and relevant data
def wDataIntoList():
  # call the openFilefunction and store its output to the variable file
  file = openFile()
  # create an empty list called myList
  myList = []
  # iterate through each line of the file
  for line in file:
    # store characters at the specified index to the variable date
    date = line[102:110]
    # convert the date from YYYYMMDD format to  Month DD, YYYY and
    # store it to the variable dateFormat
    dateFormat = datetime.datetime.strptime(date, "%Y%m%d").strftime("%B   %m, %Y")
    # store the characters at the specified index to the variable rain
    rain = line[111:115]
    # store the characters at the specified index to the variable hTemp
    hTemp = line[120:122]
    # store the characters at the specified index to the variable lTemp
    lTemp = line[129:131]
    # place the variables in order and store them to the variable data
    data = (dateFormat, rain, hTemp, lTemp)
    # add these values to myList
    myList.append(data)
  # return myList
  return(myList)
    
# determine the high temp, low temp and highest daily rainfall and print it out
# define the findHigh function with yearStart and yearEnd as parameters
def findHigh(yearStart, yearEnd):
  # error handling
  try:
    # call the wDataIntoList function and store the output to the 
    # variable myList
    myList = wDataIntoList()
    # create a message ready to be formatted and store it to the variable selection
    message = 'The {} for the selected years was: {}{}'
    # create an empty list named rain
    rain= []
    # create an empty list named hTemp
    hTemp = []
    # create an empty list named lTemp
    lTemp =[]
    # iterate through the items in myList
    for item in myList:
      # find the first object in the line and store it to the variable
      # date
      date = item[0]
      # find the last four characters of the object and store them to
      # to the variable year
      year = date[-4:]
      # if the year is greater than or equal to yearStart and
      # is less than or equal to the yearEnd...
      if (int(year) >= int(yearStart) and int(year) <= int(yearEnd)):
        # add the item at the 1 index to the list rain
        rain.append(item[1])
        # add the item at the 2 index to the list hTemp
        hTemp.append(item[2])
        # add the item at the 3 index to the list lTemp
        lTemp.append(item[3])
    # display a message to the screen with the largest value from the
    # rain list
    maxrain = (message.format('highest rainfall', max(rain), '\"'))
    # display a message to the screen with the largest value from the
    # hTemp list and the degrees symbol
    maxtemp = (message.format('highest temperature', max(hTemp), u'\N{DEGREE SIGN}'+'F'))
    # display a message to the screen with the largest value from the
    # lTemp list and the degrees symbol
    mintemp = (message.format('lowest temperature', min(lTemp), u'\N{DEGREE SIGN}'+'F'))
    return maxrain, maxtemp, mintemp
  # if a ValueError is raised...
  except ValueError:
    # display a message to the screen
    print('There is no data for the selected dates.\nMake sure that you enter valid years.')

# call the main function and execute the code
main()
