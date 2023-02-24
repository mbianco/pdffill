from SelectionFields import *

from JobDescriptionTable import *

if __name__ == "__main__":

	import argparse

	cmd = argparse.ArgumentParser()


	cmd.add_argument("--supervisor_name", "-s", help="Supervisor name")
	cmd.add_argument("--function_level", "-l", help="Function level", type=int)
	cmd.add_argument("--job", "-j", help="One of: SWE, RE, SE, HE")
	cmd.add_argument("--subcategory", "-c", help="Sub category (index)")
	cmd.add_argument("--employee_name", "-e", help="Employee name")
	cmd.add_argument("--city", help="City", default="11")
	cmd.add_argument("--employment", "-y", help="Level of employment")
	cmd.add_argument("--from_date", "-f", help="Valid from")
	cmd.add_argument("--internal", "-i", help="Internal Designation")
	cmd.add_argument("--date", "-d", help="Date of today")

	args = cmd.parse_args()

	#print("Is this the right function level:", Function_level[args.function_level-1])
	#check = input("?")
	check="y"
	if (check == "y"):
		print("%FDF-1.2")
		print("%âãÏÓ")
		print("1 0 obj")
		print("")
		print("<<")
		print("/FDF") 
		print("<<")
		print("/Fields [")

		print("<<")
		print("/T (Combo Box 5)")
		print("/V (" + args.city + ")")
		print(">>")
		print("<<")
		print("/T (22)")
		print("/V (" + Roles[args.function_level][args.job]["3"][0] + ")") #(Tasks_3)")
		print(">> ")
		print("<<")
		print("/T (23)")
		print("/V (" + Roles[args.function_level][args.job]["3"][1] + ")") #(share3)")
		print(">> ")
		print("<<")
		print("/T (45)")
		print("/V (28)")
		print(">> ")
		print("<<")
		print("/T (Combo Box 3)") # Management or not
		print("/V (No)")
		print(">> ")
		print("<<")
		print("/T (46)")
		print("/V (" + Requirement_base + " " + Requirement_fl[args.function_level] + ")")
		print(">> ")
		print("<<")
		print("/T (Combo Box 4)")
		print("/V (USYS)")
		print(">> ")
		print("<<")
		print("/T (47)")
		print("/V (" + args.date + ")")
		print(">> ")
		print("<<")
		print("/T (26)")
		print("/V (" + Roles[args.function_level][args.job]["4"][0] + ")") #(Tasks_4)")
		print(">> ")
		print("<<")
		print("/T (48)")
		print("/V ()")
		print(">> ")
		print("<<")
		print("/T (27)")
		print("/V (" + Roles[args.function_level][args.job]["4"][1] + ")") #"(share4)")
		print(">> ")
		print("<<")
		print("/T (49)")
		print("/V ()")
		print(">> ")
		print("<<")
		print("/T (30)")
		print("/V (" + Roles[args.function_level][args.job]["5"][0] + ")") #(Tasks_5)")
		print(">> ")
		print("<<")
		print("/T (Combo Box 7)")
		print("/V (" + args.internal + ")")
		print(">> ")
		print("<<")
		print("/T (31)")
		print("/V (" + Roles[args.function_level][args.job]["4"][1] + ")") #(share5)")
		print(">> ")
		print("<<")
		print("/T (10)")
		print("/V ("+ args.employment + ")")
		print(">> ")
		print("<<")
		print("/T (11)")
		print("/V (" + args.from_date + ")")
		print(">> ")
		print("<<")
		print("/T (34)")
		print("/V (" + Roles[args.function_level][args.job]["6"][0] + ")") #(Tasks_6)")
		print(">> ")
		print("<<")
		print("/T (35)")
		print("/V (" + Roles[args.function_level][args.job]["6"][1] + ")") #(share6)")
		print(">> ")
		print("<<")
		print("/T (14)")
		print("/V (" + Roles[args.function_level][args.job]["1"][0] + ")") #(Tasks_1)")
		print(">> ")
		print("<<")
		print("/T (15)")
		print("/V (" + Roles[args.function_level][args.job]["1"][1] + ")") #(share1)")
		print(">> ")
		print("<<")
		print("/T (38)")
		print("/V (" + Roles[args.function_level][args.job]["7"][0] + ")") #(Tasks_7)")
		print(">> ")
		print("<<")
		print("/T (39)")
		print("/V (" + Roles[args.function_level][args.job]["7"][1] + ")") #(share7)")
		print(">> ")
		print("<<")
		print("/T (18)")
		print("/V (" + Roles[args.function_level][args.job]["2"][0] + ")") #(Tasks_2)")
		print(">> ")
		print("<<")
		print("/T (19)")
		print("/V (" + Roles[args.function_level][args.job]["2"][1] + ")") #(share2)")
		print(">> ")
		print("<<")
		print("/T (2)")
		print("/V (" + Function_level[args.function_level] +")")
		print(">> ")
		print("<<")
		print("/T (4)")
		print("/V (" + args.internal + ")")
		print(">> ")
		print("<<")
		print("/T (6)")
		print("/V (" + Briefs[args.job][args.subcategory] + ")")
		print(">> ")
		print("<<")
		print("/T (7)")
		print("/V (CSCS)")
		print(">> ")
		print("<<")
		print("/T (8)")
		print("/V (" + args.supervisor_name +")")
		print(">> ")
		print("<<")
		print("/T (9)")
		print("/V (" + args.employee_name + ")")
		print(">>]")
		print(">>")
		print(">>")
		print("endobj")
		print("")
		print("trailer")
		print("")
		print("<<")
		print("/Root 1 0 R")
		print(">>")
		print("%%EOF")


