![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


<h2><b>Table of contents</b></h2>

<b>User Experience</b>

<b>Project Goals</b>
User Goals: To track the weight loss progress of a selection of clients in order to monitor, adjust and advertise a personal training weight loss programme, 'My Weigh or the High Weigh'
User Stories:
-The intended user is the personal trainer who is tracking his/her clients who are all following the 'My Weigh or the High Weigh' weight loss programme.
-The app enables the user to easily access information and to glean quick insights from the data using the various functions. It is an app designed to assist a personal trainer to track their clients.
-The app will inform the implementation/weekly design of the weight loss programme, alerting the personal trainer to changes that may be necessary and how effective the weight loss programme is for the clients on a weekly and inception-to-date basis. The various functions, such as details on weekly weight change and whether a client met their expected weekly weight loss offer immediate feedback to the user. This influences the exercise and nutritional adjustments that may need to be made and highlights what clients need to be developed further/focussed on for the upcoming week. The programme is a malleable, rolling programme and the expectations are adjusted each week based on the feedback from the app. The feedback function also allows the user to access stored client feedback from the week that may explain deviations from weight loss expectation without having to pursue further explanation.
-Careful consideration was given to the order of the functions and what google sheets tabs needed to be populated in order to fill various rows that the next function relied on. Additionally, indentation and nested functions were carefully considered.
-There is a function that divides clients into those that met their weight loss expectations and those that didn't. Two sub groups are printed into two separate lists to offer concise, easily interpreted feedback to the user. The user is then given the option to select which clients they would like to see the stored weekly feedback for. The idea here is that the user is more inclined to want to see the feedback from those who did not meet expectation. The function that follows this allows the user to bring up contact details for various clients, where required. The idea here is that the user may want to follow up with clients whose feedback did not align with their weekly results. The user can then contact the client they desire in order to get direct feedback as to why the setback may have occurred (e.g. social event, injury, diet, didn't meet exercise goals etc.). The setbacks will be documented accordingly and considered in the weight loss programme going forward. The feedback will also inform the user about what to expect from clients going forward and potentially what questions need to be asked in planning for the weeks ahead.
-The app also offers overall insights into the success of the programme that can inform advertising or assist with advertising for a future intake of clients, for example with the weight loss range function, the user can readily and easily access the range of weight loss (minimum-maximum) from the date of inception of the programme to present and this can be used for advertisement purposes on instagram and facebook etc., in order to promote the program to the next intake of clients.
-Weekly and overall weight loss is present in kg and must in numerical format and include decimal places. Error handling validations and print messages have been included in the code to ensure the user is informed about this.
-A relatively small control group of six men in their thirties with similar, sedentary full-time professions and each rearing small families with moderate exercise levels prior to starting the programme were selected so that they were directly comparable.
-Effectiveness of supplements for weight loss: One distinguishing element between the candidiates was that some wanted to take supplements (whey isolate protein and createin monohydrate) and half of the group did not. The clients who used supplements are distinguished with a '*' in the google sheets and the terminal. This will enable the user to track whether there was any noticeable trends for the users of supplements versus those who opted not to use them. Variations could include increased energy levels, accelarated level of muscle gain or potentially a lesser level of weight loss due to water retention initially. Distinctions between the groups will be noted more in the long-term and may not be evident within the nine week timeframe currently available. The user can use this valuable feedback to inform their recommendations on supplements going forward.


<b>Design Choices:</b>
As this is a back-end app, with minimal levels of design, the functional design was the key focus, such as the cover image, the clarity of the language used, the order of the functions and the green versus red font coloring of the clients who had met their weight loss expectations versus those who had not met their weight loss expectation.
Color scheme: Imported the colorama module and added to requirements.txt so that the 
two variance lists could be coloured separately (green/red)
Typography: The typography should be clear and consistent. It should enable the data to be presented in a way that is clear, not over crowded, confusing or muddled. This was ensured with spacing, language and use of '\n'.

