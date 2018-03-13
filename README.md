# printer-info-formatter

This little script I wrote saves me minutes a day! It doesn't sound much, but it all adds up. Keeping all my printer info in a spreadsheet means when I'm talking to someone about a specific printer or need to send off a request for a service/replacement etc. the info copied into Outlook or ticketing systems is messy and hard to read, for example: 

------------------------------------------------
TR MFP	17 Fake Highway, Altona East, VIC, 3844	3844	Traralgon	(03) 5174 3365	172.16.12.12	HP M527	CNM8J8JC0P
------------------------------------------------


The formatted info is returned already on the clipboard, meaning you can just paste straight away after using the script. Below is an example of the final output.

------------------------------------------------

Printer Name		:	TR MFP

Printer Model		:	HP M527

Serial Number		:	CNM8J8JC0P
IPv4 Address		:	172.16.12.12
Location/Address	:	317 Princes Highway, Traralgon East, VIC, 3844
Contact Name		:	contact_name
Contact No.		:	contact_number
Error/Problem		:	error_info
-------------------------------------------------

