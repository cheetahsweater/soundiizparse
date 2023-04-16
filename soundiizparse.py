from pathlib import Path
import csv

results = Path(__file__).parent / "results.csv"
resultsout = Path(__file__).parent / "results.txt"
nolist = []
yeslist = []
noartist = []
yesartist = []

with open(results, "r", encoding="utf8") as file:
    reader = csv.reader(file)

    for x in reader:
        if x[4] == "0":
            nolist.append(x[0])
            noartist.append(x[1])
        if x[4] == "1":
            yeslist.append(x[0])
            yesartist.append(x[1])
    print(nolist)
    with open(resultsout, mode="w", encoding="utf-8") as output_file:
        text = "SONGS FOUND:\n"
        for yes, artist in zip(yeslist, yesartist):
            if artist != "":
                text += artist + " - " + yes + "\n"
            else:
                text += yes + "\n"
        text += "\nSONGS NOT FOUND:\n"
        for no, artist in zip(nolist, noartist):
            if artist != "":
                text += artist + " - " + no + "\n"
            else:
                text += no + "\n"
        output_file.write(text)