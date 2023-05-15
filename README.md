# Selection Mailing Automation

Automates the selection status (rejection or selection task) during the selection procedure in KOSS.
 
### Getting the csv files

1. Go to the google sheets of the form responses.

2. Create a subsheet containing all those entries which are to be given tasks for a particular day. 

3. Make sure the `email` and `Tentative Task` fields are properly filled with link to task on github.

4. Goto `File` > `Download` > `.csv format`.

5. Save it inside `csv` folder in root directory of the script.

### Getting credentials.json for GMail enabled googleapi

1. Go to the [Google Cloud Console](https://console.cloud.google.com).

2. Create a new project or select an existing project.

3. Enable the Gmail API:
    - In the Cloud Console, navigate to the "APIs & Services" > "Library" page.
    - Search for "Gmail API" and select it.
    - Click the "Enable" button to enable the API for your project.
    
4. Create credentials for your project:
    - In the Cloud Console, navigate to the "APIs & Services" > "Credentials" page.
    - Click the "Create Credentials" button and select "OAuth client ID".
    - Choose "Desktop app" as the application type (since you're running the script locally).
    - Fill in the name for the OAuth client ID and click the "Create" button.
    - You'll see your client ID and client secret on the next screen.

5. Generate a refresh token:
    - Download the JSON file for the created OAuth client ID by clicking on the download icon next to it.
    - Save the JSON file securely in the root folder of this repository.
    - Run any of the script for the first time. Refer [Executing the scripts](#executing-the-scripts) section for commands.
    - Browser window will open and ask you to select the account, choose `admin@kossiitkgp.org` (get access to it if you don't have).
    - Allow permission on that email to use just enabled __GMAIL API__.
    - `token.json` will be generated in the root directory of this repository and mailing will start.
    
6. Next time mailing will start automatically since `token.json` has been generated.

### Executing the scripts

Here is the description on how to execute the scripts:

```graphql
python3 rejection-mailing-bcc.py (path to csv file containing rejected students details)
python3 task-mailing.py (path to csv file containing detals about students and task for a particular day) (day, DD MON YEAR [Task submission deadline])
```

Here is an example:

```bash
python3 rejection-mailing-bcc.py csv/rejected.csv
python3 task-mailing.py csv/day2.csv "Tuesday, 23 May 2023"
```