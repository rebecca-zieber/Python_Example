This is my current Python project that I'm working on in my spare time. The ultimate goal is to query glassdoor.com for jobs given a set of search specifications and to return a CSV file with the desired information for each job listing (job title, company name, desired experience, education requirements, tools/technologies). 

At the moment, I have a simplified version of the project. 

What it can do:
	- Search glassdoor for job title and company name info for jobs listed in the past 24 hours.
	- Append those search results to an existing CSV file or create a new one.

In-progress:
	- Automate website navigation using Selenium to click through each job listing and extract details about experience, education, and tools/technologies from the HTML.
	- Add experience, education, tools/technologies to the CSV file.

What's next: 
	- Add pagination for larger search results.
	- Add custom search parameters to change location/date listed/appointment type/etc.