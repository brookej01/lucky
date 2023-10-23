def count_letters_and_numbers(filename):
 letter_count = 0
 number_count = 0
# context manager
 with open("mydefaults.ini.txt") as ini_file:
   for line in ini_file:
      for char in line:
         if char.isalpha():
            letter_count += 1
         elif char.isdigit(): 
            number_count += 1

 return letter_count, number_count

ini_file = 'C:\\Users\\yukur\\Downloads\\mydefaults.ini.txt'
total_letters, total_numbers = count_letters_and_numbers(ini_file)

print(f"Total letters is: {total_letters}")
print(f"Total numbers is: {total_numbers}")
