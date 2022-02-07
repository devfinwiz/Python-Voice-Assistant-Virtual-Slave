# Python-Voice-Assistant-Virtual-Slave

> This voice assistant is buit in VS Code. It has an ability to understand human speech, process it and provide relevant, requested output to the user. 
When the user speaks out any appropriate trigger words, the virtual assistant gets activated to serve the user's command.

## This Virtual Assistant currently performs the following:

1. Greets user with appropriate greetings after analyzing what time of the day it is. Also, introduces itself when user asks it to do so.

2. Opens the webpage as per user's request. (For example: youtube.com, linkedin.com).

3. Predicts time and speaks it out to the user whenever asked. 

4. Serves user with news from both economic times and hindustan times to get hold of both financial and non financial news headlines when asked to do so. 

5. Searches data as per user's request from the web.

6. Sends email on behalf of the user by accepting the content for the body of the mail from the user and acknowledges if the task was successful or not.

7. Creates a notepad for the user when asked to do so and accepts user's speech as input to write contents to the created notepad.

8. Fetches the content from the notepad whenever asked by the user to do so and displays the contents for user to read.

9. Fetches information from wikipedia for the user's requested topic and reads it out for the user along with displaying the same.

10. Maintains user's privacy by going deaf for specified amount of time when user commands it to not listen anything.

11. Opens application present on the system like notepad, paint whenever user commands it to do so. 

12. Has the ability to open requested youtuber's channel on youtube.com (for example: carry minati's youtube channel).

13. Keeps user entertained by reading out jokes to the user when user commands it to do so.

14. Has the ability to empty recycle bin for the user upon user's command while displaying the progress of the same using winshell.  

15. Logs off automatically with a warning that it is shutting down when user speaks out trigger words like bye,tata.

## Libraries to be installed:

> 1. pyttsx3
> 2. speech_recognition
> 3. wikipedia
> 4. winshell
> 5. pyjokes
> 6. time

### Installation can be done using the pip command. (Example: pip install pyttsx3)

### Note:

> If you encounter pyttsx3 initialization error, open command prompt and run the following:

> pip uninstall pyttsx3

> then

> pip install pyttsx3==2.71


## Inbuilt libraries required:

> 1. datetime
> 2. webbrowser
> 3. os
> 4. smtplib

### Note:

Before executing the script, make sure to turn on 'Less Secure App access' option from your gmail ID that will be used to send out the mails. To do so, get going with the following steps:

1.Log into the Gmail account that will be used to send the emails.

2.Go to Gmail's [Less Secure App Access](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NELkm6zvkeSQxzOL8a2UdhbIUASi6uvDQY573YvLX9rO1G5GHA4Um6YgEmGmZD6_Jc2tsqRDXuMf99mMud0Pslsov5MA)

3.Set the Allow less secure apps option to ON.
