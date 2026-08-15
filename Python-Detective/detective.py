print('================================')
print("Python Detective")
print('================================')
case_id = input("Enter the case ID:")
case_name = input("Enter the case name:")
crime = input("Enter the crime:")
print("\nCase Registered")
print("Case ID:", case_id)
print("Case Name:", case_name)
print("Crime:", crime)
# List of suspects in this case
suspects = [
      {
            "name" : "Rahul",
            "age" : 27,
            "occupation" : "shopkeeper"
      },
      {
            "name" : "Priya",
            "age" : 37,
            "occupation" : "teacher"
      },
      {
            "name" : "Rhea",
            "age" : 23,
            "occupation" : "dancer"
      },
      {
            "name" : "Rohit",
            "age" : 32,
            "occupation" : "Designer"
      }
] 
def view_suspects():
    print("\n ---- Suspects ----")
    for suspect in suspects:
     print("Name:",suspect["name"])
     print("Age:",suspect["age"])
     print("Occupation:",suspect["occupation"])

# List of evidence collected in this case
evidence = [
        {
            "type" : "Fingerprint",
            "suspect" : "Rhea",
            "points" : 40
        },
        {
            "type" : "Fingerprint",
            "suspect" : "Rohit",
            "points" : 80
        },
        {
            "type" : "CCTV Footage",
            "suspect" : "Rohit",
            "points" : 50
        },
        {
            "type" : "Phone Location",
            "suspect" : "Rohit",
            "points" : 30
        },
        {
            "type" : "Phone Location",
            "suspect" : "Priya",
            "points" : 20
        },
        {
            "type" : "witness statement",
            "suspect" : "Rohit",
            "points" : 60
        }

    ] 
def view_evidence():
    print("\n ---- EVIDENCE ----")
    for item in evidence:
        print("Type:",item["type"])
        print("Suspect:",item["suspect"])
        print("Points:",item["points"])

# Calculate suspicion scores and find the most likely suspect
def analyze_case():
    scores = {}

    for suspect in suspects:
            scores[suspect["name"]] = 0

    for item in evidence:
                suspect_name = item["suspect"]
                points = item["points"]
            
                scores[suspect_name] += points

    print("\n --- INVESTIGATION SCORES ---")

    for suspect , score in scores.items():
        print(suspect,":",score, "points")

    most_likely_suspect = max(scores,key = scores.get)
    print("\n --- MOST LIKELY SUSPECT ---")
    print("Most_Likely_Suspect: ",most_likely_suspect)
    return scores, most_likely_suspect

# Generate and save the final investigation report
def generate_report():
    scores, most_likely_suspect = analyze_case()
    print("\n --- INVESTIGATION REPORT ---")
    print("Case ID: ",case_id)
    print("Case: ",case_name)
    print("Crime: ",crime)

    print("\nSuspect Scores:")
    for suspect, score in scores.items():
            print(suspect, "->", score, "points")

    print("\n Highest Evidence Score:")
    print(most_likely_suspect,"->", scores[most_likely_suspect], "points")

    if scores[most_likely_suspect] > 100:
       status = "High Suspicion"
    elif scores[most_likely_suspect] > 50:
       status = "Moderate Suspicion"
    else:
       status = "Low Suspicion"
    print("\n Status:",status)   



    with open("investigation_report.txt","w")as file:
     file.write("Investigation Report\n")
     file.write("Case ID:"+ case_id + "\n")
     file.write("Case:" + case_name + "\n")
     file.write("Crime:" + crime + "\n")
     file.write("\nSuspect Scores:\n")

     for suspect, score in scores.items():
          file.write(suspect + " ->" + str(score) + "points\n")

     file.write("\n Highest Evidence Score:\n")
     file.write(most_likely_suspect + " ->" + str(scores[most_likely_suspect]) + "points\n")
     file.write("\n Status: " + status + "\n")
     file.write("\n Investigation Report Saved Successfully\n")     

# Add a new suspect to the case
def add_suspect():
     name = input("Enter suspect name: ")
     for suspect in suspects:
        if suspect["name"].lower() == name.lower():
           print("Suspect already exists")
           return
     try:
        age = int(input("Enter suspect age: "))
     except ValueError:
        print("Invalid age! Please enter a number.")
        age = 0
     occupation = input("Enter suspect occupation: ")

     new_suspect = {

        "name": name,
        "age": age,
        "occupation": occupation    
        }
     suspects.append(new_suspect)
     print("\n Suspect added successfully")

# Add new evidence to the investigation
def add_evidence():

    evidence_type = input("Enter evidence type: ")
    suspect_name = input("Enter suspect name: ") 
    valid_names = []
    for suspect in suspects:
        valid_names.append(suspect["name"])
    if suspect_name not in valid_names:
        print("Invalid suspect name! Please add the suspect first.")
        return  
    try:
        points = int(input("Enter evidence points: "))
        if points < 0:
           print("Evidence points cannot be negative")
           return
    except ValueError:
        print("Invalid points! Please enter a number.")
        return
    new_evidence = {
        "type": evidence_type,
        "suspect": suspect_name,
        "points": points
    }

    evidence.append(new_evidence)

    print("\nEvidence added successfully!")    

# Main menu to the python detective application   
while True:
   print("\n--------------------------------")
   print("       PYTHON DETECTIVE ")
   print("----------------------------------")

   print("1. View Suspects")
   print("2. Add Suspect")
   print("3. View Evidence")
   print("4. Add Evidence")
   print("5. Analyze Case")
   print("6. Generate Report")
   print("7. Exit")

   choice = input("\nEnter your choice: ")

   if choice == "1":
    view_suspects()

   elif choice == "2":
    add_suspect()

   elif choice == "3":
    view_evidence()

   elif choice == "4":
    add_evidence()

   elif choice == "5":
    scores, most_likely = analyze_case()

   elif choice == "6":
    generate_report()

   elif choice == "7":
    print("Exiting Python Detective...")
    break
   else:
    print("Invalid choice!")