import csv
import json

def marvin1():
settlements = {}
with open(r"settlements_copy.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = "\t")
    i = 0 # setze Counter, um nur die erste Zeile als "header" zu speichern
    for item in csv_reader: # gehe über alle items im csv_reder
        if i == 0: # wenn erstes Element in csv_reader, speichere dieses Element als "header"
            header = item # s.o.
            i += 1 # inkrement i um 1
        else: # alle Elemente, die nicht das erste sind:
            for var_id, value in zip(header, item): # gehe über die Listen "header" (var_id) und das jeweilige Element (value)
                if var_id == "settlement_id": # wenn das Element im Header "settlement_id" ist, erstelle einen neuen Eintrag im Dictionary mit dem dazugehörigen Wert der "settlement_id" als Key
                    settlements[value] = {}
                    higher_key = value # speichere die settlement-id als "higher_key" für die folgende Operation:
                else:
                    settlements[higher_key][var_id] = value # speichere den value im settlements-dictionary mit "higher_key" als key und "var_id" als subkey

    print(json.dumps(settlements,
                     sort_keys=True, indent=4, ensure_ascii=False))
marvin1()



def csv1():
    with open ("settlements_copy.csv") as file:
        reader = csv.Dictreader(file, delimiter="\t")
        settlements = {}
        for row in reader:
            settlements[row["settlement_id"]]=row
        return(settlements)
csv1()



#yml
file = "settlements.csv"
def converter_tsv_to_yml(file):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read().strip().split("\n")

        header = data[0].split("\t")
		
        allData = []

        for d in data[1:]:
            temp = d.split("\t")
			#input(temp)
            tempVar = [temp[0]+":"]

            for i in range(0, len(header)):
                item = "\t%s: %s" % (header[i], temp[i])
                tempVar.append(item)

                tempVarFinal = "\n".join(tempVar)
            #input(tempVarFinal)

            allData.append(tempVarFinal)

    ReallyFinalData = "\n\n".join(allData)
    with open(file.replace(".csv", ".yml"), "w", encoding="utf8") as f9:
        f9.write(ReallyFinalData)

converter_tsv_to_yml(file)



#xml
file = "settlements.csv"
def converter_tsv_to_xml(file):
	with open(file, "r", encoding="utf8") as f1:
		data = f1.read().strip().split("\n")

		header = data[0].split("\t")
		
		allData = []

		for d in data[1:]:
			temp = d.split("\t")
			#input(temp)
			tempVar = []

			for i in range(0, len(header)):
				item = "\t<%s\>%s<%s\>" % (header[i], temp[i], header[i])
				tempVar.append(item)

			tempVarFinal = "<settlement>\n"+"\n".join(tempVar)+"\n<settlement\>"
			#input(tempVarFinal)

			allData.append(tempVarFinal)

	ReallyFinalData = "\n\n".join(allData)
	with open(file.replace(".csv", ".xml"), "w", encoding="utf8") as f10:
		f10.write(ReallyFinalData)
converter_tsv_to_xml(file)



#json
file = "settlements.csv"
def converter_tsv_to_json(file):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read().strip().split("\n")

        header = data[0].split("\t")

        allData = []

        for d in data[1:]:
            temp = d.split("\t")
            #input(temp)
            tempVar = []

            for i in range(0, len(header)):
                item = "\"%s\": \"%s\"," % (header[i], temp[i])
                tempVar.append(item)


            tempVarFinal = "\n{\n"+"\n".join(tempVar)+"\n}" 
            allData.append(tempVarFinal)

    ReallyFinalData = "\n\n".join(allData)
    with open(file.replace(".csv", ".json"), "w", encoding="utf8") as f9:
        f9.write(ReallyFinalData)

converter_tsv_to_json(file)