![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


<h2><b>'My Weigh or the High Weigh'-the application to assist Personal Trainers in tracking their clients.</b></h2>


<h3><b>Minimum Viable Product Logic</b></h3>
<p>Building on the success of PP2, I decided to not overly complicate my choice of project and to build on the knowledge acquired in the python tutorials and the walk-through project to layer on further code (using the walkthrough project code input a foundation for my own project (data centric, math-based) and building my own code from this using this as a foundation) as opposed to trying to implement entirely new concepts and code.</p>

<p>Additionally, I committed to more interaction with slack and the various supports (tutor support interactions/mentor meetings) on this project as it had helped me greatly in PP2. I ensured to book my three recommended mentor meetings for this project and the meetings were extremely helpful as the mentor talked through my idea and offered insightful feedback with clear goals for the following mentor meetings.</p>

<p>As advised, I took on the assessors recommendations from the PP2 feedback and applied the suggested improvements to this project. One of these recommendations, which I ensured to apply from the inception of PP3 was the ensuring the git commits were in imperative format. I received the following feedback from the assessor:

   'Going forward, ensure that all commit messages are in the imperative mood (Add…, Fix…, Style…, Edit…) and as descriptive as possible, within 50 characters, outlining the atomic change made. You can use the following link for reference on how to improve your commit messages - https://cbea.ms/git-commit/'.
   </p>

<b>Overview of the Project</b>

<P>I decided to choose a blend between project 0 and project 1 in that it is a data-centric survey of sorts but a repeated, accurate survey that follows specific data of specific people with a view to aiding in the implementation and application of a weight loss plan. The app is designed to assist personal trainers in tracking the progress of their clients and their programmes. The app will give the user an insight into how effective their weight loss programme is and inform them about what areas need to be adjusted. The purpose of the project is to offer insights on the implementation of a weight loss programme for a control group of six different candidates of a similar profile (male, mid thirties, moderate level of activity, non-vegetarian, no food intolerances, each bringing up small, young families with sedentary professions). Half of the candidiates took a daily dose of whey isolate protein and creatine (denoted by a star beside their name) and the other half did not and therefore attempts can be made by the user to gain insights from whether supplementation aided in weight loss/had an affect on the programme. Candidates will be asked to provide weekly explanations for setbacks in the programme, if applicable and these will be documented and added to the google sheets database.</p>

<b>User Experience</b>

<b>Project Goals</b>
<b>User Goals:<b>
<p>
 To track the weight loss progress of a selection of clients in order to monitor, adjust and advertise a personal training weight loss programme, 'My Weigh or the High Weigh'</p>
<b>User Stories:</b>
<ul>
<li>The intended user is the personal trainer who is tracking his/her clients who are all following the 'My Weigh or the High Weigh' weight loss programme.</li>
<li>The app enables the user to easily access information and to glean quick insights from the data using the various functions. It is an app designed to assist a personal trainer to track their clients.</li>
<li>The app will inform the implementation/weekly design of the weight loss programme, alerting the personal trainer to changes that may be necessary and how effective the weight loss programme is for the clients on a weekly and inception-to-date basis. The various functions, such as details on weekly weight change and whether a client met their expected weekly weight loss provide immediate feedback to the user. This influences the exercise and nutritional adjustments that may need to be made and highlights what clients need to be developed further/focussed on for the upcoming week. The weight loss programme is a malleable, rolling programme and the expectations are adjusted each week based on the feedback from the app. The feedback function also allows the user to access stored client feedback from the week that may explain deviations from weight loss expectation without having to pursue further explanation.</li>
<li>There is a 'variance_split' function that divides clients into those that met their weight loss expectations and those that didn't. Two sub groups are printed into two separate lists to offer concise, easily interpreted feedback to the user. The user is then given the option to select which clients they would like to see the stored weekly feedback for with the 'feedback' function. The idea here is that the user is more inclined to want to see the feedback from those who did not meet expectation. The 'contact' function that follows this allows the user to bring up contact details for various clients, where required. The idea here is that the user may want to follow up with clients whose feedback did not align with their weekly results. The user can then contact the client they desire in order to get direct feedback as to why the setback may have occurred (e.g. social event, injury, diet, didn't meet exercise goals etc.). The setbacks will be documented accordingly and considered in the weight loss programme going forward. The feedback will also inform the user about what to expect from clients going forward and potentially what questions need to be asked in planning for the weeks ahead.</p>
<p>The app also offers overall insights into the success of the programme that can inform advertising or assist the user with advertising for a future intake of clients, for example with the weight loss range function, the user can readily and easily access the range of weight loss (minimum-maximum) from the date of inception of the programme to present and this can be used for advertisement purposes on instagram and facebook etc., in order to promote the program to the next intake of clients.</p>
<p>Weekly and overall weight loss is present in kg and must in numerical format and include decimal places. Error handling validations and print messages have been included in the code to ensure the user is informed about this.</p>
<p>Effectiveness of supplements for weight loss: One distinguishing element between the candidiates was that some wanted to take supplements (whey isolate protein and createin monohydrate) and half of the group did not. The clients who used supplements are distinguished with a '*' in the google sheets and the terminal. This will enable the user to track whether there was any noticeable trends for the users of supplements versus those who opted not to use them. Variations could include increased energy levels, accelarated level of muscle gain or potentially a lesser level of weight loss due to water retention initially. Distinctions between the groups will be noted more in the long-term and may not be evident within the nine week timeframe currently available. The user can use this valuable feedback to inform their recommendations on supplements going forward.</p>


