# Resume Customizer

## Description
The Resume Customizer project simplifies the process of creating personalized resumes tailored to specific job roles. This web application, built using Django, enables users to generate customized resumes by pasting the job link into the input box. The backend compares the user's profile information provided during signup with the job requirements extracted from the link, ensuring the generated resume aligns with the user's skills and experiences.

## Features
- **Job Link Input:** Users paste the job link into the input box to trigger the resume generation process.
- **Tailored Resume Generation:** Based on the job requirements extracted from the provided link, the website generates a personalized resume.
- **User Profile Comparison:** The backend compares the information provided by the user during signup with the job requirements, ensuring the generated resume aligns with the user's skills and experiences.
- **Signup/Login:** Users can create accounts or log in to access saved resumes and preferences.
- **Template Selection:** Users can choose from a variety of resume templates to suit their preferences.
- **Export Options:** Once the resume is generated, users can export it in various formats such as PDF or Word document.

## Technologies Used
- **Framework:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Database:** PostgreSQL (or any other supported by Django)
- **Job Link Parsing:** Web Scraping techniques
- **Authentication:** Django authentication system

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database and configure connection settings in `settings.py`.
4. Run the Django server: `python manage.py runserver`
5. Access the application through your preferred web browser.

## Usage
1. Sign up for an account or log in if you already have one.
2. Copy the job link from the job posting you're interested in.
3. Paste the job link into the provided input box on the website.
4. Select your preferred resume template.
5. Generate the tailored resume.
6. Review and make any necessary edits.
7. Export the resume in your desired format.

## Contributing
Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
