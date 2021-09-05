# SecureworksDellCodingChallenge
QA Automation Engineer Coding Challenge

**1) INTRODUCTION**

**2) TECHNOLOGY AND OTHER TOOLS**

**3) DETAILS ON TECHNOLOGY USED FOR THIS APPLICATION**

**4) RECOMMENDATIONS**

**5) HOW TO RUN AND COMPILE JAVA CLASS AND TEST CLASS**

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

**3) DETAILS ON TECHNOLOGY USED FOR THIS APPLICATION**

This is a list of tools that a user needs to run the test cases on the machine. It also provides where to find them and how to check if they have been installed on your machine.
1. Python 3 

Note: In case the user does not have Python installed please follow the steps provided on this site to download and install: 
https://docs.python-guide.org/starting/install3/osx/

Note: To check if Python has been installed, please run this command.
If  it's installed, the user will see a similar output to this:

	$ python3 --version 
	
The user should see a similar output like this:
	
	$ Python 3.9.5 (User might have a different version, as long as it is Python 3 the coding challenge should work) 

2. pytest testing framework

Note: In case the user do not have the pytest testing framework installed please follow the steps provided on this site to download and install: 
https://docs.pytest.org/en/stable/getting-started.html

Note: To check if Python has been installed, please run this command.
If  it's installed, the user will see a similar output to this:

	$ pytest --version 
	
The user should see a similar output like this:
	
	$ pytest 6.2.4 (User might have a different version) 

3. MacOS terminal
Note: This coding challenge was created using a macOS environment. This provides simplicity to the coding challenge since the user can run the coding challenge and its test cases from the terminal. No need for an IDE or any other platform (e.g. Visual Studio Code). 

NOTE: If the user has experience using Python and pytest, the user can find different ways to install this technology. 
For example, pytest can be easily installed by running this command "pip install pytest" in the command line. 
Please keep in mind that these details were created to provide the most basic recommendations to install the required technology.

=====================================================

**4) RECOMMENDATIONS**

For simplicity purposes, the coding challenge and its test cases have been designed to be run by having all the files in the same folder. Therefore, please extract files from git repository and store them in a single folder.
For example, if the user wishes to extract the files in the Desktop, the user should see something like this once this is done:

/Users/<user_name>/Desktop/<folder_created_by_user>/LongestWordsInEnglish.txt
	
/Users/<user_name>/Desktop/<folder_created_by_user>/Transpose.py
	
/Users/<user_name>/Desktop/<folder_created_by_user>/test_transpose.py
	
=====================================================

**5) HOW TO RUN THE CODING CHALLENGE AND TEST CASES**

Note: Make sure that before running any of these commands you are located in the terminal inside the folder where all the files from Step 4 were stored.

Once the user has verified that Python and pytest have been installed on the machine, please follow these steps:
1. Run the Coding Challenge by running this command in the command line:
	
	``$python3 Transpose.py``
	
3. Once the application has been verified that it's providing the correct result, run the test cases by running this command in the command line:
	
	``$pytest test_transpose.py``
	
NOTE: For simplicity purposes, I did not use any tool or framework other than those that were essential to create and run the test cases. Unfortunately, for this reason we cannot create Test Reports as we usually do when we have a complete environment setup correctly. In prior experiences when working with different languages and testing frameworks, I have been able to generate different type of reports, such as Pytest HMTL Test Reports or XML reports for Jenkins. 

=====================================================
	
**6) ASSUMPTIONS IN GENERAL**

* User is running the coding challenge and the test cases in a MacOS environment.
* User has placed the files inside the same folder created by the user.
* test (i.e. LongestWordsInEnglish.txt) Text File exists inside the same folder as the other files created by the user.

=====================================================

**7) ASSUMPTIONS ABOUT CODING CHALLENGE**

* Text file will be called Words.txt. If the user wants to use her/his own file, as long as it rename the file to Words.txt, the application should read it.
* There is one specific test case that checks the size of the file. Since the requirements do not specify the size, the assumption is that the file is no bigger than 1 gigabyte.
* There is one specific test case that checks the extension of the file. Since the requirements do not specify the file extension, the assumption is that the file will be a simple text file.
* There is one specific test case which checks specifically for the string returned to only have letters and/or numbers. Since the requirements did not specify what type of characters the text file should have, there is an assumption done that the file would only have alphanumeric characters.
* If there are 2 or more words that have the same length and have been identified as the largest words within the file, the application will return the FIRST word identified as the longest word in the file. 
* In case the user wants to run this coding challenge in Windows, the steps should be very similar as the ones provided above:
  1) Install Python by following the steps provided on this site: https://www.python.org/downloads/windows/
  2) Install pytest by following the steps provided on this site: https://docs.pytest.org/en/stable/getting-started.html
  3) Download all the files provided in the same directory as instructed in Step 4
  4) Running the coding challenge and the test cases should be very similar using the same commands as provided in Step 5, the only difference would using the command prompt terminal for Windows.
