# 📘 Assignment: Python Automation and File I/O

## 🎯 Objective

Learn how to read and write files in Python and build a simple automation script that processes text, generates a report, and saves logs.

## 📝 Tasks

### 🛠️ Read and Analyze a Text File

#### Description
Read the sample text file and analyze its contents using helper functions.

#### Requirements
Completed program should:

- Open `sample-notes.txt` and read the file contents.
- Count the total number of lines, words, and characters.
- Return a dictionary or tuple with those counts.
- Use a dedicated function for reading the file and a separate function for counting metrics.

### 🛠️ Write a Summary Report

#### Description
Create a clean text report summarizing the file analysis.

#### Requirements
Completed program should:

- Write the analysis results to `report.txt`.
- Include line count, word count, and character count in the report.
- Return the report file path after saving it.

### 🛠️ Append an Automation Log Entry

#### Description
Add a log entry that records the automation action and the results.

#### Requirements
Completed program should:

- Append a new message to `automation-log.txt` without overwriting existing content.
- Include the current date and time in the log entry.
- Log a short summary such as: `Processed sample-notes.txt: 5 lines, 24 words, 132 characters`.
- Use a helper function to append the log entry.
