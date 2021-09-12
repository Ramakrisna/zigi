# Zigi's Calender Availability

***

## The goal of this project is to get a list of people, and the meetings each of them has, and return a list of available times they can all meet.

***

### I've decided to take some assumptions when addressing this task:
### 1. The data received is formatted correctly.
### 2. The time and dates of the data received are all UTC
### 3. Meetings don't end after midnight
### 4. If one person has a meeting (or several) on a certain date, but no one else, that day is open for scheduling meetings

***

**Other than that, I didn't implement a mechanism to import the data, if need be, I can, but since we didn't discuss this, I've decided not to create one in case it isn't necessary.**

***

In order to check the project, the steps needed are:
1. Change the 'sample_data' in 'main.py'
2. Run 'main.py'