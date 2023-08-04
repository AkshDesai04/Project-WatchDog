# Author: Aksh Desai
# 
# Key Role: Maintain flow of project and datapoints
# 
# 
# 
# Flow of file and its operations (main.py)
#   Check if database exists
#       If database doesn’t exist, create database
#   Check if Config table exists
#       If table doesnt exist, create it with user input
#   Initialize variables such as intervals and preferences from the Config table and save them as variables in the program for easier access
#   Create a thread for each datapoint chosen to be captured in the config file
#   Point each thread to its specific .py file


#################### imports ####################
import threading

import database_operations
import config

import KeyLogging
import ProcessDP
import Screenshot
import Selfie
import LoginActivity
import FaceRec
#################### imports ####################


#################### Database Connection ####################
con = database_operations.create_connection("host", "user", "pass")
mycursor = con.cursor()
#################### Database Connection ####################


#################### Making sure database and onfig table are ready for operations ####################
mycursor.execute(f"SHOW DATABASES LIKE 'ProjectWatchDog'")
database_exists = mycursor.fetchone()

if not database_exists:
    database_operations.create_db(con, "ProjectWatchDog")
    con.database = "ProjectWatchDog"

mycursor.execute(f"SHOW TABLES LIKE 'Config'")
table_exists = mycursor.fetchone()
if not table_exists:
    database_operations.create_table(
        con,
        "Config",
        {
            "screen_capture", 
            "cam_capture",
            "process_log_capture",
            "key_log_capture",
            "login_activity_capture",
            "face_rec"
            "screen_capture_int",
            "cam_capture_int",
            "process_capture_int",
            "face_rec_int"
        },
        {"BOOL", "BOOL", "BOOL", "BOOL", "BOOL", "BOOL", "INT", "INT", "INT", "INT"},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    )

    database_operations.db_insert(con, "Config", config.get_config_properties())
#################### Making sure database and onfig table are ready for operations ####################


#################### Getting Data from Config Table ####################
screen_capture         = database_operations.db_read(con, "SELECT screen_capture         FROM Config")
cam_capture            = database_operations.db_read(con, "SELECT cam_capture            FROM Config")
process_log_capture    = database_operations.db_read(con, "SELECT process_log_capture    FROM Config")
key_log_capture        = database_operations.db_read(con, "SELECT key_log_capture        FROM Config")
login_activity_capture = database_operations.db_read(con, "SELECT login_activity_capture FROM Config")
face_rec               = database_operations.db_read(con, "SELECT face_rec               FROM Config")
screen_capture_int     = database_operations.db_read(con, "SELECT screen_capture_int     FROM Config")
cam_capture_int        = database_operations.db_read(con, "SELECT cam_capture_int        FROM Config")
process_capture_int    = database_operations.db_read(con, "SELECT process_capture_int    FROM Config")
face_rec_int           = database_operations.db_read(con, "SELECT face_rec_int           FROM Config")
#################### Getting Data from Config Table ####################


#################### Creating and starting threads as per Config Table ####################
screen_capture_thread         = threading.Thread(target=Screenshot    .start_data_capture, args=(screen_capture_int,))  if screen_capture         else None
cam_capture_thread            = threading.Thread(target=Selfie        .start_data_capture, args=(cam_capture_int,))     if cam_capture            else None
process_log_capture_thread    = threading.Thread(target=ProcessDP     .start_data_capture, args=(process_capture_int,)) if process_log_capture    else None
key_log_capture_thread        = threading.Thread(target=KeyLogging    .start_data_capture)                              if key_log_capture        else None
login_activity_capture_thread = threading.Thread(target=LoginActivity .start_data_capture)                              if login_activity_capture else None
face_rec_thread               = threading.Thread(target=FaceRec       .start_face_rec, args=(face_rec_int,))     if face_rec               else None

screen_capture_thread         .start()
cam_capture_thread            .start()
process_log_capture_thread    .start()
key_log_capture_thread        .start()
login_activity_capture_thread .start()
face_rec_thread               .start()
#################### Creating and starting threads as per Config Table ####################