<b>Design Choices:</b>
<p>As this is a back-end app, with minimal levels of design, the functional design was the key focus, such as the cover image, the clarity of the language used, the order of the functions and the use of colorama to distinguish sections of font. For example green versus red font coloring font coloring of the clients who had met their weight loss expectations versus those who had not met their weight loss expectation.</p>
<p>Color scheme: Imported the colorama module and added to requirements.txt so that the two variance lists could be coloured separately (green/red) and different functions coloured accordingly to signify different sections.</p>
<p>Typography: I aimed for the typography to be clear and consistent. It should enable the data to be presented in a way that is clear, not over crowded, confusing or muddled. This was ensured with spacing, language, color, 'press x to continue' inputd and use of '\n'.</p>
<p>Opening image: I implemented a cover photo of a bodybuilder that fits in with the theme of the app as per below:

![alt text](.//images/bodybuilder_image.png);</p>


<b>Planning</b>
<p>I used Lucidchart Flowchart to assist in planning out the intent and functions of the app. Please see the extracts below:</p>

<b>Lucidchart flowchart:</b>

Please see screengrabs from my <b>Lucidchart</b> planning process below:

![alt text](.//images/lucidcharts_plan.png);
![alt text](.//images/lucidcharts_overall_flow.png);
![alt text](.//images/lucid_functions_1.png);
![alt text](.//images/lucid_functions_2.png);


<ul>
<li>I started with extremely detailed notes and planning descriptions and refined this as I went.</li>
<li>The visual aspect of the lucid chart images greatly assisted me in formulating the logic needed in designing each of my functions.</li>
</ul>

<b>Goals</b>
<p>When plotting the functions, I always had in mind what I wanted the user to achieve with the app. I wanted the app to perform a number of functions that would be useful for a personal trainer in order to keep track of their clients.</p>
<b>Order of the functions:</b>
<p>The order of the functions is extremely important in this app as some functions rely on the previous function running prior to them so the data required has been populated. The omission or failure of one function would have a negative impact on other functions throughout the app, so I was particularly careful in considering this. Additionally, one limitation of the app in its current format is the variance_split function is not dynamic and as such requires manual editing after running the app to ensure that the app will run without issue for the following user. Careful consideration was given to the order of the functions and what google sheets tabs needed to be populated in order to fill various rows that the next function relied on. Additionally, indentation and nested functions were carefully considered.</p>

<b>Features</b>

<b>Existing Features</b>
<p>Inspired by the 'Love Sandwiches' walkthrough project, this app is manipulating a stored, malleable database maintained on google sheets and extracting various insights (using functions) that present the information in a useful way to the user.</p>

<b>Some of the features/functions include:</b>
<ul>

<li>Log in: Username and password required. This is to ensure that only the personal trainer(user) who has created the username and password has access to the  weight loss information. The function validation is linked with the username and password stored on google sheets so is easily adapted and tracked by the user.</li>
<li>Error-handling: These are a number of functions/code instances inserted that trigger errors if the correct information is not input (for example when the user needs to type in the latest week 9 week-end weigh-in information, the information must be for all six of the clients in kg format, accordingly, errors will be triggered if it is not in numerical format, if it is not a float and if less than six values are entered). Also in the Log In function, recursion is used so that the function continually loops to the beginning if the correct username and password is not entered. Additionally, in the client feedback and contact information sections, the user must input a choice of '1-7' and if the choice is invalid the function will not work. .</li>
<ol>The user is given options to prompt a number of different functions that offer different insights into the progress of the candidates so far, such as:
<li>-Calculate the change in weight for the latest week on a client-by-client basis.</li>
<li>Calculate which clients met weight loss expectations and which didn't.</li>
<li>Brings up client comments logged during the week in order to provide the personal trainer with insight.</li>
<li>Bring up contact information for those that did not meet their weight loss expectation so that the personal trainer (user) can get more feedback.</li>
</ol>
<li>Also, half of the clients used supplements (as denoted by the star beside their name) and half did not. This will enable the user to monitor and analyse whether there were any emerging trends between candidates who used supplements and those who didn't over a longer timeframe.</li>
</ul>

<h2><b>Features that could be implemented in future</b></h2>

<b>More elaborate design.<li><

<p>The current design is relatively minimal. In future versions, HTML/CSS and Javascript could be employed to make the website more pleasing and potentially easier to comprehend/use for the personal trainer. (E.g. added progress pics for the clients, scroll bars, the ability to navigate to different tabs, video demonstrations, sign-up forms etc.)</p>

<b> Incorporate visualizations of client progress.</b>

<p>The analysis of the data is currently only in numerical format but this could be paired with Tableau to produce visual representations of the data (e.g. Pie charts and graphs) that will give the user an even faster insight into he progress of their clients. These visualisations could also be shared with the clients to increase their understanding.</p>

<b>Clients interacting with google sheets.</b>

<p>As the app is linked with google sheets and updated from there, in future the clients will be log into the app themselves to input their own weekly feedback comments during the week, outlining reasons for setbacks, as opposed to the user having to input the feedback themselves during the week.This will save the personal trainer from having to contact them all together in the same evening and allows the clients to convey feedback even when it is not possible to contact the personal trainer.</p>

<b>Connect with emails</b>

<p>An additional feature to incorporate going forward will be connecting the app with automatic emails. The idea is that the personal trainer (user) can trigger updates to be sent to the client to alert them to their progress. Based on the user's analysis of the data, the email could outline an approach for the client to apply going forward, as well as attaching various relevant diet/training plans that would suit the client's situation. These plans could be saved to the database also and could address specific challenges (e.g. if client is travelling all week and can only perform body weight exercises or has limited capability to cook food).</p>

<b>Expanding data stored and adding more functions</b>
<ol>
<li><b>Stored plans.</b>
<p>Various suggested adjustments/updated plans could be written by the personal trainer, saved to the database and prompted based on client progress. This would include nutritional adjustments and exercise programme adjustments that include tweaks that can be made that are specific to different client situations. These can be stored on the system, listed within a function and triggered based on the users analysis of weekly data and the requirements of the client. (e.g. if it is known/disclosed in the feedback that a client will be travelling all week and will not have access to a gym, there could be a separate alternative plan saved to the system (outlining food types to target e.g. getting plain, easily trackable foods at airports and different exercises to use e.g. outdoor running, bodyweight exercises etc.)) This will save the user a lot of time as he/she will not need to continuously redraw different programmes and can mail these directly to the client. It also decreases the likelihood of prochrastination as all the information will be stored and readily available.</p></li>

<li><b>Additional functions</b>
<p>Two other useful functions that will be added to the app in future will be a function that calculates the 'range of weight loss' from the inception of the programme to date. This could be done using MAX and MIN formulae and an f print statement. The range function would assist with advertising the programme and keeping current clients motivated.  Another function that will be added is a fuction that calculates the average weekly weight loss per client and the averaage total weight loss per client from the date of inception of the prgramme to present. This function could provide valuable insight to the personal trainer with regard to overall progress of the program and whether certain times promoted or hindered more or less weight loss (e.g. Christmas holidays might cause the average total weight loss to decrease). It also would be useful for advertising and motivational purposes.</p></li>
</ol>

<b>Database Design</b>

<h2><b>TECHNOLOGIES USED</b></h2>

<b>Language Used:</b> Python 3.8.10

<b>Frameworks, Libraries & Programs:</b> 
<p>
<ul>
<li>Google Spreadsheets: this is linked in with Github and used as the external data source for the client data-enabled as per Code Institute tutorial.</li>
<li>Google Drive API: this was used to generate the credentials for the project in order to securely access the Google Spreadsheet. Followed the process as outlined in the Code Institute tutorial.</li>
<li>Google Sheets API: this is used to support the interactions between the Github code and the data stored in the Google Spreadsheet, set up per the process outlined in the Code Institute tutorial.</li>
<li>gspread: Python API for Google Sheets imported to project-imported as per the instruction given in the Code Insitute tutorial.</li>
<li>Google Auth: Google authentication library for Python required to use the credentials generated for Google Drive API-imported per the Code Insitute tutorial.</li>
<li>Lucidcharts (as mentioned on 'Love Sandwiches' tutorial). Signed up for a trial with Lucidcharts to enable me to use an unlimited number of tabs in my planning process. Used to create the flowcharts outlining the functionality of the project at planning stage.</li>
<li>Git: As per other projects, I used Git for version control. I input code on the Gitpod terminal, committed this to Git and pushed it to GitHub on a regular basis.</li>
<li>GitHub: holds the project repository once the code has been pushed from Git.</li>
<li>Heroku: used to deploy the application and provides an environment in which the code can execute (provides direct feedback as to the effectiveness of the code). As per the Code Institute tutorial, installed using GITHUB Student Developer Pack authentication code provided by Student Care. Connected Heroku with GIT per the Code Institue tutorial. Initially for demonstrative purposes, manual deployment selected in order to track how this is done and for the project, updated to automatic deployment. This linked with Git and deployed on Gitpod following the usual process as per other projects.
</ul>
</p>

<b>Testing:</b> 
<p>'pip3 install pycodestyle' was used for testing on the Gitpod terminal itself as there appeared to be an issue with the PEP8 validator</p>

<p>Installation performed per below comment extracted from Slack:</p>

![alt text](.//images/testing_pip3installation.png);

Gitpod->Python Select Linter->pycodestyle

Linter:
![alt text](.//images/testing_linter.png);

Codestyle:
![alt text](.//images/testing_pycodestyle.png);

<b>Testing User Stories from User Experience (UX) Section</b>
<b>Testing on Gitpod</b>
I tested the app prior to deployment several times, using the following code on Gitpod:
'python3. -> run.py'

<b>Testing on the live Heroku App</b>
I also tested the app several times once deployed on Heroku and updated based gitpod based on any issues noted.


All functions worked accordingly (eg the login function worked with the correct inputs, the latest weigh-in information was accepted, the change in weight loss was calculated correctly, the variance from expectation was calculated correctly and split into two rows, the feedback and contact information printed accurately) but I noted the requirement for a manual reset/deletion of appended rows at the end of each run due to some of the functions/formulae being manual and not dynamic. This limitation is further discussed in the bugs section.

<h2><b>Further Testing</b></h2>

<b>Known Bugs</b>
<b>Formula that are not dynamic within some tabs.</b>
<p>A limitation of the app design is that there are a number of tabs with manual formulae included within the Google Sheets document that have rows that are not dynamic and thus require manual adjustment on each run of the app. For example, the variance_split function as per below screengrab, the division into two separate lists (those who met expectation and those who did not meet expectation) is currently done based on the latest appended row in the variance tab but the formula is not dynamic and must be manually updated if another, further row is added. A tab each is given for each list. Variance green=those who met expectation and variance red=those who did not meet expectation. The names only populate if a condition in the formula is fulfilled and this is what makes the function work. In future versions, an effort will be made to make the formula in these two tabs dynamic so they change once another row is added (using COUNTA):</p>

variance green tab: 
![alt text](.//images/variance_split_greenlist.png);
variance red tab:
![alt text](.//images/variance_split_redlist.png);

<p>Conditional formatting has been add to the variance tab within google sheets to highlight visually those who met and did not meet expectation (so the user can quickly check this also):</p>

conditional formatting in variance tab: 
![alt text](.//images/variance_conditionalformatting.png);

 <p> The code is written in a certain order so that everything works and is populated in the correct order. But, the manual formulae will require update on each additional entry of the app.</p>

 <p> This limitation also applies to the expected weight change ('expected_wc') tab as currently the weight change for week 9 is a manual formula (the average of the first 8 weeks). On each run of the app, in order to be accurate the user would need to drag this formula down to the next row prior to running the app. In future versions, this could be made dynamic by making the expected_weight loss calculation a function within the app itself.</p>

 manual formula in 'expected_wc' tab:
 ![alt text](.//images/expected_wc.png);


<h2><b>Deployment</b></h2>

<p>This project was the first backend project (previous projects had been front end, HTML/CSS and Javascript)</p>

<p>This project required activation of the GITHUB Student Developer pack, as provided by the Code Institute, per the below:</p>

<p>Per Slack, requested Github Student Developer Pack activation email and activated accordingly once received. Please see relevant screengrabs below:</p>

<li>Email from CI with activation code:

![alt text](.//images/github_studentdeveloper_code.png); </li>

<li>Email re upgrade to student developer:

![alt text](.//images/github_developer_active.png);</li>

<p>Activated Heroku and connected it to GITHUB profile per below:</p>

![alt text](.//images/heroku_deploymentmethod.png);

<p>I selected manual deployment for the Walkthrough ('Love Sandwiches project') but updated to automatic deployment for this project and, accordingly, it was automatically connected to Heroku for deployment and the usual deployment process could be followed on GITHUB thereafter, per below:</p>

<h2><b>General overview on pinning the Gitpod repository to workspaces and using Heroku for deployment</b></h2>

<b>Steps to pin repositary to workspaces followed per the Code Institute tutorial</b>
<ol>
<li>I set up repositary using the python template provided by the Code Institute</p>
<li>Once the gitignore file was updated to include the cred.json file extracted from google sheets linking, I pinned the repositary to github workspaces so that I could open it without selecting 'gitpod' on each occassion (as this would reset the gitignore fail and exclude the creds file). Please see repositary pinned to workspaces below:

![alt text](.//images/workspaces.png);


<p>By connecting the Heroku to Gitpod and selecting 'automatic deployment', any changes pushed to the main branch were also immediately applied to the live project on Heroku.
 Also, in a reciprocative way, any data changes made through the use of the application are applied to the Google spreadsheet (e.g. the function where the latest weights are inserted in the Heroku app, this immediately updates the 'week_ends' tab in Google Sheets to include the values entered)</p>
</ol>

<h2><b>Detailed step-by-step of set-up of App</b></h2>

<h2><b>How to create and configure the Google spreadsheet and APIs</b></h2>

<b>Steps to setup and configure access to data-completed as per Code Institute tutorial</b>

<p>I followed the instructions provided by the Code Institute in the walkthrough 'Love Sandwiches' project, I set up APIs using the Google Cloud Platform.</p>

<b>Created the Google Spreadsheet</b>

<li>I logged into my Google account-e.g. I went to gmail and opened google sheets.</li>
<li>I created a Google Spreadsheet called 'my_weigh_or_the_high_weigh' on the Google Drive with several tabs for different functions:'login_info, weight change etc', per below screengrab:

![alt text](.//images/googlesheets_myweigh.png)

</li>

 <b>Setup Google Drive credentials</b>

<li>I clicked on the hamburger menu in the top left of the screen to access the navigation menu.</li>

<li>On the left hand menu, I selected 'APIs and Services' and then selected 'Library'.</li>

<li> I searched for the Google Drive API. I selected the Google Drive API and enabled it, to get to the API and Services Overview page.</li>

<li>I clicked on the 'Create Credentials' button.</li>

<li>I selected 'Google Drive' API from the dropdown for 'Credential Type'.</li>

<li>I selected 'Application Data' in response to 'What data will you be accessing'</li>

<li>On the Create Service Account page, for step 1, I entered a service account name in the first text box. Any value could be entered here. I then clicked on 'Create and Continue'</li>

<li>For step 2, 'Grant this service account access to project', I selected Editor from the 'Select a Role' dropdown and then clicked continue</li>

<li>On step 3, 'Grant users access to this service account', I selected Done, as no input was required here.</li>

<li>On the next page, I clicked on the service account name created (listed under the Service Accounts area) to go to the configuration page.</li>

<li>In the  KEYS tab, I clicked on the 'Add Key' dropdown and selected 'Create New Key'.</li>

<li>I selected the JSON radio button then clicked Create. The json file with the new API credentials downloaded.</li>

<li>I renamed the downloaded file to 'creds.json' (as per CI tutorial). I ensured this filename was listed in the 'gitignore' file in the project. This was done on the 'Love Sandwiches' walkthrough project. </li>

<li>I copied the new creds.json file into the gitpod project</li>

<li>In the creds.json file, I copied the value for "client email" (excluding inverted commas) and then on the Google Drive, I pasted this exact address into the share with section. Share the spreadsheet created above with this email address, assigning a role of Editor. Please see image of share process shown below:</li>

Share Spreadsheet Image: ![alt text](.//images/googlesheets_share.png)

<b>Enabling Google Sheets APIs</b>

<li>I went back to the dashboard for the project on Google Cloud Platform and accessed the navigation menu.</li>
<li>On the left hand menu, I selected 'APIs and Services' and then 'Library'</li>
<li>I searched for the Google Sheets API and then enabled this.</li>


<b>I installed the gspread and google-auth libraries in the development environment using the command 'pip3 install gspread google-auth' as described in the walkthrough project.</b>

</ol>
<b>How this site was deployed to Heroku</b>
<b>Steps followed to deploy-as per the Code Institute tutorial</b>
<ol>
<li>The requirements.txt file in the project was updated to include details on the project dependencies.(e.g. I added the colorama module)</li>

<b>Steps to do this are :</b>
<ol>
<li>I entered the following command at the terminal prompt : 'pip3 freeze > requirements.txt'</li>
<li>I committed the resulting changes to requirements.txt and pushed to github.</li>

<b>Heroku</b>
<li>I activated the Github Student Developer Pack provided by the Code Institute</li>

<li>I created a Heroku account and logged in.</li>

<li>From the Heroku dashboard, I clicked the Create new app button.</li>

<li>On the Create New App page, I enter a unique name for the application and selected region as ''. Then, I clicked Create app.</li>

<li>Then I was brought to the 'Application Configuration' page.</li>

<li>I clicked on the Settings tab and went to the 'Config Vars' section to set up the private Environment Variables for the application, meaning the credentials used by the application in order to access the spreadsheet data.</li>

<li>I clicked on 'Reveal Config Vars'. In the field for key, I entered 'CREDS' and pasted the entire contents of the creds.json file in as the value, then clicked add.</li>

<li>I then went tothe Settings page to update the Buildpacks section. I clicked 'Add buildpack', and selected Python from the pop up window and then saved the changes. I then added another buildpack, selecting 'Node.js' from the pop up window saved. It is important that the buildpacks are listed Python first, then Node.js beneath as expressly stated in the Code Institue tutorials.</li>

<li>Then I moved to the Deploy tab on the 'Application Configuration' page.</li>

<li>I selected GitHub as the Deployment Method and confirmed that I wanted to connect to GitHub. I entered the name of the github repository (the one used for this project is 'https://github.com/valerieniloinsigh31/pp3_my_weigh_or_the_high_weigh') and clicked on 'Connect' to link up the Heroku app to the GitHub repository code.
Please see a screengrab of the Heroku deployment tab below, with Github having been connected:

![alt text](.//images/heroku_deploymentmethod.png);
</li>

<li>For deployment, two options are given on Heroku, either 'Automatically Deploy' each time changes are pushed to GitHub, or 'Manually deploy'. I selected automatical deployment for the project. (but did intially select manual deployment when setting up Heroku for 'Love Sandwiches' walkthrough)</li>

<li> The usual deployment process was followed on Github once it was connected to Heroku.
1. Go to repositary on Github.
2.Click on settings
3.Click on Github pages
4.In Github pages, in 'Build and Deployment' section, update branch to 'Main branch'.
5. Live project link should load after a minute.

Github deployment screengrabs:
Repositary:
![alt text](.//images/github_repositary.png);
Githubs pages:
![alt text](.//images/github_deploy_settings.png);
Live link:
![alt text](.//images/github_deploy_liveproject.png):

<li>The application can be run from the Application Configuration page by clicking on the Open App button. Please see screengrab below:

Open App on Heroku: ![alt text](.//images/heroku_openapp.png);
</li>
</ol>

<b>The live link for this project is https://pythonpp3.herokuapp.com/</b>

<b>Credits:</b>
<ul>
<li>Code Institute tutorials-particularly the 'Love Sandwiches' Walkthrough Project and Slack.</li>
<li>Ideas-'Love Sandwiches walkthrough project' and various projects listed on slack as well as the hotel bookings and event scheduler projects listed below (that were listed on the Project 3 pdf circulated on Slack)</li>
<li>Reviewed the following projects which were listed in 'The Importance of MVP-PP3' document shared on Slack:

Hotel Bookings (useful as also data-centric):https://github.com/JoGorska/hotel-booking/blob/main/run.py
Event Scheduler (useful as also data-centric): https://github.com/elainebroche-dev/ms3-event-scheduler
<p>The README for this project also influenced the format of my README.
I also drew inspiration from the format of the README from the Event Scheduler repositary.</p>
</li>
<li>Slack-Read queries and viewed different student repositories on Slack when researching for my project. I found the peer code review page particularly useful.</li>
<li>Colorama module-imported colorama module to enable me to color the font to make the presentation more distinct and readable. I watched the following video on installing colorama: https://www.google.com/search?q=import+colorama+python&oq=Import+colorama+python&aqs=chrome.0.0i512j0i22i30j0i390l3.6454j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=__K1eY9aBHcKYhbIP2vaq2AY_35</li>
<li>Cover image: ASCII Art Archive: https://www.asciiart.eu/sports-and-outdoors/other. Noted that a number of other projects added images from ASCII and I liked the aesthetic. I found a suitable image for my project and added this.</li>
<li>Per the assessor feedback on project 2, I tried to ensure my git commits were adequate, using the imperative format as outlined in the following: https://cbea.ms/git-commit/</li>

</ul>

<b>Various student projects that I looked at included:</b>
<ol>
<li>Laura Walsh-Adoption form app: https://github.com/lauralola/adoption_form_response</li>
<li>Paul Dwyer-Choose your own adventure app: https://github.com/Pauldwyer/Choose-your-adventure</li>
<li>Kevin McSherry-Horoscope apP: https://github.com/kevinmcsherry/Horoscope_P3</li>
</ol>







