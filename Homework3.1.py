#Homework3: count total amount of letters in txt file
# opening and reading txt file
f = open("Homework3.txt" , "r")

# defining function Alphacaount
def AlphaCount(f):
    # adding variable which will count the letter
    alphacount=0
    # adding loop for reading each line
    for line in f:
        # adding another loop which will read each character in a line
        for ch in line:
            # Adding condition.True outcome means that text file includes at least one alphabetical character
            if ch.isalpha()==True:
                # if the statement is true, will be applied the following formula
                alphacount=alphacount+1
    return alphacount

print(AlphaCount(f))
f.close()