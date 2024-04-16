
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1985744
 
# Date:16/04/2023

#progression for individual student.
#Part1(A)

def progression():                #define a function
    global pass_c
    global defer_c
    global Fail
    
    print('Students version')
    
    pass_c=int(input(' enter pass credit:'))
    defer_c=int(input('enter defer credit:'))
    Fail=int(input(' enter fail marks:'))

    if pass_c==120:
          print('Progress')
    elif pass_c==100:
          print('Progress(module trailer)')
    elif pass_c<=80 and Fail<=60:
          print('Do not progress-module retriever')
    elif pass_c<=40 and defer_c<=40 and Fail<=120:
          print('Exclude')

progression()                   
