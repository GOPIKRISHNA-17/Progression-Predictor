
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1985744
 
# Date:16/04/2023

#Part A AND Part B
#Partb-Validation

def progression():

    global pass_c
    global defer_c
    global Fail

    try:                                                                 #use try for error handling
        pass_c= int(input("enter your credit at pass : "))
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
                    f_cr = int(input(" enter your credit at fail : "))
            if pass_c + defer_c + Fail == 120 :
                if pass_c == 120:
                    print("Progress")

                elif pass_c == 100:
                    print("Progress(module trailer)")

                elif 0<= pass_c <= 80 and 0<= defer_c <=120 and 0<= Fail <= 60 :
                    print("Do not progress - Module retriever")

                elif Fail >= 80:
                    print("Exclude")

            else:
                print(" Total incorrect ")

    except ValueError:                                       #use except for error handling
        print("Integer required")

progression()        
        
