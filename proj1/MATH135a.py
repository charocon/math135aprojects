
def problem_1_horner():
    print("\nWith the given polynomial") 
    print("p(x) = x^6 + 8x^5 - 3x^3 - 4x^2 + 10 about -3\n")

    poly_matr = [1, 8, 0, -3, -4, 0, 10]

    center = -3
    curr_coef = []
    final_taylor = []

    for i in range(len(poly_matr) - 1):
        # First if it is the first iteration, the first term waterfalls down, becomes the first coefficient,
        # Then multiply that first coefficient by the center, then product + coefficient from polynomial

        bottom_ans = poly_matr[0]

        for j in range(len(poly_matr)):
            if j == 0:
                curr_coef.append(bottom_ans)
                continue
            else:
                bottom_ans = ( center * bottom_ans ) + poly_matr[j]
                curr_coef.append(bottom_ans)
        
        final_taylor.append(bottom_ans)
        curr_coef.pop()

        # Start over the synthethic division and pop the last element that is the coefficient
        poly_matr.clear()
        poly_matr = curr_coef.copy()
        curr_coef.clear()

    final_taylor.append(poly_matr[0])

    # Write out the taylor series
    for i in range(len(final_taylor)):
        if i == 0:
            print("f(x) = " + str(final_taylor[0]), end=' ')
        else:
            print(" + " + str(final_taylor[i]) + "(x + " + str(center * -1) + ")^" + str(i), end=' ')

    print("\n")

def problem_2_octal():
    print("\nGiven a decimal number")
    print("(42871.02044249548245602455)_10\n")

    prob_int = 42871
    prob_dec = 0.02044249548245602455

    # For the integer part do division
    octal_rem = []

    while(prob_int != 0):
        octal_rem.append(prob_int%8)
        prob_int = int(prob_int/8)

    octal_rem.reverse()

    # For the decimal part do multiplication
    octal_prod = []

    split_rep = divmod(prob_dec*8, 1)
    while(split_rep[1] != 0):
        # Using the divmod built in python function that I recently learned how to use off of the python documentation
        octal_prod.append(split_rep[0])
        prob_dec = split_rep[1]
        split_rep = divmod(prob_dec*8, 1)
    octal_prod.append(split_rep[0])

    # Print out the octal representation

    octal_rep = ""

    for i in range(len(octal_rem)):
        octal_rep = octal_rep + str(octal_rem[i])

    octal_rep = octal_rep + "."

    for i in range(len(octal_prod)):
        octal_rep = octal_rep + str(int(octal_prod[i]))

    print(octal_rep)

def main():
    prob_input = input("Which problem would you like to do\n")

    while(True):
        if prob_input.isdigit() and (int(prob_input) == 1 or int(prob_input) == 2):
            break
        else:
            prob_input = input("\nNot a valid input, please try again: ")

    if int(prob_input) == 1:
        problem_1_horner()
    else:
        problem_2_octal()


if __name__ == "__main__":
    main()