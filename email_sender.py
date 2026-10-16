import smtplib
from email.message import EmailMessage
import os
import json


seen_file = "seen_jobs.json"

def send_emails(new_jobs):
    seen_ids = set()
    if os.path.exists(seen_file):
        try:
            with open(seen_file, "r") as file:
                seen_ids = set(json.load(file))
        except Exception:
            seen_ids = set()
    all_jobs = [job for job in new_jobs if job.get("jobId") and job["jobId"] not in seen_ids]
    if len(all_jobs) == 0:
        return False
        
    SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    # cant show my password on GitHub sorry
    msg = EmailMessage()
    word = "Apprenticeships" if len(all_jobs) >1 else "Apprenticeship"
    msg["Subject"] = f"🚀 {len(all_jobs)} new Degree {word} Dropped!"
    msg["From"] = SENDER_EMAIL
    RECEIVER_EMAILS = os.environ.get("RECEIVER_EMAILS")
    msg["To"] = RECEIVER_EMAILS
    
    body = "All the Degree Apprenticeships you haven't applied for yet hurry up and go apply \n \n"
    for job in all_jobs:
        body += f"Company: {job['companyName']}\n"
        body += f"Role: {job['jobTitle']}\n"
        body += f"Link: {job['url']}\n"
        body += "\n" +"-" *40 + "\n"
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email notification sent successfully!")
        
        for job in all_jobs:
            seen_urls.add(job["url"])
        
        with open(seen_file, "w") as file:
            json.dump(list(seen_ids),file, indent = 2) # converts our python data into json for program to read
    except Exception as e:
        print(f"Error sending email: {e}")