<b>Planning</b>
<p>I used Lucidchart Flowchart to assist in planning out the intent and functions of the app. Please see the extracts below:</p>

<b>Lucidchart flowchart:</b>

Please see excerpts below:

I started with extremely detailed notes and planning descriptions and refined this as I went.
The visual aspect of the lucid chart images greatly assisted me in formulating the logic needed in 
designing each of my functions.

Goals:
Order of the functions:

<b>Features</b>

<b>Existing Features</b>
-Drawing influence from the 'Love Sandwiches' walkthrough project, the project is manipulating a stored, malleable database maintained on google sheets and extracting various insights (using functions) that present the information in a useful way to the user.

<b>Some of the features/functions include:</b>
<ul>
<li>Log in: Username and password required. This is to ensure that only the personal trainer(user) who has created the username and password has access to the  weight loss information.</li>
<li>Error-handling: These are a number of functions/code instances inserted that trigger errors if the correct information is not input (for example when the user needs to type in the latest week 9 week-end weigh-in information, the information must be for all six of the clients in kg format, accordingly, errors will be triggered if it is not in numerical format, if it is not a float and if less than six values are entered)...such as Log In, Entering latest weigh-in data, Choosing client for feedback and contact information.</li>
<ol>
The user is given options to prompt a number of different functions that offer different insights into the progress of the candidates so far, such as:
<li>-Calculate the change in weight for the latest week on a client-by-client basis.</li>
<li>Calculate which clients met weight loss expectations and which didn't.</li>
<li>Bring up contact information for those that did not meet their weight loss expectation so that the personal trainer (user) can get more feedback.</li>
<li>Calculate week with maximum and minimum weight loss and present as a range.</li>
</ol>
-Also, user can assess whether there were any emerging trends between candidates who used supplements and those who didn't.
</ul>

<b>Features Left to Implement</b>

-Design that would be more pleasing for user:

It is quite paired backed and minimal design, in future HTML/CSS and Javascript could be employed to make the website more pleasing and potentially easier to comprehend/user for the user.

-Start to import visualizations of the data e.g. Pie charts and graphs. Could link up with Tableau etc to present visualisations comparing weekly data and making progress more comarable.

