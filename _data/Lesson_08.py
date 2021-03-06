
import re, os


source = "C:/Users/Tatjana Smiljnic/Desktop/univie-tnt-2019.github.io/Lesson07/wget-activehistory/" # Source presents path_where_initial_xml_files_are.

target = "C:/Users/Tatjana Smiljnic/Desktop/univie-tnt-2019.github.io/Lesson_08/wget-activehistory_modified/" # Target is path_to_save_new_files.


lof = os.listdir(source)
counter = 0 # general counter to keep track of the progress

for f in lof:
    if f.startswith("dltext"): # fileName test        
        with open(source + f, "r", encoding="utf8") as f1:
            text = f1.read()

            # try to find the date
            date = re.search(r'<date value="([\d-]+)"', text).group(1)

            # splitting the issue into articles/items (with regular expression we want to unify links so that we can use it)
            split = re.split("<div3 ", text)

            c = 0 # item counter
            for s in split[1:]: # in order to split 
                c += 1
                s = "<div3 " + s # a step to restore the integrity of items
                #input(s)

                # try to find a unitType
                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"
                    print(s)

                # try to find a header                  
                try:
                    header = re.search(r'<head>(.*)</head>', s).group(1)
                    header = re.sub("<[^<]+>", "", header)
                except:
                    header = "NO HEADER"
                    print("\nNo header found!\n")

                text = re.sub("<[^<]+>", "", s)
                text = re.sub(" +\n|\n +", "\n", text)
                text = re.sub("\n+", ";;; ", text)

                # generating necessary bits 
                fName = date+"_"+unitType+"_"+str(c)

                itemID = "#ID: " + date+"_"+unitType+"_"+str(c)
                dateVar   = "#DATE: " + date
                unitType = "#TYPE: " + unitType
                header = "#HEADER: " + header
                text = "#TEXT: " + text

                # creating a text variable
                var = "\n".join([itemID,dateVar,unitType,header,text])
                #input(var)

                # saving
                with open(target+fName+".txt", "w", encoding="utf8") as f9: #
                    f9.write(var)

        # count processed issues and print progress counter at every 100        
        counter += 1
        if counter % 100 == 0:
            print(counter)

