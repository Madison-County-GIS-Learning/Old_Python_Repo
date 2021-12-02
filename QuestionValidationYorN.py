def answerQuestion(question):
    while True:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        askQuestion = input(question + " Answer Y or N \n").upper()
        if askQuestion in ["Y","N","YES","NO"]:
            break
        print("Sorry, I didn't understand that.")
    
    if askQuestion == "Y" or askQuestion == "YES": 
        print("Thank you for selecting  Yes \nWe will process your request\n")
        return "Y"
    else:
        print("You have selected  No \nWe will NOT process this portion\n")
        return "N"

answerQuestion(question="Y or N")