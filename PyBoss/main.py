import os
import csv
import datetime

#Path to file 
fileto_load = os.path.join("Resources","employee.csv")
fileto_output = os.path.join("Analysis","employee_format.csv")

# State abbreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Placeholder for formatted contents
Emp_Id = []
Emp_FirstName = []
Emp_LastName = []
Emp_Dob = []
Emp_Ssn = []
Emp_State = []

# Read the csv and convert it into dictionaries
with open(fileto_load) as Emp_data:
    reader = csv.DictReader(Emp_data)

    # Loop through each row, and store in a new list
    for row in reader:

        #  Store EmpID into a list
        Emp_Id = Emp_Id + [row["Emp ID"]]

        #  Split Name and store in a temporary variable
        Split_Name = row["Name"].split(" ")

        #Save first and last name in separate list
        Emp_FirstName  = Emp_FirstName  + [Split_Name[0]]
        Emp_LastName= Emp_LastName + [Split_Name[1]]

        # Format Dob 
        Format_Dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        Format_Dob = Format_Dob.strftime("%m/%d/%Y")

        # Store Dob in a list
        Emp_Dob = Emp_Dob+ [Format_Dob]

        # Format Ssn
        Split_Ssn = list(row["SSN"])
        Split_Ssn[0:3] = ("*", "*", "*")
        Split_Ssn[4:6] = ("*", "*")
        Joined_Ssn = "".join(Split_Ssn)

        # Store Ssn in a list
        Emp_Ssn = Emp_Ssn + [Joined_Ssn]

        # Replace state name's to abbreviation
        State_Abbrev = us_state_abbrev[row["State"]]

        #Store abbreviated name's in list
        Emp_State = Emp_State + [State_Abbrev]

# Zip all the new lists together
Emp = zip(Emp_Id, Emp_FirstName, Emp_LastName,
            Emp_Dob, Emp_Ssn, Emp_State)

# Write all of the election data to csv
with open(fileto_output, "w", newline="") as Outfile:
    writer = csv.writer(Outfile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(Emp)