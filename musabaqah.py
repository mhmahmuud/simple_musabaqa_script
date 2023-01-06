
# function that computes the overall score
def compute_mark():    
    
    tilawa_count=0 # variable to hold tilawa mistakes
    tadbiq_count=0 # variable to hold tadbiq mistakes
    total_score=0  # variable to hold the total score
    

    category=input("Enter participant category: ") # getting participant category

    while True : # checking for valid response
        if category =="60" or category =="40" or category =="20" or category =="10" or category =="60":
            break
        else :
            print ("Your response is not a valid category ")
            category=input("Enter participant category: ")

    
    
    p_name=input("Enter participant name: ") #participant_name
    
    user_input=input("Enter .. for tilawa . for tadbiq or y if done ")

    
# while loop that keeps prompting the judge to record the mistakes
    while True:
        if user_input=="y":
            break
        elif user_input=="..":
            tilawa_count+=1
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")
            
        elif user_input==".":
            tadbiq_count+=0.5
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")
        else:
            print("enter valid response please !")
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")

            
    print ("First section done")
    print()
    
    p_dress=None
    p_saut=None


    try:
        p_dress=int(input("Enter dress mark: "))
        
    except Exception:
        print("Enter valid marks please " )
        p_dress=int(input("Enter dress mark: "))
        

    try:
        p_saut=int(input("Enter saut mark: "))

    except Exception:
        print("Enter valid marks please " )
        p_saut=int(input("Enter saut mark: "))





    total_score=80-(tilawa_count+tadbiq_count) + p_dress + p_saut


    #write to file after calculating
    if category=="60":
        
        with open ("sixty_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} is {} ".format(p_name,category, total_score) + "\n")

    elif category=="40":
        
        with open ("forty_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")

    elif category=="20":
        
        with open ("20_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")

    elif category=="10":
        
        with open ("ten_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")


    elif category=="5":
        
        with open ("five_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {} {".format(p_name,category, total_score) + "\n")


    #display result result

    print("Total tilawa count is {}".format(tilawa_count))
    print("Total tadbiq count is {}".format(tadbiq_count))
    print("Dress mark is {}".format(p_dress))
    print("Saut Mark {}".format(p_saut))
    print("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score))


# loop to restart the program after computing

response="y"

while response=="y":
    
    compute_mark()
    response=input("do you want to compute again? (y or n)")
        


