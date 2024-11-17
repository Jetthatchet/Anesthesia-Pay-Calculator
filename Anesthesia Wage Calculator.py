#Call Rates $$$
CALL_Rate= 40
PREM_Rate= 185
CALL_Hours= 14                      #Base: 14 hours for a shift of call
#Pay Rates Per Shift $$$
REG_Shift= 1700
FLOAT_Shift= REG_Shift #FLOAT IS CURRENTLY CONJOINED WITH REGULAR SHIFT
CALL_Shift= REG_Shift+(CALL_Hours*CALL_Rate)
WKND_Shift= 1520
NIGHT_Shift= 560
PC_Shift= 0 #POST-CALL IS NOT INCLUDED IN CALCULATIONS (YET)

#----------Nerd Code: By Jett McDonald----------#

def main(): #Compile Variables
 try:
  Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours= get_Worked() #Recieves input
  Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay= calc_Pay(Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours)#Calculates pay for each shift type
  Total_Pay= calc_TotalPay(Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay)#Calculates total compensation
  Total_Shifts= calc_TotalShift(Reg_Days, Call_Days, Weekend_Days, Nights_Worked)
  print_PaywwHours(Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay, Total_Pay, Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours, Total_Shifts) #Prints total pay and hours worked in a receipt format
  #run_another = 
  check_Repeat()
  #if run_another == 'y':
  # main()
 except:
  print('Restarting Program...')
  print('')
  main()
def get_Worked(): #Inputs for Time
 try:
  print('')
  Reg_Days= float(input('Regular and Float Shifts Worked: ')) 
  if Reg_Days < 0:#Handles negatives
    bad_Input()
  else:
   Call_Days = float(input('Week-Day Call Shifts Worked: '))
   if Call_Days < 0:
      bad_Input()
   else:
     Weekend_Days= float(input('Weekend Shifts Worked: '))
     if Weekend_Days < 0:
       bad_Input()
     else:
       Nights_Worked= float(input('Night Shifts Worked: '))
       if Nights_Worked < 0:
        bad_Input()
       else: PREM_Hours=float(input('In Decimal Format, Enter Hours Of Premium Service Provided: '))
       if PREM_Hours < 0:
        bad_Input()
       else:
        return Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours
 except:
  print('')
  print('ERROR: Please enter a valid, positive number. Include decimals if applicable.')#Handles invalid entries
def calc_Pay(Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours):#Calculates pay for premium time and all other shifts
 Reg_Pay = Reg_Days*REG_Shift
 Call_Pay = Call_Days*CALL_Shift
 Weekend_Pay = Weekend_Days*WKND_Shift
 Nights_Pay = Nights_Worked*NIGHT_Shift
 PREM_Pay = PREM_Hours*PREM_Rate
 return Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay
def calc_TotalPay(Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay): #Calculates total pay across all shifts
 Total_Pay = Reg_Pay+ Call_Pay+ Weekend_Pay+ Nights_Pay+ PREM_Pay
 return Total_Pay
def calc_TotalShift(Reg_Days, Call_Days, Weekend_Days, Nights_Worked):#Calculates total shifts worked
 Total_Shifts= Reg_Days+Call_Days+Weekend_Days+Nights_Worked
 return Total_Shifts
def print_PaywwHours(Reg_Pay, Call_Pay, Weekend_Pay, Nights_Pay, PREM_Pay, Total_Pay, Reg_Days, Call_Days, Weekend_Days, Nights_Worked, PREM_Hours, Total_Shifts):#Prints totals
 print(f'>---------------------------------------<')
 print(f'| Regular Shifts: {Reg_Days} | ${Reg_Pay}\t|')
 print(f'| Call shifts: {Call_Days} \t| ${Call_Pay}\t|')
 print(f'| Weekend shifts: {Weekend_Days} | ${Weekend_Pay}\t|')
 print(f'| Night shifts: {Nights_Worked} \t| ${Nights_Pay}\t|')
 print(f'| Premium Hours: {PREM_Hours} \t| ${PREM_Pay}\t|')
 print(f'|---------------------------------------|')
 print(f'| TOTAL: {Total_Shifts} Shifts \t| ${Total_Pay}\t| ')
 print(f'>---------------------------------------<')
def bad_Input():#Message for negative/error entries
 print('Input Error: positive numbers only.')
 main()
def check_Repeat():#Checks if user want to run another calculation
 while True:
  run_another = input("Do you want to perform another calculation? |Y / N|: ").strip().lower()
  if run_another == 'y':
   main()
  elif run_another == 'n':
   print('GoodBye!')
   break
  else:
   print('Invalid input. Must enter "Y" or "N" ...')

main()
