test_mark = int(input("Please enter your test mark: "))

if test_mark >= 75 and test_mark <= 100:
    print("You got a distinction!")
elif test_mark < 75 and test_mark >= 50:
    print("You have passed!")
elif test_mark <= 49 and test_mark >= 0:
    print("You have failed")
else:
    print("Invalid entry")