-Enable function where clients can input their own comments during the week outlining reasons for setbacks as opposed to the user having to input the feedback themselevs during the week. These can be prompted once a candidate is listed as not meeting expectation and the client comments will offer immediate feedback ( e.g. if they overate, didn't make it to the gym, had a wedding etc.). This will save the personal trainer from having to contact them after the fact

-An additional feature to incorporate going forward will be connecting the app with automatic texting. The personal trainer (user) can trigger updates to be sent to the client the minute the week-end weigh in data is entered to alert them to their progress.

-Various adjustments saved to the database and prompted based on progress. Nutritional adjustments and exercise programme adjustments that include tweaks that can be made that are specific to differen situations. These can be stored on the system, listed within a function and triggered based on the users analysis of weekly data and the requirements of the client. (e.g. if it is know that a client will be travelling all week and will not have access to a gym, there could be a separate alternative plan saved to the system (outlining food types to target e.g. getting plain, easily trackable foods at airports and different exercises to use e.g. outdoor running, bodyweight exercises etc.)) This will save the user a lot of time as he/she will not need to continuously redraw different programmes and can mail these dircetly to the client.

<b>Database Design</b>

<h2><b>TECHNOLOGIES USED</b></h2>

<b>Language Used:</b> Python 3.8.10

<b>Frameworks, Libraries & Programs:</b> 
Google Spreadsheets: used as the external data source for the client data-accessed per CI tutorial
Google Drive API: used to generate credentials used in the project to securely access the Google Spreadsheet-accessed per CI tutorial
Google Sheets API: used to support interactions (e.g. read/write functionality) between the code and data stored in the Google Spreadsheet-accessed per CI tutorial
gspread: Python API for Google Sheets imported to project-incorporated per CI tutorial
Google Auth: Google authentication library for Python required to use the credentials generated for Google Drive API-imported per cI tutorial
Lucidcharts (as mentioned on CI tutorial) used to create the flowcharts outlining the functionality of the project.
Git: used for version control via the Gitpod terminal to commit to Git and Push to GitHub.
GitHub: generates/contains the repository for the projects code after being pushed from Git.
Heroku: used to deploy the application and provides an environment in which the code can execute. As per CI tutorial, installed using GITHUB Student Developer Pack authentication code provided by Student Care. Connected with GITHUB per CI tutorial. Initially for demonstrative purposes, manual deployment selected in order to track how this is done and then alerted to automatic deployment linked with Github.

<b>Testing:</b> 
'pip3 install pycodestyle' was used for testing on the GITHUB terminal itself as there appeared to be an issue with the PEP8 validator

Installation performed per below comment extracted from Slack:
Gitpod->Python Select Linter->pycodestyle

Linter:
Codestyle:

<b>Testing User Stories from User Experience (UX) Section</b>

<b>Further Testing</b>

<b>Known Bugs</b>
One limitation of the design is that there are a number of tabs with manual formulae included within 
the Google Sheets document. The code is written in a certain order so that everything works and is populated in the correct order. But, the manual formulae will require update on each additional entry of the app. For example, there are two tabs, 'variance_green' and 'variance_red' that has manual formulas that splits the variance between expected weight loss and actual weight loss into the clients who met expectation and those that did not meet expectation. This formulae are linked to the newly appended row in the variance tab (e.g. row 10) so will not update on the next running of the app when another row is appended unless the formulae are manually updated (e.g. changed from row 10 to row 11). In future versions of the app, I could design a workaround of this to autmate this feature but for now, there is a printed reminded included at the end of the app, reminding the personal trainer 'Please update manual rows within google sheets before logging out.'


<b>Deployment</b> 
-This project was the first backend project (previous projects had been front end, HTML/CSS and Javascript)
-This project required activiation of the GITHUB Student Developer pack, as provided by the Code Institute, per the below:

-Per Slack, requested Github Student Developer Pack activiation email and activated accordingly once received
-Activated Heroku and connect it to GITHUB profile per below:

I selected manual deployment for the Walkthrough ('Love Sandwiches project') but updated to automatic deployment for this project and, accordingly, it was automatically connected to Heroku for dpeloyment and the usual deployment process could be followed on GITHUB thereafter, per below:

<h2><b>Clone the GitHub repository</b></h2>
<b>Steps to create a local clone-per CI tutorial</b>
<ol>
<li>Go to the https://github.com/elainebroche-dev/ms3-event-scheduler repository on GitHub</li>

<li>Click the "Code" button to the right of the screen, click HTTPs and copy the link there</li>

<li>Open a GitBash terminal and navigate to the directory where you want to locate the clone</li>

<li>On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process</li>

<li>Changes made to the local clone can be pushed back to the repository using the following commands:

git add filenames (or "." to add all changed files)
git commit -m "text message describing changes"
git push

N.B. Any changes pushed to the master branch will take effect on the live project because automatic deployments are enabled in Heroku for this project.

N.B. Any data changes made through the use of the application will take effect in the live project Google spreadsheet.
</ol>

<h2><b>How to create and configure the Google spreadsheet and APIs</b></h2>
<b>Steps to setup and configure access to data</b>
<ol>
<b>Create the Google Spreadsheet</b>
<ol>
<li>Log in to your Google account</li>
<li>Create a Google Spreadsheet called 'my_weigh_or_the_high_weigh' on the Google Drive with several tabs:''.</li>

Set up APIs using the Google Cloud Platform

Access the Google Cloud Platform

Create a new project and give it a unique name, then select the project to go to the project dashboard
</ol>

<b>Setup Google Drive credentials</b>

<li>Completed as per CI tutorial</li>

<li>Click on the hamburger menu in the top left of the screen to access the navigation menu</li>

<li>On the left hand menu select 'APIs and Services' and then 'Library'</li>

<li>>Search for Google Drive API</li>

<li>Select Google Drive API and click on 'enable' to get to the API and Services Overview page</li>

<li>Click on the Create Credentials button near the top left of the screen</li>

<li>Select 'Google Drive' API from the dropdown for 'Credential Type'</li>

<li>Select the 'Application Data' radio button in the 'What data will you be accessing' area</li>

<li>Select the 'No, I'm not using them' for the 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?' area</li>

<li>Cick Next</li>

<li>On the Create Service Account page, step 1 is to enter a service account name in the first text box. Any value can be entered here.</li>

<li>Click on 'Create and Continue'</li>

<li>On step 2, 'Grant this service account access to project', select Basic -> Editor from the 'Select a Role' dropdown.</li>

<li>Click on Continue</li>

<li>On step 3, 'Grant users access to this service account', select Done, no input is required</li>

<li>On the next page, click on the service account name created (listed under the Service Accounts area) to go to the configuration page for the new service account.</li>

<li>Click on the KEYS tab at the top middle of the screen.</li>

<li>Click on the Add Key dropdown and select Create New Key.</li>

<li>Select the JSON radio button then click Create. The json file with the new API credentials will download your machine.</li>

<li>Rename the downloaded file to creds.json. This filename is already listed in the project .gitignore file and so no further action will be needed to prevent it being accidentally uploaded to github. This was done on the 'Love Sandwiches' walkthrough project. Could name anything but ensure name is also included in .gitignore file.</li>

<li>Copy the new creds.json file into the local clone</li>

<li>In the creds.json file, copy the value for "client email" (excluding inverted commas) and then  on the Google Drive, paste this exact address into the share with section. Share the spreadsheet created above with this email address, assigning a role of Editor similar to the image shown below:</li>

Share Spreadsheet Image:


<b>Enable Google Sheets API</b>

<li>Go back to the dashboard for the project on Google Cloud Platform and access the navigation menu as before</li>
<li>On the left hand menu select 'APIs and Services' and then 'Library'</li>
<li>Search for Google Sheets API</li>
<li>Select Google Sheets API and click on 'enable'</li>


<b>Install gspread and google-auth libraries in the development environment using the command 'pip3 install gspread google-auth'</b>


</ol>
<b>How this site was deployed to Heroku</b>
<b>Steps followed to deploy-as per CI tutorial</b>
<ol>
<li>The requirements.txt file in the project was updated to include details on the project dependencies.</li>

<b>Steps to do this are :</b>
<ol>
<li>Enter the following command at the terminal prompt : 'pip3 freeze > requirements.txt'</li>
<li>Commit resulting changes to requirements.txt and push to github.</li>

<li>Log in to Heroku, create an account if necessary.</li>

<li>From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.</li>

<li>On the Create New App page, enter a unique name for the application and select region. Then click Create app.</li>

<li>You will then be brought to the Application Configuration page for your new app. Changes are needed here on the Settings and Deploy tabs.</li>

<li>Click on the Settings tab and then scroll down to the 'Config Vars' section to set up the private Environment Variables for the application - i.e. the credentials used by the application to access the spreadsheet data.</li>

<li>Click on 'Reveal Config Vars'. In the field for key enter 'CREDS' and paste the entire contents of the creds.json file into the VALUE field and click ADD. A description on the creation of the creds.json file is documented in 'How to create and configure the Google spreadsheet and APIs' section above.</li>

<li>Next, scroll down the Settings page to Buildpacks. Click Add buildpack, select Python from the pop up window and click on Save changes. Click Add buildpack again, select Node.js from the pop up window and click on Save changes. It is important that the buildpacks are listed Python first, then Node.js beneath.</li>

<li>Click on the Deploy tab on the Application Configuration page.</li>

<li>Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is INSERT REPOSITARY) and click on Connect to link up the Heroku app to the GitHub repository code.</li>

