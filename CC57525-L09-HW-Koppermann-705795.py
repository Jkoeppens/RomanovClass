import re
import os

directory = "./Daily_dispach"
target = "cleanedDispach"
def read_dir(directory):
    os.listdir(directory) 
    filessorted=sorted(files)
    for filename in filessorted:
        if filename.startswith("dltext"):
            with open (f"{directory}{filename}", "r") as f1:
                raw = f1.read()
                date = re.search(r'<date value="([-\d]+)"', raw).group(1)
                print("date ",date)
                counter = 0
                err_count = 0
                for article in re.split("<div3", raw)[1:]:
                    counter += 1
            #        print("counter:\t",counter)
                    articeID = date + "-" + str(counter)
                    type = re.search(r"type=\".*\" n", article).group(0)
                    type = re.sub("type=\"", "", type)
                    type = re.sub("\" n", "", type)
                    try:
                        header = re.search(r"<head(.*)?>(.*)</head>", article).group(1)
                        header = re.sub("<[^<]+>", "", header)
                        print(f"Last header: {header}")
                    except:
                        try:
                            header = re.search(r"(.*)<head />", article).group(1)

                        except:
                            err_count  += 1
                            header = "no header"
                            print(f"Error for type {type} at section {articeID}"
                                f"\nCounter at: {counter}"
                                f"\nError no {err_count}")
                    body = re.sub("<[^<]+>", "", article)
                    body=re.sub("\n", " ", body)
                    body=re.sub("<[^<]+>", " " , body)
                    body=re.sub(" *", " ", body)
                    #body is not working at all

                    #xml because my future material is in xml
                    #still working on conversion
                    listcategories= ["header", "type", "body"]
                    listitems = [header, type, body]
                    tempVar = []
                    allData = []
                    for i in range(0, len(listcategories)):
                        item = "\t<%s\>%s<%s\>" % (listcategories[i], listitems[i], listcategories[i])
                        tempVar.append(item)
                        
                    tempVarFinal = "<article>\n"+"\n".join(tempVar)+"\n<article\>"
                    #input(tempVarFinal)
                    allData.append(tempVarFinal)

    ReallyFinalData = "\n\n".join(allData)
    with open(f1.replace("dis", "splitdis"), "w", encoding="utf8") as f10:
		    f10.write(ReallyFinalData)

           
read_dir(directory)






for file in os.listdir(dir):

    path_to_data = "dispachissue1.xml" + str(file)
    read_file(path_to_data)
        # next, process the main body of the article
        # next, collect all variables into some general variable (list of dictionary)
    # convert all collected data into the format of your choosing and save it to your computer (use a new folder, not the same folder where your initial Dispatch data is stored)

# next, final, write some code to process ALL issues of the Dispatch (in total, the initial Dispatch data includes 1,349 XML files, adding up to ±426 mb) 
#header: 
if re.search(r"<head(.*)?>(.*)</head>", article).group(1) == None :
     header= "no header" 
else:
header = re.search(r"<head(.*)?>(.*)</head>", article).group(1)
#same with type, vllt auch raw machen, dann darin nacht richtgem suchen, dann den cleanen oder wenn empt dann "no type"
''' body = just take header and take out any\n and /\s\s+/g, doppelte leerzeichen,

dispachDict[articleID] = {"articleID:": "header": , ... }
'''