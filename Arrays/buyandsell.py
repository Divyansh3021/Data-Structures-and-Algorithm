prices = [1,2]
profit = 0
stock = False
current_price = 0
i = 0
# for i in range(len(prices)-1):
while i <= len(prices) - 1:
    if (prices[i] > prices[i+1]) and (stock ==  False):
        i+=1
        continue
    else :
        print("Current price is: ", prices[i])
        if stock == False:
            stock = True
            current_price = prices[i]
            print("bought stock at: ", current_price)
            i += 1
        else:
            count = 0
            max_price = current_price   #current price  = 1, i = 2
            print("i = ",i)

            for count in range(len(prices)-i):
                if (max_price < prices[i+count]):
                    max_price = prices[i+count]
                    print("Current price: ",current_price," max price: ",max_price)
                
                else:
                    break
            if max_price > current_price:
                profit += max_price-current_price
                stock = False
                print("Stocks sold at current price of: ", current_price," max price: ",max_price)
                i = i+count
                print("Modified i: ",i)

print(profit)
