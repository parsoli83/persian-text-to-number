#DESCRIPTION:
#this func is made to handle persian numeric inputs
#when you call it, it uses "CompleteVoiceAnalyse()" as voice analyzer
#then if the word was a numeric_string it will change its format to int and returns it
#otherwise it will return False
############################################################
#ATTENTION:IT CAN JUST CHANGE NUMBERS TYPE FROM 0 TO 999
############################################################
import numpy as np
def numeric_input(persian_number_string):
  #i use this list to find out if the word is a number or not
  l_persian_number_strings=np.array([
    #zero:
    [
      ["صفر","صفرم","هیچ"]
    ],
    #1_digit numbers:
    [
      ["یک","اول","نخست"],
      ["دو","دوم"],
      ["سه","سوم"],
      ["چهار","چار","چهارم"],
      ["پنج","پنجم"],
      ["شش","شیش","شیشم","ششم"],
      ["هفتم","هفت"],
      ["هشت","هشتم"],
      ["نه","نهم"]
    ],
    #2_digit numbers >>> 11 to 19:
    [
      ["یازده","یازدهم"],
      ["دوازده","دوازدهم"],
      ["سیزده","سیزدهم"],
      ["چارده","چهارده","چاردهم","چهاردهم"],
      ["پانزده","پونزده","پانزدهم","پونزدهم"],
      ["شانزده","شونزده","شانزدهم","شونزدهم"],
      ["هفدهم","هیوده","هیفدهم","هوده","هیودهم","هفده","هیفده","هودهم"],
      ["هیجده","هیجدهم","ه‍‍جده","هجدهم"],
      ["نونزده","نانزده","نوزده","نونزدهم","نانزدهم","نوزدهم"]
    ],
    #2_digit numbers >>> 10 to 90:
    [
      ["ده","دهم"],
      ["بیست","بیستم"],
      ["سی","سیم"],
      ["چهل","چهلم"],
      ["پنجاه","پنجاهم"],
      ["شست","شستم"],
      ["پنجاه","پنجاهم"],
      ["شست","شستم"],
      ["هفتاد","هفتادم"],
      ["هشتاد","هشتادم"],
      ["نود","نودم"]
    ],
    #3_digit numbers:
    [
      ["صد","صدم","یکصد","یک صد","یک صدم","یکصدم"],
      ["دویست","دویستم"],
      ["سیصد","سیصدم"],
      ["چهارصد","چارصد","چهارصدم","چارصدم"],
      ["پانصد","پونصد","پانصدم","پونصدم"],
      ["ششصد","شیشصد","ششصدم","شیشصدم"],
      ["هفتصد","هفتصدم","هفصد","هفصدم"],
      ["هشصد","هشتصد","هشصدم","هشتصدم"],
      ["نهصد","نهصدم"]
    ]
  ])
  #the processing part
  if type(persian_number_string)==int:
    return persian_number_string
  else:
    persian_number_string=persian_number_string.split()
    while "و" in persian_number_string:
      persian_number_string.remove("و")
    for i in range(len(persian_number_string)):
      sample=persian_number_string[i]
      while "ُ" in persian_number_string[i]:
        sample.remove("ُ")
      persian_number_string[i]=sample
  full_number=0
  for num in persian_number_string:
    con=False
    #check if its zero
    for i in l_persian_number_strings[0][0]:
      if num==i:
        con=True
        full_number+=0
    #check if its a number from 1 to 9
    for digit in l_persian_number_strings[1]:
      if num in digit:
        full_number+=(l_persian_number_strings[1].index(digit)+1)
    #check if its a number from 11 to 19
    for digit in l_persian_number_strings[2]:
      if num in digit:
        full_number+=(l_persian_number_strings[2].index(digit)+1)+10
    #check the greater ranges
    for dimension in range(3,len(l_persian_number_strings)):
      for digit in l_persian_number_strings[dimension]:
        if num in digit:
          full_number+=(l_persian_number_strings[dimension].index(digit)+1)*10**(dimension-2)
  if full_number==0 and con==False:
    return False
  else:
    return full_number
txt_input=input("persian_num:")
print(numeric_input(txt_input))
