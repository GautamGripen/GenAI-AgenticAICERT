import json
BASE_DIR = r"C:\Dev\GenAI-AgenticAICERT/"

#Now we will read Formula 1 data from "F1_data.json" file

def read_drivers1(number: int):
    with open(f"{BASE_DIR}F1-DATA-JSON-main/F1_drivers.json") as racer1:

     fullnames = json.load(racer1)

     for full_name in fullnames:
            if full_name['number'] == number:
                resultname = full_name.get('full_name')

                return resultname

def read_drivers2(number: int):
    with open(f"{BASE_DIR}F1-DATA-JSON-main/F1_drivers.json") as racer2:

     nationalities = json.load(racer2)

    for nationality in nationalities:
            if nationality['number'] == number:
                resultnationality = nationality.get('nationality')

                return resultnationality

def read_drivers3(number: int):
    with open(f"{BASE_DIR}F1-DATA-JSON-main/F1_drivers.json") as racer3:

     ids = json.load(racer3)

    for id in ids:
            if id['number'] == number:
                resultid = id.get('id')

                return resultid


def read_teams1(world_championships: int):
    with open(f"{BASE_DIR}F1-Data-JSON-main/F1_teams.json") as manufacturer1:

        names = json.load(manufacturer1)

        for name in names:
            if name['world_championships'] == world_championships:
                resultteamname = name.get('name')

                return resultteamname

def read_teams2(world_championships: int):
    with open(f"{BASE_DIR}F1-Data-JSON-main/F1_teams.json") as manufacturer2:
        fullteamnames = json.load(manufacturer2)

        for full_name in fullteamnames:
            if full_name['world_championships'] == world_championships:
                resultchampionship = full_name.get('full_name')

                return resultchampionship

def read_teams3(world_championships: int):
    with open(f"{BASE_DIR}F1-Data-JSON-main/F1_teams.json") as manufacturer3:

        bases = json.load(manufacturer3)

        for base in bases:
            if base['world_championships'] == world_championships:
                resultbase = base.get('base')

                return resultbase

def read_teams4(world_championships: int):
    with open(f"{BASE_DIR}F1-Data-JSON-main/F1_teams.json") as manufacturer4:

        teamprinciples = json.load(manufacturer4)

        for team_principal in teamprinciples:
            if team_principal['world_championships'] == world_championships:
                resultteamprincipal = team_principal.get('team_principal')

                return resultteamprincipal

def read_teams5(world_championships: int):
    with open(f"{BASE_DIR}F1-Data-JSON-main/F1_teams.json") as manufacturer5:

        powerunits = json.load(manufacturer5)

        for power_unit in powerunits:
            if power_unit['world_championships'] == world_championships:
                resultpowerunit = power_unit.get('power_unit')

                return resultpowerunit

# for user input
if __name__ == '__main__':
    print("The Name of the F1 Driver is : " + read_drivers1(55))
    print("The Nationality of the F1 Driver is : " + read_drivers2(55))
    print("The ID of the F1 Driver is : " + read_drivers3(55))

    print("The Name of the F1 team is : ", read_teams1(16))
    print("The Full Name of the F1 team is : ", read_teams2(16))
    print("The F1 Team is based at : ", read_teams3(16))
    print("The Name of the F1 Team Principal is : ", read_teams4(16))
    print("The Car is Powered by : ", read_teams5(16))


