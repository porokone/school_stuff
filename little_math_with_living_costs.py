# This program asks user about monthly income, how much school lunch costs, how many times user eats in campus and how much for the rest of living costs
# after that, it prints yearly income, school lunch costs, monthly living costs and how much user has money left and how much money is saved in four years
# if costs is cut down 20%
monthly_income = float(input("How much is your monthly income? "))
school_lunch_costs = float(input("How much school lunch costs? "))
school_lunch_times = float(input("How many times do you eat at camput in one month? "))
living_costs = float(input("How much rest of living costs is in one month? "))
print("Your yearly income is", monthly_income*12, "€")
print("Monthly school lunch costs is", school_lunch_costs * school_lunch_times, "€")
print("Monthly living costs (including school lunches) is", school_lunch_costs * school_lunch_times + living_costs, "€")
print("You have left", monthly_income - school_lunch_costs * school_lunch_times - living_costs, "€")
print("If you cut down your living costs 20% (not including school lunches) down, you save", living_costs * 0.2 * 12 * 4, "€")
print("Done, have a nice day at HAMK")