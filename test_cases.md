# Test Cases - Bug Tracker CLI

## TC001 - Add a new bug
**Steps**
1. Run the application
2. Choose option 1
3. Enter bug title
4. Enter bug description
5. Enter bug priority

**Expected Result**
A new bug is added and saved successfully.

---

## TC002 - View all bugs
**Steps**
1. Run the application
2. Choose option 2

**Expected Result**
All saved bugs are displayed with ID, title, status, priority, and date created.

---

## TC003 - Mark bug as fixed
**Steps**
1. Run the application
2. Choose option 3
3. Select a valid bug number

**Expected Result**
The selected bug status changes from Open to Fixed.

---

## TC004 - Handle invalid bug number
**Steps**
1. Run the application
2. Choose option 3
3. Enter a bug number that does not exist

**Expected Result**
The system displays an invalid choice message.

---

## TC005 - View bugs when no bugs exist
**Steps**
1. Delete or clear the bugs.json file
2. Run the application
3. Choose option 2

**Expected Result**
The system displays "No bugs found."