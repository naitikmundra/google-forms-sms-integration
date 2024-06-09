//Google form sms integration by Naitik Mundra
//Code.gs 
//Open the google form as admin and find script editor. Then paste thiks code in Code.gs file.
//This file will send on our backend the responsess as form is submitted. We will take mob no. in the response in google form.


// Function to send a POST request on form submission
function onFormSubmit(e) {
  // URL to send the POST request to (use the ngrok URL if running locally)
  var url = "ADD RECIEVING URL HERE";
  var spreadsheetId = 'ADD SPREADSHEET(THE ONE WHICH IS LINKED TO FORM) ID HERE';
  
  // Open the spreadsheet by ID
  var sheet = SpreadsheetApp.openById(spreadsheetId).getActiveSheet();
  
  // Get the last row with data
  var lastRow = sheet.getLastRow();
  
  // Get the form response data from the last row
  var formResponse = sheet.getRange(lastRow, 1, 1, sheet.getLastColumn()).getValues()[0];
  
  // Create the payload (you can customize this based on your requirements)
  var payload = {
    message:formResponse,
    timestamp: new Date().toISOString()
  };

  // Set the options for the POST request
  var options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  };

  // Send the POST request
  try {
    var response = UrlFetchApp.fetch(url, options);
    Logger.log('POST request sent successfully. Response: ' + response.getContentText());
  } catch (error) {
    Logger.log('Error sending POST request: ' + error.toString());
  }
}

// Install the trigger to run on form submission
function createOnSubmitTrigger() {
  var form = FormApp.openById('your-form-id'); // Replace with your form ID
  ScriptApp.newTrigger('onFormSubmit')
           .forForm(form)
           .onFormSubmit()
           .create();
}
