#Given lists for project
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Personal declarations
total_price = 0
average_price = 0
total_revenue = 0
average_daily_revenue = 0

#Sum up average prices
for price in prices:
    total_price += price

#Average price of haircuts
average_price = total_price / len(prices)
print("Average Haircut\n" + 
"Price\n" + 
str(average_price))

#List comprehension for lowered prices
new_prices = [low_price - 5 for low_price in prices]
#print(new_prices)

#calculating the revenue
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:\n" +
str(total_revenue))

#Calculating average daily revenue
average_daily_revenue = total_revenue / 7
#print(average_daily_revenue)

#Bringing in more customers...
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles) - 1) if new_prices[i] < 30]
print(cuts_under_30)