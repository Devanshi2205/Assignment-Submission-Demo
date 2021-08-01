gift_persented_to = [2,1,5,3,4]
gift_received_from = []

for i in range(len(gift_persented_to)):
    gift_received_from.append(gift_persented_to.index(i+1) + 1)
    print("Person P", (i+1), "has received gift from person P", gift_persented_to.index(i+1) + 1)

print(gift_received_from)