print("Answer yes or no to the following questions")
medicine = ""

q1 = input("Is the patient experiencing diarrhea?")
if q1 == "yes":
    medicine += "Loperamide(Imodium) or Bismuth(Pepto-Bismol) for diarrhea, "

q2 = input("Is the patient experiencing heartburn and/or gastritis?")
if q2 == "yes":
    medicine += "Omeprazole(Prilose) for heartburn/gastritis, "

q3 = input("Is the patient experiencing nausea and/or vomiting?")
if q3 == "yes":
    medicine += "Omeprazole(Prilose) for nausea/vomiting, "

q3 = input("Is the patient hospitalized with SpO2<94% on room air or need supplemental oxygen, ventilation or ECMO?")
if q3 == "yes":
    medicine += "Remdesivir, "

if medicine == "":
    medicine += "nothing"
print("It is recommended to take " + medicine)