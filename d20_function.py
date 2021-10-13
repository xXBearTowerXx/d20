def d20():
    import random
    from time import sleep
    min = 1
    max = 20
    
    roll_again= "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dice...")
        sleep(1)
        print("done!")
        sleep(0.5)
        print("let's see what you got...")
        sleep(1)
        n=random.randint(min, max)
        print("the result is ", n)
        sleep(1)
        if n == 1:
            print("you fucked up")
        if n > 1 and n <= 5:
            print("feels bad")
        if n > 5 and n <= 10:
            print("kinda unlucky")
        if n > 10 and n <= 15:
            print("that's good")
        if n > 15 and n <= 19:
            print("nice roll!")
        if n == 20:
            print("you bent the reality to your own will")
        sleep(1)
        roll_again = input("wanna roll the dice again? ")
    if roll_again == "fuck you":
        print("No U!")
    if roll_again == "No u!" and n == 20:
        print("Impossible!")
        sleep(1)
        print("This is not how you use the uno reverse card!")
        sleep(2)
        print("By doing this you created a time paradox!")
        sleep(2)
        print("this whole timeline will cease to exi-")
        sleep(2)
        print("\n" * 100)
    if roll_again == "No u!" and n < 20:
        print("hahah you don't hold such power!")
