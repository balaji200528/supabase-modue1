from supabase import create_client,client

url = "https://uqicdexmfsjonkrfjrua.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVxaWNkZXhtZnNqb25rcmZqcnVhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM3OTg2NTgsImV4cCI6MjA2OTM3NDY1OH0.yRtn8_2nxiTypqj5MAgwFwwmP0ubYAs2KOTZr4H1cNw"

supabase = create_client(url,key)

def add_task(title,description,status):
    data={
        "title":title,
        "description":description,
        "status":status
    }
    response=supabase.table("todolist").insert(data).execute()
    return response

def view_task():
    response=supabase.table("todolist").select("*").execute()
    return response

def updae_task(task_id,new_status):
    response=supabase.table("todolist").update({"status":new_status}).eq("id",task_id).execute()
     



