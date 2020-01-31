weight = 0.5
input = 0.5
goal_predication = 0.8

step_amount = 0.001

for iteration in range(1101):
    predication = input * weight
    error = (predication - goal_predication) ** 2
    print("Error: " + str(error) + ".\tPredication: " + str(round(predication, 5)) + ".\tWeight: " + str(weight))

    up_predication = input * (weight + step_amount)
    up_error = (goal_predication - up_predication) ** 2

    down_predication = input * (weight - step_amount)
    down_error = (goal_predication - down_predication) ** 2

    if down_error < up_error:
        weight -= step_amount

    if down_error > up_error:
        weight += step_amount
