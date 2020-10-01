# remove_text_from_image
You can remove text from image.

Step 1. Establish a Vision API project.
  Sign-in to Google Cloud Platform Console and create a new project.
  2. Name the project and click the CREATE button.
  3. Click Active Cloud Shell.
  4. Then a console shell will appear at the bottom.
    Run $ gcloud auth list to confirm that you are authenticated.
    And also run $ gcloud config list project to confirm the project id.

Step 2. Enable the Vision API.
  Run command line $ gcloud services enable vision.googleapis.com

Step 3. Authenticate API requests and download the keyFile.json.
  According to the Google Codelabs tutorial, we need to create a Service Account and a key for accessing the Vision API.
   
  Click the link below and follow the Setting up authentication GCP CONSOLE steps.
  https://cloud.google.com/vision/docs/libraries#client-libraries-usage-python

  This page shows how to get started with the Cloud Client Libraries for the Cloud Vision API. Read more about the client…
  cloud.google.com
  i. GO TO THE CREATE SERVICE ACCOUNT KEY PAGE
  ii. From the Service account list, select New service account.
  iii. In the Service account name field, enter a name.
  iv. Don’t select a value from the Role list. No role is required to access this service.
 
  v. Click Create. A note appears, warning that this service account has no role.
  vi. Click Create without role. A JSON file that contains your key downloads to your computer.
 
Step 4. Set GOOGLE_APPLICATION_CREDENTIALS with keyFile.json
  Rename the JSON file as keyFile.json. Then set GOOGLE_APPLICATION_CREDENTIALS with the file.
  export GOOGLE_APPLICATION_CREDENTIALS=~/Desktop/keyFile.json
  
Step 5. Install the Google Client Vision API client library.
  i.Run pip freeze | grep google-cloud-vision to check if the library is already installed.
  ii. If you’re not setting the environment, please run pip install --upgrade google-cloud-vision.

Step 6. Write Python code to query the Vision API.
  Copy and save the "vision.py" code as a Python file.

Run the Python file to test if all the environment settings are correctly set up.
/usr/local/opt/python/bin/python3.7 [path/to/your/filename.py]
or 
python3 [path/to/your/filename.py]