<li>Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Automatic Deploy was selected. (but did intially select manual deployment when setting up Heroku for 'Love Sandwiches' walkthrough)</li>

<li>The application can be run from the Application Configuration page by clicking on the Open App button.</li>
</ol>

<b>The live link for this project is (INSERT WHEN DEPLOYED)</b>

<b>Credits:</b>
Code Institute tutorials-particularly the 'Love Sandwiches' Walkthrough Project and Slack
Ideas-'Love Sandwiches walkthrough project'
Slack-Read queries and viewed different student repositories on Slack when researching for my project-a list of these influences included below
Modules imported:
RE-Email verification
Colorama-coloring font
Cover image: ASCII Art Archive: https://www.asciiart.eu/sports-and-outdoors/other

Various student projects that I looked at included:
Ramon Link:
Raul dwyer-choose your story
Kevin Sherries: Horoscope...importing lists informed my idea for bringing feedback in

Reviewed the following projects which were listed in 'The Importance of MVP-PP3' document shared on Slack:

Hotel Bookings (useful as also data-centric):https://github.com/JoGorska/hotel-booking/blob/main/run.py
Event Scheduler (useful as also data-centric): https://github.com/elainebroche-dev/ms3-event-scheduler
I also drew inspiration from the format of the README from the Event Scheduler repositary



