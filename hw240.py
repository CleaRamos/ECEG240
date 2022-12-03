# VERSION 2022_11_02

#1: Letter Grade --------------------------------------------------------------
def thomas_letter_grade(pct):
   
  grade = ""
    if pct >=93:
        grade = "A"
    elif (pct >=90) and (pct <93):
        grade = "A-"
    elif (pct >= 87) and (pct <90):
        grade = "B+"
    elif (pct >=83) and (pct <87):
        grade = "B"
    elif (pct >= 80) and (pct <83):
        grade = "B-"
    elif (pct >= 77) and (pct <80):
        grade = "C+"
    elif (pct >=73) and (pct <77):
        grade = "C"
    elif (pct >= 70) and (pct <73):
        grade = "C-"
    elif (pct >= 67) and (pct <70):
        grade = "D+"
    elif (pct >=63) and (pct <67):
        grade = "D"
    elif (pct >= 60) and (pct <63):
        grade = "D-"
    else:
        grade = "F"
    return grade

#2 - is Ascending ---------------------------------------------------------------------------
def is_ascending (items):
  ascending = True
  counter = 0
  run_times = len(items) -1
  print(len(items))
  #accepts a list and itterates through list
  
  if (len(items) <=1):
    return (ascending)
  
  while counter < run_times:
    print(f'{counter}: {items[counter]}, {items[counter +1]}')
    if items[counter] >= items[counter+1]:  
      ascending = False
      return ascending
      break
    counter += 1
  return ascending


#3 - Temperature Conversion -------------------------------------------
def f_to_celsius(fahrenheit):
  c = (fahrenheit-32)*(5/9)
  return (c)

#4 - Formated Temperature Conversion ------------------------------------------------------------------------
def f_to_celcius_str(fahrenheit):
  c = (fahrenheit-32)*(5/9)
  return (f'{c:.2f}')


#5 - Only Odd Digits -----------------------------------------------------------------------
def only_odd_digits(n):
  has_odd = True
  even_nums = [2,4,6,8]

  if n==0:
    return False

  #checking if last digit is false
  while n>0:
    last_dig = n%10
    for i in even_nums:
      if i == last_dig:
        has_odd = False
        return(has_odd)
    n = n//10
  return(has_odd)

#6 & 7 - Crossword Solver ----------------------------------------------------------------------
#SKIP
def crossword_solver_exact_case(word):

# converting words into a dictionary array
  dictionary = []
  fp = open("words.txt", "r")
  for line in fp:
    ln = line.strip()
    dictionary.append(ln)
    
  fp.close

  w_index = 0
  potential_words = []

  #itterate through string until you find a dasn
  while w_index < len(word):
    current_letter = word[w_index]
    if current_letter != "-":
      #itterate through dictionary
      for i in dictionary:
        if len(i) == len(word):
          if i[w_index] == current_letter:
            potential_words.append(i)
    w_index += 1

  return(potential_words)


  #maybe I should splice?? once i find a dash and compare words that have the same ???


    


print(crossword_solver_exact_case('o-f'))


    




#8 Letter Frequency ----------------------------------------------------------------
def letter_pattern_frequency(letters):
 
  dictionary = []
  fp = open("words.txt","r")
  for line in fp:
    ln = line.strip()
    dictionary.append(ln)
  fp.close

  count = 0
  total_words = len(dictionary)
  
  for i in dictionary:
    if (letters in i) == True:
      count += 1
  
  return (count, 100*(count/total_words))


#9 Recursive Sum of a List ----------------------------------------------------------------

def recursive_list_sum(numbers):
  n = len(numbers)
  if len(numbers) == 0:
    return 0
    
  if n == 1:
    return numbers[0]
  return (numbers[0] + recursive_list_sum(numbers[1:]))

  
 #10 Freqency Dictionary ----------------------------------------------------------------
def dictionary_counter(list):
  new_dict = {}
  for i in list:
    if i in new_dict.keys():
      new_dict[i]+=1
    else:
      new_dict[i] = 1
  return new_dict


 #11 Sort array by element frequency ----------------------------------------------------------------
#SKIP

#use dictionary function from problem 10
# findout sort elements in frequency from greatest to least
  # append that element _# of times to a new array?



#12 Perfect Powers ----------------------------------------------------------------
def is_perfect_power(n):
  b = 2
  e = 2
  while b < n:
    while e < n:
      result = b^e
      if result == n:
        return False
      e+=1
    b+=1
  return True



#13 Break a word into syllables --------------------------------
#I DON'T UNDERSTAND THIS - MY CODE IS NOT CORRECT
def break_into_syllables(word,syllables):

  for i in syllables:
    if (i in word) == False:
      return False
    else:
      return True

#print(break_into_syllables("hello",['hel', 'hol', 'llo','he']))
#print(break_into_syllables("world",['woo','wor','rld','or']))
#print(break_into_syllables("banana",['na','ba']))

#14 Domino Cycle --------------------------------
def domino_cycle(tiles):
  if (len(tiles) == 0):
    return True
  
  itterations = len(tiles) 
  tiles.append(tiles[0])

  is_cycle = False
  index = 0
  while index < itterations:
    if tiles[index][1] == tiles[index+1][0]:
      is_cycle = True
      index += 1
    else:
      return False
  return is_cycle

#15 And sometimes... WHY?!? --------------------------------
def disemvowel(text):
  #vowels = ['a','e','i','o','u']
  vowels = 'aeiou'
  y = 'y'
  index = len(text)-1
  while index >= 0:
    if (text[index] ==  y):
      if ((text[index-1] in vowels) or (text[index+1] in vowels)) == True:
        text = text[0:index] + text[index+1:]
    index -= 1

  index2 = len(text)-1
  while index2 >= 0:
    if (text[index2] in vowels) == True:
      text = text[0:index2] + text[index2+1:]
    index2 -= 1 

  return text


  
#16 Endless Ant --------------------------------
def endless_ant(moves):

  #idex of the letter in "moves"
  index = 0
  
  orientation = ('N', 'E', 'S', 'W')
  #starting coordinate
  coor = (0,0)
  #keeps track of index of coordinate in oreintation list
  c_index = 0
  current = orientation[0]
  
  while index < len(moves):
    if moves[index] == 'F':
      if current == 'N':
        coor = (coor[0], coor[1]+1)
      elif current == 'E':
        coor = (coor[0]+1, coor[1] )
      elif current == 'S':
        coor = (coor[0] , coor[1]-1)
      elif current == 'W':
        coor = (coor[0] -1, coor[1])
        
    elif moves[index] == 'R':
      if c_index == 3:
        c_index = 0
      else:
        c_index += 1

    elif moves[index] == 'L':
      if c_index == 0:
        c_index = 3
      else:
        c_index -= 1
        
    current = orientation[c_index]
    index += 1
  
  return (coor)

   
    