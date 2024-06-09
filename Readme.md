# ### Google form sms integration
A one stop solution to send sms to form respondents.

## Adding Script to the google form 
![](https://i.postimg.cc/q7K0JWjc/mail-google.png)

Open Code.gs file and add paste in the code from Code.gs file in the repo and backend url and **Spreadsheet id **(ie connected/linked with the form to see responses, **if no file is linked link a spreadsheet to the form**)

## Now create a trigger as stated in the image below
![](https://i.postimg.cc/QxzRF0Bf/Screenshot-from-2024-06-09-17-10-56.png)

## Setting Up the Backend to send sms
Checkout the ` backend.py `for sample, or just create a post request reciever in language of your choice to recieve the responses as a user submits the form in realtime.

