import pandas as pd
import matplotlib.pyplot as plt
import wikipediaapi as wk

# read csv file
df = pd.read_csv("sports.csv")
df = df.set_index("SPORT")

# wikipedia object
wiki = wk.Wikipedia(
    language="en",
    user_agent="CIS2300-Project (student@example.com)"
)

print("CIS2300 Sports Project")

op = ""

while op != "7":
    print("\n*** Main Menu ***")
    print("1 - Display ALL data")
    print("2 - Display SELECTED records")
    print("3 - Add NEW sport")
    print("4 - Delete a sport")
    print("5 - Save to file")
    print("6 - Wikipedia info")
    print("7 - Exit")

    op = input("Please choose (1-7): ")

    # 1 show all data
    if op == "1":
        print("\n--- All Sports Data ---")
        print(df)
        g = input("Show graph? y/n: ")
        if g == "y" or g == "Y":
            df.plot(kind="bar")
            plt.xlabel("SPORT")
            plt.show()

    # 2 show selected data
    elif op == "2":
        print("\nCountries you can choose:", ", ".join(df.columns))
        countries = input("Enter countries (comma): ").upper().split(",")
        countries = [c.strip() for c in countries]

        print("Sports you can choose:", ", ".join(df.index))
        sports = input("Enter sports (comma): ").upper().split(",")
        sports = [s.strip() for s in sports]

        try:
            out = df.loc[sports, countries]
            print("\n--- Selected Data ---")
            print(out)
            g = input("Show graph? y/n: ")
            if g == "y" or g == "Y":
                out.plot(kind="bar")
                plt.xlabel("SPORT")
                plt.show()
        except:
            print("Something wrong. Maybe spelling is wrong.")

    # 3 add new sport
    elif op == "3":
        sp = input("Input sport name: ").upper()
        if sp == "":
            print("Sport name cannot empty.")
        else:
            vals = []
            for c in df.columns:
                v = input(c + " score: ")
                try:
                    v = int(v)
                except:
                    print("Not a number, set to 0.")
                    v = 0
                vals.append(v)
            df.loc[sp] = vals
            print("New sport added.")

    # 4 delete sport
    elif op == "4":
        sp = input("Sport to delete: ").upper()
        if sp in df.index:
            df = df.drop(sp)
            print("Sport deleted.")
        else:
            print("Sport not exist.")

    # 5 save file
    elif op == "5":
        df.to_csv("sports.csv")
        print("File saved.")

    # 6 wikipedia info
    elif op == "6":
        kw = input("Search term: ")
        p = wiki.page(kw)
        if p.exists():
            print("\n--- Wikipedia Info ---")
            print(p.summary[:400])
        else:
            print("No info found.")

    # 7 exit program
    elif op == "7":
        print("Ok, exit now.")

    # wrong option
    else:
        print("Wrong option, try again.")

