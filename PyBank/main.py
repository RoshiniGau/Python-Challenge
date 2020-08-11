import os
import csv
from pathlib import Path

csvpath = os.path.join("Resources","PyBankbudget.csv")
month_list=[]
profit_loss_list=[]
average_monthly_change_list=[]
previous_month_amount=0
with open(csvpath, 'r') as budget:
     
    csvreader = csv.reader(budget, delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        month_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))
    total_months=len(month_list)
    net_profit_loss=0

    for x in profit_loss_list:
       net_profit_loss=net_profit_loss+x


    for x in range(len(profit_loss_list)):
        if x == 0 :
            previous_month_amount=profit_loss_list[x]

        else :
            monthly_change=profit_loss_list[x]-previous_month_amount
            average_monthly_change_list.append(monthly_change)
            previous_month_amount=profit_loss_list[x]
    length=len(average_monthly_change_list)
    total=sum(average_monthly_change_list)
    profit_loss_average=total/length
    #print(profit_loss_average)

month_greatest_increase=''
amount_greatest_increase=0
month_greatest_decrease=''
amount_greatest_decrease=0
for x in range(len(average_monthly_change_list)):
    if average_monthly_change_list[x] > amount_greatest_increase:
        amount_greatest_increase=average_monthly_change_list[x]
        month_greatest_increase=month_list[x+1]
    elif average_monthly_change_list[x]<amount_greatest_decrease :
        amount_greatest_decrease=average_monthly_change_list[x]
        month_greatest_decrease=month_list[x+1]
print("Financial Analysis")
print("-------------------------------------------------------------------")
print("Total Months :" +str(total_months))
print("Total:"  +str(net_profit_loss))
print("The greatest increase in profits over the entire period was in " +month_greatest_increase  +" "+ "for $"  +str(amount_greatest_increase))
print("The greatest decrease in profits over the entire period was in " +month_greatest_decrease  +" "+ "for $"  +str(amount_greatest_decrease))

file=open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("-----------------------------------------------------------------" +"\n")
file.write("Total Months :" +str(total_months) +"\n")
file.write("Total:"  +str(net_profit_loss) +"\n")
file.write("The greatest increase in profits over the entire period was in " +month_greatest_increase  +" "+ "for $"  +str(amount_greatest_increase) +"\n")
file.write("The greatest decrease in profits over the entire period was in " +month_greatest_decrease  +" "+ "for $"  +str(amount_greatest_decrease) +"\n")
file.close()
