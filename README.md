![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


<h2><b>Table of contents</b></h2>

<b>User Experience</b>

<b>Project Goals</b>
User Goals: To track the weight loss progress of a selection of clients in order to monitor, adjust and advertise a personal training weight loss programme, 'My Weigh or the High Weigh'
User Stories:
-The intended user is the personal trainer who is tracking his/her clients who are all following the 'My Weigh or the High Weigh' weight loss programme.
-The app enables the user to easily access information and to glean quick insights from the data using the various functions. It is an app designed to assist a personal trainer to track their clients.
-The app will inform the implementation/weekly design of the weight loss programme, alerting the personal trainer to changes that may be necessary and how effective the weight loss programme is for the clients on a weekly and inception-to-date basis. The various functions, such as details on weekly weight change and whether a client met their expected weekly weight loss offer immediate feedback to the user. This influences the exercise and nutritional adjustments that may need to be made and highlights what clients need to be developed further/focussed on for the upcoming week. The programme is a malleable, rolling programme and the expectations are adjusted each week based on the feedback from the app. The feedback function also allows the user to access stored client feedback from the week that may explain deviations from weight loss expectation without having to pursue further explanation.
-There is a function that divides clients into those that met their weight loss expectations and those that didn't. There two sub groups are printed in two separate lists to offer concise, easily interpreted feedback for the user. The user is then given the option to select which clients they would like to see the stored weekly feedback from. The idea here is that the user is more inclined to want to see the feedback from those who did not meet expectation. The function that follows this allows the user to bring up contact details for various clients where required. The idea here is that the user may want to follow up with clients whose feedback did not align with their results. The user can then send an email to the client to get direct feedback as to why the setback may have occurred (e.g. social even, injury, diet, didn't meet exercise goals etc.). The setbacks will be documented accordingly and considered in the weight loss programme going forward. 
-The app also offers overall insights into the success of the programme that can inform advertising or assist with advertising for a future intake of clients, for example with the weight loss range function, the user can readily and easily access the range of weight loss (minimum-maximum) from the date of inception of the programme to present and this can be used for advertisement purposes on instagram and facebook etc., in order to promote the program to the next intake of clients.
-Weekly and overall weight loss is present in kg and must in numerical format and include decimal places.
-A relatively small control group of six men in their thirties with similar sedentary full-time professions, who had small families with moderate exercise levels prior to starting the programme were selected so that they were directly comparable.
-Effectiveness of supplements for weight loss: One distinguishing element between the candidiates was that some wanted to take supplements (whey isolate protein and createin monohydrate) and half of the group did not. The clients who used supplements were distinguished with a '*'. This will enable the user to track whether there was any noticeable trends for the users of supplements versus those who opted not to use them. Variations could include increased energy levels, accelarated level of muscle gain or potential a lesser level of weight loss due to water retention initially. Distinctions between the groups will be noted more in the long-term and may not be evident within the nine week timeframe currently available.


<b>Design Choices:</b>
As this is a back-end app, with minimal levels of design, the functional design was the key focus, such as the cover image, the clarity of the language used, the order of the functions and the green versus red font coloring of the clients who had met their weight loss expectations versus those who had not met their weight loss expectation.
Color scheme: Imported the colorama module and added to requirements.txt so that the 
two variance lists could be coloured separately (green/red)
Typography: The typography should be clear and consistent. It should enable the data to be presented in a way that is clear, not over crowded, confusing or muddled. This was ensured with spacing, language and use of '\n'.

<b>Planning</b>
I used both Balsaimq Wireframes and Lucidchart Flowchart to assist in planning out the intent and functions of the app. Please see the extracts below:

Balsamiq Wireframes:

Lucidchart flowchart:

Please see excerpts below:

I started with extremely detailed notes and planning descriptions and refined this as I went.

Goals:
Order of the functions:

<b>Features</b>

<b>Existing Features</b>
-Drawing influence from the 'Love Sandwiches' walkthrough project, the project is drawing insights from a database maintained on google sheets and extracting various insights (using functions) that present the information in a useful way to the user.
Some of the features/functions include:
-Log in: Username and password required. This is to ensure that only the personal trainer(user) who has created the username and password has access to the  weight loss information. 
Error-handling: These are a number of functions/code instances inserted that trigger errors if the correct information is not input (for example when the user needs to type in the latest week 9 week-end weigh-in information, the information must be for all six of the clients in kg format, accordingly, errors will be triggered if it is not in numerical format, if it is not a float and if less than six values are entered)...such as Log In, Entering latest weigh-in data, Choosing client for feedback and contact information
-The user is given options to prompt a number of different functions that offer different insights into the progress of the candidates so far, such as:
-Calculate the change in weight for the latest week on a client-by-client basis
-Calculate which clients met weight loss expectations and which didn't
-Bring up contact information for those that did not meet their weight loss expectation so that the personal trainer (user) can get more feedback
-Calculate week with maximum and minimum weight loss and present as a range
-Also, user can assess whether there were any emerging trends between candidates who used supplements and those who didn't

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
GitHub: the respository for the projects code after being pushed from Git.
Heroku: is used to deploy the application and provides an enviroment in which the code can execute-installed via GITHUB Student Developer Pack as provided by CI Institute

