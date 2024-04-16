# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1985744
 
# Date:16/04/2023

#Part 3
#Text File (extension)

def histogram():
    print("--"* 50)
    print("Histogram")
    print("progress ", progress," : ","*"* progress)
    print("Trailer  ", trailer," : ","*"* trailer)
    print("Retriver ", retriever," : ","*"* retriever)
    print("Exclude  ", exclude," : ","*"* exclude)
    print("\n")
    print(outcomes, "Outcomes in total")
    print("--"* 50)




progress  = 0
trailer   = 0
retriever = 0
exclude   = 0
outcomes  = 0

lista = []

while True:
    try:
        pass_c = int(input("enter your credit at pass : "))
        while pass_c not in range(0, 121, 20):
            print("Out of range. enter a valid credit.")
            pass_c = int(input(" enter your credit at pass : "))

        else:
            defer_c = int(input("enter your credit at defer : "))
            while defer_c not in range(0, 121, 20):
                print("Out of range.  enter a valid credit.")
                defer_c = int(input("P enter your credit at defer : "))

            else:
                Fail = int(input(" enter your credit at fail : "))
                while Fail not in range(0, 121, 20):
                    print("Out of range.  enter a valid credit.")
                    Fail = int(input(" enter your credit at fail : "))
            if pass_c + defer_c + Fail == 120 :

                if pass_c == 120:
                    print("Progress")
                    progress += 1
                    outcomes += 1
                    lista.append(["Progress - ", pass_c, defer_c, Fail])

                elif pass_c == 100:
                    print("Progress(module trailer)")
                    trailer += 1
                    outcomes += 1
                    lista.append(["Progress(module trailer) - ", pass_c, defer_c, Fail])

                elif 0<= pass_c <= 80 and 0<= defer_c <=120 and 0<= Fail <= 60 :
                    print("Do not progress - Module retriever")
                    retriever += 1
                    outcomes += 1
                    lista.append(["Do not progress - Module retriever - ", pass_c, defer_c, Fail])

                elif Fail >= 80:
                    print("Exclude")
                    exclude += 1
                    outcomes += 1
                    lista.append(["Exclude - ", pass_c, defer_c, Fail])
                output = input("Would you like to enter another set of data ?\nEnter 'y' for yes or 'q' to quit  : ").lower()
                if output == "q":
                    histogram()
                    break
                if output == "y":
                    print("\n")
                    continue
                else:
                    break

            else:
                print("Total incorrect")

                choice = input("Would you like to enter another set of data ?\nEnter 'y' for yes or 'q' to quit  : ").lower()
                if output == "q":
                    histogram()
                    break
                if output == "y":
                    print("\n")
                    continue
                else:
                    break

    except ValueError:
        print("Integer required")


for elements in lista:
    print(*elements)

file = open("progress.txt", "w")
for elements in lista :
   file.writelines(str(elements)+ "\n")
file.close() 

       
        



