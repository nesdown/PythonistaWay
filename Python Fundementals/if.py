def main():
    x, y = 8, 8

    # if (x < y):
    #     print("X is less than Y")
    # elif (x == y):
    #     print("The values X and Y are qeual.")
    # else:
    #     print("X is higher than Y")

    # A if B else C
    st = "x is less than y" if (x < y) else "x is greater than y"
    print(st)

    total = 100
    country = "US"

    if country == "US":
        if total <= 50:
            print("Shipping is 50$")
        elif total <= 100:
            print("Shipping is 25$")
        elif total <= 200:
            print("Shipping 15$")
        else:
            print("Shipping is FREE") 
    
    if country == "AU":
        if total <= 50:
            print("Shipping is 100$")
        else:
            print("Shipping is FREE")

# function(argument) {
#     switch(argument) {
#         case 0:
#             return "This is case 0"
#         case 1: 
#             return "This is case 1"
#         case 2:
#             return "This is case 2"
#     }
# }

def SwitchExample(argument):
    switcher = {
        0: "This is case 0",
        1: "This is case 1",
        2: "This is case 2"
    }

    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    argument = 1
    print(SwitchExample(0))