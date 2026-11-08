import sqlite3

def db_sync():
    connection = sqlite3.connect("jobs.db", check_same_thread = False)    # sync the connection and the cursor and connect to the jobs database
    connection.commit()
    return connection

def jobs_database(connection):   # creates database if it's not already made
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS jobs(
                jobId INTEGER PRIMARY KEY,
                jobTitle TEXT,
                url TEXT,
                companyName TEXT,
                applied INTEGER DEFAULT 0,
                hidden INTEGER DEFAULT 0,
                location TEXT,
                remove INTEGER DEFAULT 0
                )""")
    connection.commit()

    
def insert_jobs(jobs_dict, connection):
    cursor = connection.cursor()
    for jobs_id, details in jobs_dict.items(): # inserts the job details into the database
        cursor.execute("INSERT OR IGNORE INTO jobs (jobId, jobTitle, url, companyName, location) VALUES(?,?,?,?,?)",(jobs_id,details["jobTitle"], details["url"], details["companyName"], details["location"]))
    connection.commit()

def add_job(job_details, connection):
    title, company, location, url = job_details
    title = title.title()
    company = company.title()
    location = location.title()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO jobs (jobTitle, url, companyName, location) VALUES(?,?,?,?)", (title, url, company, location))
    connection.commit()
    

def get_jobs(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE hidden = 0 ORDER BY applied ASC")
    job = cursor.fetchall()
    connection.commit()
    return job

def get_removed_jobs(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE hidden = 1 and remove = 0 ORDER BY applied ASC ")
    removed_jobs = cursor.fetchall()
    connection.commit()
    return removed_jobs

def delete_job(jobId, connection):
    cursor = connection.cursor()
    cursor.execute("UPDATE jobs SET remove = 1 WHERE jobId = ?", (jobId,))
    connection.commit()
    return 200

def update_job(jobId, type, value, connection):
    cursor = connection.cursor()
    query = f"UPDATE jobs SET {type} = ? WHERE jobId = ?"
    cursor.execute(query, (value, jobId))
    connection.commit()