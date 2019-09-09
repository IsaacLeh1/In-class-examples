#Isaac Lehman
#9/19
#Cash Register

#Amount of items
numItems=8
#Item cost
costPerItem=11.3
#Total before tax
subTotal= numItems*costPerItem
#Tax rate
taxRate=0.07
#Tax amount
taxAmount= taxRate*subTotal
#Total price
totalPrice=taxAmount+subTotal
print()

print("        SALES RECEIPT")
print("Number of items  "," : ",str(numItems))
print("Cost per item        "," : ","$",str(costPerItem))
print("Tax rate                "," : ",str(taxRate))
print("Tax Amount          "," : ",str(taxAmount))
print("TOTAL SALE PRICE"," : ",str(totalPrice))