# /Fields [
# <<
# /T (Combo Box 5)
# /V (Zurich City)
# >> 
# <<
# /T (22)
# /V (Tasks_3)
# >> 
# <<
# /T (23)
# /V (share3)
# >> 
# <<
# /T (45)
# /V (28)
# >> 
# <<
# /T (Combo Box 3)
# /V (No)
# >> 
# <<
# /T (46)
# /V (Requirements_Cell)
# >> 
# <<
# /T (Combo Box 4)
# /V (USYS)
# >> 
# <<
# /T (47)
# /V (Data_Cell)
# >> 
# <<
# /T (26)
# /V (Tasks_4)
# >> 
# <<
# /T (48)
# /V ()
# >> 
# <<
# /T (27)
# /V (share4)
# >> 
# <<
# /T (49)
# /V ()
# >> 
# <<
# /T (30)
# /V (Tasks_5)
# >> 
# <<
# /T (Combo Box 7)
# /V (Application developer)
# >> 
# <<
# /T (31)
# /V (share5)
# >> 
# <<
# /T (10)
# /V (Level_of_Employment)
# >> 
# <<
# /T (11)
# /V (Valid_From)
# >> 
# <<
# /T (34)
# /V (Tasks_6)
# >> 
# <<
# /T (35)
# /V (share6)
# >> 
# <<
# /T (14)
# /V (Tasks_1)
# >> 
# <<
# /T (15)
# /V (share1)
# >> 
# <<
# /T (38)
# /V (Tasks_7)
# >> 
# <<
# /T (39)
# /V (share7)
# >> 
# <<
# /T (18)
# /V (Tasks_2)
# >> 
# <<
# /T (19)
# /V (share2)
# >> 
# <<
# /T (2)
# /V (4021-I IT support \(1st level\) / 03)
# >> 
# <<
# /T (4)
# /V ()
# >> 
# <<
# /T (6)
# /V (Brief_Description)
# >> 
# <<
# /T (7)
# /V (Organizational_Unit)
# >> 
# <<
# /T (8)
# /V (Supervisor_Name)
# >> 
# <<
# /T (9)
# /V (Employee_Name)
# >>]