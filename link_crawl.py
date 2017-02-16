import requests
import time
import os
from bs4 import BeautifulSoup

print("YOU NEED BEAUTIFULSOUP TO RUN THIS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Fetches ALL hrefs on a given website. Tree like - could run forever!!!")
print("Provided as is. Have fun.")
print("")
print("")

def_web = raw_input("Enter URL: ")

start_time = time.time()

print("")
print("Initialising")
print("")

count = 0

res = requests.get(def_web)
data = res.text

soup = BeautifulSoup(data, "html.parser")

main_url_file = open("main_urls.txt", "w")
sub_url_file = open("sub_urls.txt", "w")

# Scrape links from the initial webpage
storage_init = []
storage_sub_links = []

os.system('cls')
print("###############")
print("~~LINKS CRAWL~~")
print("###############")
print("")
print("RUNNING")
print("")

for link in soup.find_all("a"):
    ext_1 = str(link.get('href'))

    print(ext_1)
    storage_init.append(ext_1)
    main_url_file.write(ext_1 + "\n")

    count += 1

    print(">> MAIN PAGE CRAWL <> " + "COUNT: " + str(count) + " <> ARRAY: " + str(len(storage_init)))
    print(">> URL : " + ext_1)
    print(str((time.time() - start_time)/60) + " min.")

# Phase 2

print("~~~~~~~~~~~~~~~~~~")
print("Going in the array")
print("~~~~~~~~~~~~~~~~~~")

main_url_file.close()

if(len(storage_init) != 0):
    for url in storage_init:
        cur_ind = storage_init.index(url)

        if(cur_ind > 0):
            print("Looking up @ index: " + str(cur_ind) + " && URL: " + str(url))
            try:
                # assing the new URL
                def_web = url

                res = requests.get(def_web)
                data = res.text

                soup = BeautifulSoup(data, "html.parser")
                while True:
                    try:
                        for link in soup.find_all("a"):
                            ext_1 = str(link.get('href'))

                            print(ext_1)
                            storage_sub_links.append(ext_1)
                            sub_url_file.write(ext_1 + "\n")

                            print("")
                            print(">> SUB CRAWL <> " + "INDEX: " + str(cur_ind) + " <> ARRAY: " + str(len(storage_sub_links)))
                            print(">> URL : " + ext_1)
                            print(str((time.time() - start_time) / 60) + " min.")
                    except KeyboardInterrupt:
                        break
            except:
                print("ERROR - General Issue")

                dec_time = raw_input("Continue? (enter = Y):")
                if (dec_time != ""):
                    break

    print("")
    print(str(len(storage_sub_links)) + "# of links found")
    q_time = raw_input("Do you want to go deeper? (Y/N): ")

    if(q_time == "Y" or q_time == "y"):
        for url in storage_sub_links:
            cur_ind = storage_sub_links.index(url)

            if (cur_ind > 0):
                print("Looking up @ index: " + str(cur_ind) + " && URL: " + str(url))
                try:
                    # assing the new URL
                    def_web = url

                    res = requests.get(def_web)
                    data = res.text

                    soup = BeautifulSoup(data, "html.parser")
                    while True:
                        try:
                            for link in soup.find_all("a"):
                                ext_1 = str(link.get('href'))

                                print(ext_1)
                                if(ext_1 not in storage_sub_links):
                                    storage_sub_links.append(ext_1)
                                    sub_url_file.write(ext_1 + "\n")

                                print("")
                                print(
                                ">> DEEP CRAWL <> " + "INDEX: " + str(cur_ind) + " <> ARRAY: " + str(len(storage_sub_links)))
                                print(">> URL : " + ext_1)
                                print(str((time.time() - start_time) / 60) + " min.")
                        except KeyboardInterrupt:
                            break
                except:
                    print("ERROR - General Issue")

                    dec_time = raw_input("Continue? (enter = Y):")
                    if(dec_time != ""):
                        break

                sub_url_file.close()
    elif(q_time == "N" or q_time == "n"):
        main_url_file.close()
        sub_url_file.close()

        print("")
        print("Operation canceled by user")
        print("DONE")


else:
    print("No links found")
