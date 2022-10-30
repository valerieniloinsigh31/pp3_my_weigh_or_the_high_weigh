![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


<h2><b>Table of contents</b></h2>

<b>User Experience</b>

<b>Project Goals</b>
User Goals: Show the results of the weight loss programme on a weekly basis for six programme participants within a similar control group in order to advertise the programme 'My Weigh or the High Weigh'
User Stories:
-The intended user is the personal trainer who is tracking his/her clients who are all following the 'My Weigh or the High Weigh' weight loss programme.
-The app enables the user to easily access information and to glean quick insights from the data using the various functions. It is an app design to assist a personal trainer to track their clients.
-The app will inform the shape of the weight loss programme, alerting the personal trainer to changes that may be necessary and how effective the weight loss programme is for the clients on an individual weekly and overall basis. The various functions, such as details on weekly weight change', details on total overall weight change and whether a client met their expected weekly weight loss offer immediate feedback to the user. This influences the exercise and nutritional adjustments that may need to be made and highlights what clients need to be developed further/focussed on for the upcoming week. The programme is a malleable, rolling programme and the expectations are adjusted each week based on the feedback from the app.
-There is a function that divides clients into those that met their weight loss expectations and those that didn't. Those that did not meet their weight loss goals are highlighted in red and the user is given an option to access their contact details. The user can then send an email to the client to get direct feedback as to why the setback may have occurred (e.g. social even, injury, diet, didn't meet exercise goals etc.). The setbacks will be documented accordingly and considered in the weight loss programme going forward.
-The app also offers overall insights into the success of the programme that can inform advertising or assist with advertising for a future intake of clients, for example with the weight loss range function, the user can readily and easily access the average range of weight loss on an overall total programme to-date basis as well and this can be used for advertisement purposes on instagram and facebook in order to promote the program to the next intake of clients.
-Weekly and overall weight loss is present in kg and % format.
-A relatively small control group of six men in their thirties with similar sedentary full-time professions, who had small families with moderate exercise levels to start with was taken so that they were directly comparable.
-Effectiveness of supplements for weight loss: One distinguishing element between the candidiates was that some wanted to take supplements (whey isolate protein and createin monohydrate) and half of the group did not. The clients who used supplements were distinguished with a '*'. This will enable the user to track whether there was any noticeable trends for the users of supplements versus those who opted not to use them. Variations could include increased energy levels, accelarated level of muscle gain or potential a lesser level of weight loss due to water retention initially. Distinctions between the groups will be noted more in the long-term and may not be evident within the nine week timeframe currently available.


<b>Design Choices:</b>
As this is a back-end app, with minimal levels of design, the functional design was the key focus, such as the clarity of the font and sizing and the green versus red font coloring of the clients who had met their weight loss expectations versus those who had not met their weight loss expectation.
Color scheme: Python format-how it will be viewed, does not allow for much design
Typography: The typography should be clear, energetic and consistent. It should enable the data to be presented in a way that is clear, not over crowded, confusing or muddled.

<b>Planning</b>
I used both Balsaimq Wireframes and Lucidchart Flowchart to assist in planning out the intent and functions of the app. Please see the extracts below:

Balsamiq Wireframes:

Lucidchart flowchart:
Please see excerpt below:

Several tabs

<b>Features</b>

<b>Existing Features</b>
Drawing influence from the 'Love Sandwiches' walkthrough project, I am drawing insights from a database maintained on google sheets and extracting various insights using functions that present the information in a useful way to the user.
Some of the features/functions include:
-Log in: Username and password required. This is to ensure that only the personal trainer(user) who has created the username and password has access to the  weight loss information.
Error-handling: These are a number of functions/code instances inserted that trigger errors if the correct information is not input (for example when the user needs to type in the latest week 9 week-end weigh-in information, the information must be for all six of the clients in kg format, accordingly, errors will be triggered if it is not in numerical format, if it is not a float and if less than six values are entered)
-The user is given options to prompt a number of different functions that offer different insights into the progress of the candidates so far, such as:
-Calculate the change in weight for the latest week on a client-by-client basis
-Calculate the total change in weight on a client-by-client basis
-Calculate which clients met weight loss expectations and which didn't
-Bring up contact information for those that did not meet their weight loss expectation so that the personal trainer (user) can get more feedback
-Calculate week with maximum and minimum weight loss
-Calculate total weight loss range over programme to date
-Also, user can assess whether there were any emerging trends between candidates who used supplements and those who didn't

<b>Features Left to Implement</b>

-Start to import visualizations of the data e.g. Pie charts and graphs
-Enable function where clients can input their own comments during the week outlining reasons for setbacks. These can be prompted once a candidate is listed as not meeting expectation and the client comments will offer immediate feedback ( e.g. if they overate, didn't make it to the gym, had a wedding etc.). This will save the personal trainer from having to contact them after the fact
-An additional feature to incorporate going forward will be connecting the app with automatic texting. The personal trainer (user) can trigger updates to be sent to the client the moinute data is input

<b>Database Design</b>

<b>Technologies Used:</b> Python, APIs (Google Sheets)

<b>Languages:</b> Python

<b>Frameworks, Libraries & Programs:</b> Math...Dateandtime

<b>Testing:</b> PIP3 install was sued for testing on the GITHUB terminal itself as there appeared to be an issue with the PEP8 validator

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

Content-git commit messages website per assessor feedback provided on PP2, made an effort to name my git commits more imperative

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




