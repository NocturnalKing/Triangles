#herons formula only for now
import math

def herons_formula():
  #herons formula
  #used to solve an area
  a = float(input("Input a side: "))
  b = float(input("Input another side: "))
  c = float(input("Input the last side: "))
  s = (a+b+c)/2
  answer = math.sqrt(s*(s-a)*(s-b)*(s-c))
  return answer

def sines_law_side():
  #law of sines
  #but to solve for a side
	a = float(input("Input side 'a': "))
	A = float(input("Input angle 'A' (in degrees): "))
	B = float(input("Input angle 'B' (in degrees): "))
	answer = a*math.sin(B)/math.sin(A)
	return answer

def sines_law_angle():
  #law of sines
  #solving for an angle
	a = float(input("Input side 'a': "))
	A = float(input("Input angle 'A' (in degrees): "))
	b = float(input("Input side 'b': "))
	answer = b*math.sin(A)/a
	return answer

def cosines_law_side():
  #law of cosine
  #solving for a side
	return "This fucntion doesn't work yet"

while True:
	print("This is the format \nLetter - What it does - What it needs")
	print("A - Area of a triangle - 3 sides")
	print("B - Law of sines (solving for a side) - 2 angles and 1 of their sides")
	print("C - Law of sines (solving for an angle) - 2 sides and 1 of their angles")

	choice = input("What is your choice (input a letter): ")
	choice = choice.title()
	while choice not in ['A', 'B', 'C']:
		print("That isn't a valid input")
		choice = input("What is your choice (input A, B, C, or Stop): ")
		choice = choice.title()

	if choice == "A":
		print("Answer: [", herons_formula(), "]")
	elif choice == "B":
		print("Answer: [", sines_law_side(), "]")
	elif choice == "C":
		print("Answer: [", sines_law_angle(), "]")
	print("")
	if input("Do you want to use another triangle? [y/n]: ").lower() == 'n':
            print("Thanks for using the program!")
            break
	else:
		print()
