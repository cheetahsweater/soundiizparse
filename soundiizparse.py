from pathlib import Path
import csv

#Results CSV outputted by Soundiiz
results = Path(__file__).parent / "results.csv"
#New file for parser
resultsout = Path(__file__).parent / "results.txt"
#Defining lists
nolist = []
yeslist = []
noartist = []
yesartist = []

with open(results, "r", encoding="utf8") as file:
    reader = csv.reader(file)

    for x in reader:
        #Adds song and artist names to "no" lists if song not found (denoted by "0" in the fifth column of the CSV)
        if x[4] == "0":     
            nolist.append(x[0])
            noartist.append(x[1])
        #Adds song and artist names to "yes" lists if song found (denoted by "1" in the fifth column of the CSV)
        if x[4] == "1":
            yeslist.append(x[0])
            yesartist.append(x[1])
    with open(resultsout, mode="w", encoding="utf-8") as output_file:
        #Adds section for songs successfully found and creates a list with each line having one song
        text = "SONGS FOUND:\n"
        for yes, artist in zip(yeslist, yesartist):
            if artist != "":        #Adds artist name if applicable, otherwise skips it
                text += artist + " - " + yes + "\n"
            else:
                text += yes + "\n"
        #Adds section for songs not found and creates a list with each line having one song
        text += "\nSONGS NOT FOUND:\n"
        for no, artist in zip(nolist, noartist):
            if artist != "":
                text += artist + " - " + no + "\n"
            else:
                text += no + "\n"
        #Outputs reorganized text into new file
        output_file.write(text)
        print("Done! :)")