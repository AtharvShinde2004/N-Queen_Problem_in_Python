import copy

from random import randrange

import random



class Board:

    def __init__(self, n):

        self.n = n

        self.board = [[0 for i in range(0, self.n)] for j in range(0, self.n)]

        for i in range(0, n):

            while 1:

                rand_row = random.randint(0, n - 1)

                rand_col = i

                if self.board[rand_row][rand_col] == 0:

                    self.board[rand_row][rand_col] = "Q"

                    break



def print_state(state):

    for i in range(n):

        result = ""

        for j in range(n):

            result += str(state[i][j]) + " "

        print(result)

    print("")



def calculate_heuristics(tboard, n):

    cost = 0

    for i in range(0, n):

        for j in range(0, n):

            if tboard.board[i][j] == "Q":

                for k in range(j + 1, n):

                    if tboard.board[i][k] == "Q":

                        cost += 1

                i1, j1 = i + 1, j + 1

                while i1 < n and j1 < n:

                    if tboard.board[i1][j1] == "Q":

                        cost += 1

                    i1 += 1

                    j1 += 1

                i1, j1 = i - 1, j + 1

                while i1 >= 0 and j1 < n:

                    if tboard.board[i1][j1] == "Q":

                        cost += 1

                    i1 -= 1

                    j1 += 1

    return cost



def calculate_min_board(tboard, n):

    list1 = []

    min_cost = calculate_heuristics(tboard, n)

    for i in range(0, n):

        for j in range(0, n):

            if tboard.board[j][i] == "Q":

                for i1 in range(0, n):

                    if tboard.board[i1][i] != "Q":

                        new_board = copy.deepcopy(tboard)

                        new_board.board[j][i] = 0

                        new_board.board[i1][i] = "Q"

                        cost = calculate_heuristics(new_board, n)

                        if cost < min_cost:

                            list1.clear()

                            min_cost = cost

                            list1.append([i1, i])

                        elif cost == min_cost:

                            list1.append([i1, i])



    return list1, min_cost



def hill_climbing(board, iteration_count):

    steps = 0

    val = calculate_heuristics(board, n)

    if iteration_count < 4:

        print("The search sequence for random configuration: ", iteration_count + 1)

        step_count = 0

    while 1:

        if iteration_count < 4:

            print_state(board.board)

            step_count += 1

        if val == 0:

            break

        else:

            steps += 1

            list1, cost = calculate_min_board(board, n)

            if val <= cost or len(list1) == 0:

                break

            else:

                random_index = randrange(0, len(list1))

                index = list1[random_index]

                val = cost

                for i in range(0, n):

                    board.board[i][index[1]] = 0

                board.board[index[0]][index[1]] = "Q"



    if iteration_count < 4:

        if val == 0:

            print("Success")

        else:

            print("Failure")

        print("Number of Steps: ", step_count - 1)

        print("----------------")

    if val == 0:

        return 1, steps

    return 0, steps



def hill_climbing_with_sideways(tboard, iteration_count):

    steps = 0

    side_way_count = 0

    b = tboard

    present_cost = calculate_heuristics(b, n)

    if iteration_count < 4:

        print("The search sequence for random configuration: ", iteration_count + 1)

        step_count = 0

    while steps < 100:

        if iteration_count < 4:

            print_state(b.board)

            step_count += 1

        if present_cost == 0:

            break

        else:

            steps += 1

            list1, cost = calculate_min_board(b, n)

            if present_cost < cost:

                break

            if len(list1) == 0:

                break

            else:

                if present_cost == cost:

                    side_way_count += 1

                else:

                    side_way_count = 0

                random_index = randrange(0, len(list1))

                index = list1[random_index]

                present_cost = cost

                for i in range(0, n):

                    b.board[i][index[1]] = 0

                b.board[index[0]][index[1]] = "Q"



    if iteration_count < 4:

        if present_cost == 0:

            print("Success")

        else:

            print("Failure")

        print("Number of Steps: ", step_count - 1)

        print("----------------")

    if present_cost == 0:

        return 0, steps

    return 1, steps



def hill_climbing_random_restart(tboard):

    restart_count = 0

    steps = 0

    b = tboard

    hprev = calculate_heuristics(b, n)

    while 1:

        if hprev == 0:

            break

        else:

            steps += 1

            list1, h = calculate_min_board(b, n)

            if hprev <= h or len(list1) == 0:

                restart_count += 1

                b = Board(n)

                hprev = calculate_heuristics(b, n)

                continue



            random_index = randrange(0, len(list1))

            index = list1[random_index]

            hprev = h

            for i in range(0, n):

                b.board[i][index[1]] = 0

            b.board[index[0]][index[1]] = "Q"



    if hprev == 0:

        return 0, steps, restart_count

    return 1, steps, restart_count



