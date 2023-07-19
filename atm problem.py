def calculate_total_amount(denominations, notes):
    total_amount = 0
    for i in range(len(denominations)):
        total_amount += denominations[i] * notes[i]
    return total_amount

denominations = [2000, 500, 200, 100]
notes = []
for denomination in denominations:
    note = int(input("Enter the number of {denomination} notes: "))
    notes.append(note)

total_amount = calculate_total_amount(denominations, notes)
print("Total amount available in the ATM machine:", total_amount)
