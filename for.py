people = [["John", "New-York", "35", "male"], ["Alex", "Moscow", "21", "male"], ["Annika", "Tallinn", "30", "female"],
          ["Piere", "Paris", "42", "male"]]

for person in people:
    if person[3] == "male":
        print("This is " + person[0] + ". He lives in " + person[1] + ". He is " + person[2] + ", " + person[3])
    elif person[3] == "female":
        print("This is " + person[0] + ". She lives in " + person[1] + ". She is " + person[2] + ", " + person[3])