def random_restart_hill_climbing_with_sideways(tboard):

    steps = 0

    side_way_count = 0

    restart_count = 0

    b = tboard

    hprev = calculate_heuristics(b, n)

    while 1:

        if hprev == 0:

            break

        else:

            steps += 1

            list1, h = calculate_min_board(b, n)

            if hprev < h or len(list1) == 0:

                b = Board(n)

                hprev = calculate_heuristics(b, n)

                restart_count += 1

                side_way_count = 0

                continue



            if hprev == h:

                side_way_count += 1

                if steps >= 100:

                    b = Board(n)

                    hprev = calculate_heuristics(b, n)

                    restart_count += 1

                    side_way_count = 0

            else:

                side_way_count = 0



            random_index = randrange(0, len(list1))

            index = list1[random_index]

            hprev = h

            for i in range(0, n):

                b.board[i][index[1]] = 0

            b.board[index[0]][index[1]] = "Q"



    if hprev == 0:

        return 0, steps, restart_count

    return 1, steps, restart_count



def main():

    global n



    success_steps = 0

    failure_steps = 0

    success_count = 0

    failure_count = 0

    try:

        n = int(input("Enter the value of n: "))

        print("*** Steepest-ascent Hill Climbing ***")

        print("Executing...")

        for i in range(0, 500):

            b = Board(n)

            val, steps = hill_climbing(b, i)

            if val == 0:

                failure_count += 1

                failure_steps += steps

            else:

                success_count += 1

                success_steps += steps



        success_rate = (success_count / (success_count + failure_count)) * 100

        failure_rate = (failure_count / (success_count + failure_count)) * 100

        print(

            "Success rate is: ",

            round(success_rate, 2),

            "% and Failure rate is: ",

            round(failure_rate, 2),

            "%",

        )

        if success_count != 0:

            print(

                "The average number of steps when the algorithm succeeds: ",

                round(success_steps / success_count, 2),

            )

        if failure_count != 0:

            print(

                "The average number of steps when the algorithm fails: ",

                round(failure_steps / failure_count, 2),

            )



        print("*** Hill-climbing search with sideways move ***")

        print("Executing...")

        success_steps = 0

        failure_steps = 0

        success_count = 0

        failure_count = 0

        for i in range(0, 500):

            b = Board(n)

            val, steps = hill_climbing_with_sideways(b, i)

            if val == 1:

                failure_count += 1

                failure_steps += steps

            else:

                success_count += 1

                success_steps += steps

        success_rate = (success_count / (success_count + failure_count)) * 100

        failure_rate = (failure_count / (success_count + failure_count)) * 100

        print(

            "Success rate is: ",

            round(success_rate, 2),

            "% and Failure rate is: ",

            round(failure_rate, 2),

            "%",

        )

        if success_count != 0:

            print(

                "The average number of steps when the algorithm succeeds: ",

                round(success_steps / success_count, 2),

            )

        if failure_count != 0:

            print(

                "The average number of steps when the algorithm fails: ",

                round(failure_steps / failure_count, 2),

            )



        print("*** Random-restart hill-climbing search without sideways move ***")

        print("Executing...")

        success_steps = 0

        failure_steps = 0

        success_count = 0

        failure_count = 0

        total_restart_count = 0

        for i in range(0, 100):

            b = Board(n)

            val, steps, restart_count = hill_climbing_random_restart(b)

            if val == 1:

                failure_count += 1

                failure_steps += steps

            else:

                success_count += 1

                success_steps += steps

            total_restart_count += restart_count

        print(

            "The average number of random restarts required without sideways move:",

            total_restart_count / (success_count + failure_count),

        )

        print(

            "The average number of steps required without sideways move:",

            success_steps / (success_count + failure_count),

        )



        print("*** Random-restart hill-climbing search with sideways move ***")

        print("Executing...")

        success_steps = 0

        failure_steps = 0

        success_count = 0

        failure_count = 0

        total_restart_count = 0

        for i in range(0, 100):

            b = Board(n)

            val, steps, restart_count = random_restart_hill_climbing_with_sideways(b)

            if val == 1:

                failure_count += 1

                failure_steps += steps

            else:

                success_count += 1

                success_steps += steps

            total_restart_count += restart_count

        print(

            "The average number of random restarts required with sideways move:",

            total_restart_count / (success_count + failure_count),

        )

        print(

            "The average number of steps required with sideways move:",

            success_steps / (success_count + failure_count),

        )



    except ValueError:

        print("Please enter a number as the value of n.")



main()

