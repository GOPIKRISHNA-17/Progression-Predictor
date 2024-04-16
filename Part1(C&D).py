# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1985744
 
# Date:16/04/2023

#Part A AND Part B
#PartC and PartD
#Multiple outcomes and histogram

 
def histogram():                                       #create a function for histogram
    print("--"* 50)
    print("Histogram")
    print("progress ", progress," : ","*"* progress)
    print("Trailer  ", trailer," : ","*"* trailer)
    print("Retriever", retriever," : ","*"* retriever)
    print("Exclude  ", exclude," : ","*"* exclude)
    print("\n")
    print(outcomes, "Outcomes in total")
    print("--"* 50)




progress = 0
trailer  = 0
retriever= 0
exclude  = 0
outcomes = 0



while True:
        try:
            pass_c = int(input(" enter your credit at pass : "))
            while pass_c not in range(0, 121, 20):
                print("Out of range.  enter a valid credit.")
                pass_c = int(input(" enter your credit at pass : "))

            else:
                defer_c = int(input(" enter your credit at defer : "))
                while defer_c not in range(0, 121, 20):
                    print("Out of range.  enter a valid credit.")
                    defer_c = int(input(" enter your credit at defer : "))

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

                    elif pass_c == 100:
                        print("Progress(module trailer)")
                        trailer += 1
                        outcomes += 1

                    elif 0<= pass_c <= 80 and 0<= defer_c<=120 and 0<= Fail <= 60 :
                        print("Module retriever")
                        retriever += 1
                        outcomes += 1

                    elif Fail >= 80:
                        print("Exclude")
                        exclude += 1
                        outcomes += 1

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
                    output = input("Would you like to enter another set of data ?\nEnter 'y' for yes or 'q' to quit : ").lower()
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

