from random import sample

def cardsToString(arr, p, c):
    result = ""
    for i in range(c):
        for j in range(p):
            result += f"{arr[j*c+i]:<5}"
        result+="\n"
    return result

def moveSlice(arr, start, end, new_index):
    slice_to_move = arr[start:end]
    arr = arr[:start] + arr[end:]
    arr = arr[:new_index] + slice_to_move + arr[new_index:]
    return arr

possible_cards = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc",
                  "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh",
                  "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks",
                  "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd"]
num_piles = 3
cards_per_pile = 7
order = 2
total_cards = num_piles*cards_per_pile
validColumns = [str(i+1) for i in range(num_piles)]

coords = []
cards = sample(possible_cards, total_cards)
selections = ()
last_selection = False
for i in range(num_piles):
    for j in range(cards_per_pile):
        coords.append((i+1,))

while True:
    print(cardsToString(cards, num_piles, cards_per_pile))
    selection = input(f"Which column is your card in ({validColumns})? ")
    if selection not in validColumns:
        continue
    else:
        s = int(selection)
        selections = selections + (s,)
        visit_order = [i for i in range(total_cards)]
        if s != order:
            visit_order = moveSlice(visit_order, (s-1)*cards_per_pile, (s-1)*cards_per_pile+cards_per_pile, (order-1)*cards_per_pile)
        temp = [() for i in range(total_cards)]
        tempc = ["" for i in range(total_cards)]
        index = 0
        count = 0
        while index < total_cards-1:
            temp[index] = coords[visit_order[count]] + (count%num_piles + 1,)
            tempc[index] = cards[visit_order[count]]
            index = total_cards-1 if index+cards_per_pile == total_cards-1 else (index+cards_per_pile)%(total_cards-1)
            count += 1
        temp[index] = coords[visit_order[count]] + (count%num_piles + 1,)
        tempc[index] = cards[visit_order[count]]
        selectionIndex = next((i for i, t in enumerate(temp) if t[:len(selections)] == selections), -1)
        if selectionIndex == -1:
            print("Not possible, either you've made a mistake or switched cards")
            selections = selections[:len(selections)-1]
            continue
        coords = temp.copy()
        cards = tempc.copy()
        if last_selection:
            break
        elif len(set(coords)) == len(coords):
            last_selection = True

selectionIndex = next((i for i, t in enumerate(temp) if t[:len(selections)] == selections), -1)
print(f"\nYour card is the {cards[selectionIndex]}!")