Content-git commit messages website per assessor feedback provided on PP2, made an effort to name my git commits more imperative, informed the format of my commit messages: https://cbea.ms/git-commit/

Video on installing colorama: https://www.google.com/search?q=import+colorama+python&oq=Import+colorama+python&aqs=chrome.0.0i512j0i22i30j0i390l3.6454j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=__K1eY9aBHcKYhbIP2vaq2AY_35

<b>Minimum Viable Product Logic</b>
Building on the success of PP2, I decided to not overly complicate my choice of project and to build on the knowledge acquired in tutorials and the walk-through project to layer on further code (using the walkthrough project code input as boilerplate code and editing this/building my own code from this using this as a foundation) as opposed to trying to implement entirely new concepts and code. 

 Additionally, I committed to more interaction with slack and the various supports (tutor support interactions/mentor meetings) on this project as it had helped me greatly in PP2. I ensured to book my three recommended mentor meetings for this project and the inception meeting was extremely helpful as the mentor talked through my idea and offered insightful feedback with clear goals for the following mentor meetings.

As advised, I took on the assessors recommendations from the PP2 feedback and applied the suggested improvements to this project.

One of these recommendations, which I ensured to apply from the inception of PP3 was the ensuring the git commits were in imperative format. I received the following feedback from the assessor:

   'Going forward, ensure that all commit messages are in the imperative mood (Add…, Fix…, Style…, Edit…) and as descriptive as possible, within 50 characters, outlining the atomic change made. You can use the following link for reference on how to improve your commit messages - https://cbea.ms/git-commit/'

<b>Overview of the Project</b>
I decided choose a blend between project 0 and project 1 in that it is a data-centric survey of sorts but a repeated, accurate survey that follows specific data of specific people with a view to aiding in the implementation and application of a weight loss plan. The app is designed to assist personal trainers in tracking the progress of their clients and their programmes. The app will give the user an insight into how effective their weight loss programme is and inform them about what areas need to be adjusted. The purpose of the project is to offer insights on the implementation of a weight loss programme for control group of six different candidates of a similar profile (male, mid thirties, moderate level of activity, non-vegetarian, no food intolerances, each bringing up small, young families with sedentary professions). Half of the candidiates took a daily dose of whey isolate protein and creatine and the other half did not and therefore attempts will be made to gain insights from whether supplementation aided in weight loss/had an affect on the programme. Candidates will be asked to provide weekly explanations for setbacks in the programme, if applicable and these will be documented and added to the google sheets database.

OTHER CONSIDERATIONS:


Refactoring code to streamline project: Is there any code that was refactored to streamline project:
Object Orientated Programming: has any of this been included...
Iteration...loops instead..appending rows...can manual formula be made automated





