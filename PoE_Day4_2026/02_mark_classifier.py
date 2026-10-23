test_mark = input("Please enter your test mark between 0% and 100%: ")

conv_test_mark = -1
if test_mark == "":
    print("Test mark not entered")
else:
    conv_test_mark = int(test_mark)
    
 
if conv_test_mark <= 100 and conv_test_mark >= 80:
     print("Outstanding!")
elif conv_test_mark <= 79 and conv_test_mark >= 70:
    print("Highly competent!")
elif conv_test_mark <= 69 and conv_test_mark >= 50:
    print("Competent!")
elif conv_test_mark <= 49 and conv_test_mark >= 40:
    print("Not yet competent!")
elif conv_test_mark <= 39 and conv_test_mark >= 0:
    print("Not achieved!")
else:
    print("Invalid mark")