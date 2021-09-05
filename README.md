# SecureworksDellCodingChallenge
QA Automation Engineer Coding Challenge

**1) INTRODUCTION**

**2) TECHNOLOGY AND OTHER TOOLS**

**3) RECOMMENDATIONS**

**4) SET UP ENVIRONMENT TO RUN SCRIPTS**

**5) HOW TO RUN THE CODING CHALLENGE AND TEST CASES**

**6) ASSUMPTIONS IN GENERAL**

**7) ASSUMPTIONS ABOUT CODING CHALLENGE**

=====================================================

**1) INTRODUCTION**

This README file is a guideline on how to compile and run the test cases provided for the coding challenge. 
It provides the TECHNOLOGY that a user needs to have on her/his machine in order to run the Python application.
It also provide some ASSUMPTIONS made in order to run the test cases in a simple manner.

=====================================================

**2) TECHNOLOGY AND OTHER TOOLS**

In order to run this application, the user needs:
1) Python 3
2) pytest testing framework
3) macOS terminal 

=====================================================

**3) RECOMMENDATIONS**

For simplicity purposes, the coding challenge and its test cases have been designed to be run by having all the files in the same folder. Therefore, please extract files from git repository and store them in a single folder.
For example, if the user wishes to extract the files in the Desktop, the user should see something like this once this is done:

/Users/<user_name>/Desktop/<folder_created_by_user>/Words.txt
	
/Users/<user_name>/Desktop/<folder_created_by_user>/Transpose.py
	
/Users/<user_name>/Desktop/<folder_created_by_user>/test_transpose.py

/Users/<user_name>/Desktop/<folder_created_by_user>/requirements.txt

=====================================================

**4) SET UP ENVIRONMENT TO RUN SCRIPTS**

Note: This coding challenge was created using a macOS environment. This provides simplicity to the coding challenge since the user can run the coding challenge and its test cases from the terminal. No need for an IDE or any other platform (e.g. Visual Studio Code). 

In order to run this coding challenge, the user needs Python 3.

In case the user does not have Python installed please follow the steps provided on this site to download and install: 
https://docs.python-guide.org/starting/install3/osx/

Note: To check if Python has been installed, please run this command.
If  it's installed, the user will see a similar output to this:

	$ python3 --version (or $python, this depends on how users have their own environment setup)
	
The user should see a similar output like this:
	
	$ Python 3.9.5 (User might have a different version, as long as it is Python 3 the coding challenge should work) 
	
After the user has verified that has Python 3 on the machine, please follow these instructions:

1) Go to the directory where the user downloaded the files from the git repository. Following the directions on Step 3, run this command to go to that directory in the terminal:

		cd /Users/<user_name>/Desktop/<folder_created_by_user>
		
1) Create an environment by running this command in the terminal:

		python3 -m venv venv

2) Activate the environment by running this command in the terminal:

		source venv/bin/activate

3) Install the requirements file provided in the repository by running this command in the terminal:

		pip install -r requirements.txt

This command will setup all the dependencies needed to run the scripts including pytest. Once this is done, the user should be ready to run and test the coding challenge.

Optional: The user might see a warning stating that the environment has an old version of pip. Run the provided suggestion by the system to update pip in case you want this warning to not be prompted again.
	
=====================================================

**5) HOW TO RUN THE CODING CHALLENGE AND TEST CASES**

Note: Make sure that before running any of these commands you are located in the terminal inside the folder where all the files from Step 3 were stored.

1. Run the Coding Challenge by running this command in the command line:
	
	``$python3 Transpose.py``
	
3. Once the application has been verified that it's providing the correct result, run the test cases by running this command in the command line:
	
	``$pytest test_transpose.py``
	
NOTE: For simplicity purposes, I did not use any tool or framework other than those that were essential to create and run the test cases. Unfortunately, for this reason we cannot create Test Reports as we usually do when we have a complete environment setup correctly. In prior experiences when working with different languages and testing frameworks, I have been able to generate different type of reports, such as Pytest HMTL Test Reports or XML reports for Jenkins. 

=====================================================
	
**6) ASSUMPTIONS IN GENERAL**

* User is running the coding challenge and the test cases in a MacOS environment.
* User has placed the files inside the same folder created by the user.
* test (i.e. Words.txt) Text File exists inside the same folder as the other files created by the user.

=====================================================

**7) ASSUMPTIONS ABOUT CODING CHALLENGE**

* Text file will be called Words.txt. If the user wants to use a different file, please removed the original file and rename the new file to Words.txt
* There is one specific test case that checks the size of the file. Since the requirements do not specify the size, the assumption is that the file is no bigger than 1 gigabyte.
* There is one specific test case that checks the extension of the file. Since the requirements do not specify the file extension, the assumption is that the file will be a simple text file.
* There is one specific test case which checks specifically for the string returned to only have letters and/or numbers. Since the requirements did not specify what type of characters the text file should have, there is an assumption done that the file would only have alphanumeric characters.
* If there are 2 or more words that have the same length and have been identified as the largest words within the file, the application will return the FIRST word identified as the longest word in the file. 
* In case the user wants to run this coding challenge in Windows, the steps should be very similar as the ones provided above:
  1) Install Python by following the steps provided on this site: https://www.python.org/downloads/windows/
  2) Install pytest by following the steps provided on this site: https://docs.pytest.org/en/stable/getting-started.html
  3) Download all the files provided in the same directory as instructed in Step 3
  4) Running the coding challenge and the test cases should be very similar following the instructions in Step 5 by using the command prompt terminal for Windows.
	
