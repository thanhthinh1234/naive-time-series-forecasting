"""
Author: Thinh Mai
Date: 10/23/2019
Purpose: Predicting tomorrow's weather, naive time series forecasting
"""

#create a weather forecasting function
def naivePrediction(lyst,k):

    # set condition, if k is bigger than or equal to the number of observations then print 'Error'
    if len(lyst) <= k:
        return ('Error: k should be less than the number of observations')
    else:
        # prepare for below sum and lists
        s = 0
        all_f = []
        group_f = []
        sum_f = []
        calc_list = []
        actual = []
        final = []
        final_sum = 0
        # create a list of actual values that will be used in the calculation
        for n in range(k, len(lyst)):
            actual.append(lyst[n])
            # create a list contains all forecast values
            for x in range(1, k + 1):
                all_f.append(lyst[n - x])
        # start a loop to group these forecast values based on k value
        for i in range(s, len(all_f), k):
            s = i
            # grouping forecast values
            group_f.append(all_f[s:s + k])

        for number in group_f:
            # make a list contains sum of each group forecast values
            sum_f.append(sum(number))

        # in each group, if forecast sum is greater than or equal to k/2 return 1, if not return 0
        calc_list = [1 if sum >= k / 2 else 0 for sum in sum_f]

        # apply subtraction between forecast list and actual list
        final = [x1 - x2 for (x1, x2) in zip(calc_list, actual)]
        for num in final:
            # apply absolute function
            final_sum += abs(num)
        # set up a formula to calculate mean absolute error
        MAE = final_sum / (len(lyst) - k)
        return MAE

#applying function
def main():
    print(naivePrediction([1, 0, 1, 0, 1], 2))
    print(naivePrediction([1, 0, 1, 0, 1], 3))
    print(naivePrediction([1, 0, 1, 0, 1], 5))
    print(naivePrediction([1, 0, 1, 0, 1, 1, 1], 3))
    print(naivePrediction([1, 0, 1, 0, 1, 1, 1], 4))

main()


