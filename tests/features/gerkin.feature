Feature: Using a retirement age calculator to figure out
  what year and month your age should be when you can retire.

Scenario: The user was born before 1900
  Given the user inputs their birth year of "1899" and birth month of "01"
  When the birth year is before 1938
  Then the retirement age will be "65" years old

Scenario: The user was born in 1940
  Given the user inputs their birth year of "1940" and their birth month of "03"
  When the birth year is between 1937 and 1943 and the month is calculated
  Then the retirement age will be "65" years and "6" months old

Scenario: The user was born in 1950
  Given the user inputs their birth year of "1950" and their birth month of "06"
  When the birth year is between 1942 and 1955 and the month is calculated
  Then the retirement age will be "66" years old

Scenario: The user was born in 1958
  Given the user inputs their birth year of "1958" and their birth month of "09"
  When the birth year is between 1955 and 1960 and the month is calculated
  Then the retirement age will be "66" years and "8" months old

Scenario: The user was born in 2021
  Given the user inputs their birth year of "2021" and their birth month of "12"
  When the birth year is after 1960 and the month is calculated
  Then the retirement age will be "67" years old