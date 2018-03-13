import pyperclip


my_string = input("Printer info string: ")

# Split on tab delimiter
formatted_string = my_string.split('\t')

y = "Printer Name" + "\t\t" + ":" + "\t" + formatted_string[0] + "\n" +\
    "Printer Model" + "\t\t" + ":" + "\t" + formatted_string[6] + "\n" +\
    "Serial Number" + "\t\t" + ":" + "\t" + formatted_string[7] + "\n" +\
    "IPv4 Address" + "\t\t" + ":" + "\t" + formatted_string[5] + "\n" +\
    "Location/Address" + "\t" + ":" + "\t" + formatted_string[1] + "\n" +\
    "Contact Name" + "\t\t" + ":" + "\t" + "contact_name" + "\n" +\
    "Contact No." + "\t\t" + ":" + "\t" + "contact_number" + "\n" +\
    "Error/Problem" + "\t\t" + ":" + "\t" + "error_info"

print("\n\n")
print(y)

#Copy formatted info to clipboard
pyperclip.copy(y)


#keep cmd window open
print("\n")
input("Press Enter to close...")


