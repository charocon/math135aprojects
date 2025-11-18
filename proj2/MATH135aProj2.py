
def problem_1_spp():

    problem_matrix = [[0.4096, 0.1234, 0.3678, 0.2943, 0.4043],
                      [0.2246, 0.3872, 0.4015, 0.1129, 0.1550],
                      [0.3645, 0.1920, 0.3781, 0.0643, 0.4240],
                      [0.1784, 0.4002, 0.2786, 0.3927, 0.2557]]

    scale_vector = [0,0,0,0]
    index_vector = [1,2,3,4]
    scaled_pivots = [0,0,0,0]
    n = 4
    pivot_row = 0

    # For the first iteration going to the next, find the scaled vector
    for i in range(n - 1):
        # Finding the pivot row 
        scaled_pivots = [ problem_matrix[0][i]/scale_vector[0] ,
                          problem_matrix[1][i]/scale_vector[1] ,
                          problem_matrix[2][i]/scale_vector[2] ,
                          problem_matrix[3][i]/scale_vector[3] ]
        # Finding the pivot row
        max_value = max(scaled_pivots)
        pivot_row = scaled_pivots.index(max_value)
        # Swap the index vector with the current iteration
        i, pivot_row = pivot_row, i
        # solve for zeroing out the columns


            



def problem_2_tri():
    print("bruh")

def main():
    prob_input = input("Which problem would you like to do\n")

    while(True):
        if prob_input.isdigit() and (int(prob_input) == 1 or int(prob_input) == 2):
            break
        else:
            prob_input = input("\nNot a valid input, please try again: ")

    if int(prob_input) == 1:
        problem_1_spp()
    else:
        problem_2_tri()


if __name__ == "__main__":
    main()