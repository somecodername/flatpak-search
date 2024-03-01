import os

a = input("Enter anything associated with the Flatpak package you want to search: ")
print("--------------------------------------------------------------------------------------")
print("                               Flatpak searcher has been started                      ")
print("--------------------------------------------------------------------------------------\n")


search_command = "flatpak search " + a

search_result = os.popen(search_command).read()

if not search_result.strip():
    if a:
        print("No results found for package:", a)
else:
    print(search_result)