<b>Testing:</b> 
PIP3 install was used for testing on the GITHUB terminal itself as there appeared to be an issue with the PEP8 validator

Installation performed per below comment extracted from Slack:


<b>Testing User Stories from User Experience (UX) Section</b>

<b>Further Testing</b>

<b>Known Bugs</b>

<b>Deployment</b> 
-This project was the first backend project (previous projects had been front end, HTML/CSS and Javascript)
-This project required activiation of the GITHUB Student Developer pack, as provided by the Code Institute, per the below:


-Activated Heroku and connect it to GITHUB profile per below:

I selected manual deployment for the Walkthrough ('Love Sandwiches project') but updated to automatic deployment for this project and, accordingly, it was automatically connected to Heroku for dpeloyment and the usual deployment process could be followed on GITHUB thereafter, per below:



<b>Credits:</b>
Code Institute tutorials-particualrly the functions and Slack
Font-what font did I choose and why
Font Awesome-icons, still motiviational and useful despite backend functionality
Ideas-'Love Sandwiches walkthrough project'
Slack-Read queries and viewed different student repositories on Slack when researching for my project:
Various student projects that I looked at included:
ramon
paul dwyer-choose your story
https://github.com/JoGorska/hotel-booking/blob/main/run.py- as specified in slack MVP doc

Content-git commit messages website per assessor feedback provided on PP2, made an effort to name my git commits more imperative
Video on installing colorama: https://www.google.com/search?q=import+colorama+python&oq=Import+colorama+python&aqs=chrome.0.0i512j0i22i30j0i390l3.6454j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=__K1eY9aBHcKYhbIP2vaq2AY_35

<b>Minimum Viable Product Logic</b>
Building on the success of PP2, I decided to not overly complicate my choice of project and to build on the knowledge acquired in tutorials and the walk-through project to layer on further code (using the walkthrough project code input as boilerplate code and editing this) as opposed to trying to implement entirely new concepts and code. 
 Additionally, I committed to more interaction with slack and the various supports (tutor/mentor) on this project as it had helped me greatly in PP2. I ensured to book my three recommended mentor meetings for this project and the inception meeting was extremely helpful as the mentor talked through my idea and offered insightful feedback with clear goals for the following mentor meetings.

As advised, I took on the assessors recommentations from the PP2 feedback and applied the suggested improvements to this project.

One of these recommendations, which I ensured to apply from the inception of PP3 was the ensuring the git commits were in imperative format. I received the following feedback from the assessor:

   'Going forward, ensure that all commit messages are in the imperative mood (Add…, Fix…, Style…, Edit…) and as descriptive as possible, within 50 characters, outlining the atomic change made. You can use the following link for reference on how to improve your commit messages - https://cbea.ms/git-commit/'

<b>Overview of the Project</b>
I decided choose a blend between project 0 and project 1 in that it is a survey of sorts but a repeated, accurate survey that follows specific data of specific people with a view to aiding in the implementation and application of a weight loss plan. The app is designed to assist personal trainers in tracking the progress of their clients and their programmes. The app will give the user an insight into how effective their weight loss programme is and inform them about what areas need to be adjusted. The purpose of the project is to offer insights on the implementation of a weight loss programme for control group of six different candidates of a similar profile (male, mid thirties, moderate level of activity, non-vegetarian, no food intolerances, each bringing up small, young families with sedentary professions). Half of the candidiates took a daily dose of whey isolate protein and creatine and the other half did not and therefore attempts will be made to gain insights from whether supplementation aided in weight loss/had an affect on the programme. Candidates will be asked to provide weekly explanations for setbacks in the programme, if applicable and these will be documented and added to the google sheets database.

Linking up with Google Sheets:
Imported libraries:
Refactoring code to streamline project: Is there any code that was refactored to streamline project:
Application Programming Interface (API)-Google Cloud Platform-walkthrough followed:
API-Google Drive and API-Google Sheets
Object Orientated Programming:
Importing external libraries:




