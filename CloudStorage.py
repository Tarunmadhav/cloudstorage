import dropbox
import os
class transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,file_from,file_to):
        for root,dirs,files in  os.walk(file_from){
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.relpath(file_to,relative_path)
        }
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    access_token="sl.Arjnq9WfTQa8NZEzrM3ZlbrcOnNzYvL4Juz-nbWEw89aT_wY0uwtHFZiItaYmVsJo3kLmNEt5BuuSOSF8DKgoCcMB_LW3AkhbjIB3jMy62mtybLhF2HC221-xrucZKDJs9NKI18"
    transfer_data=transferdata(access_token)
    file_from=input("Enter the File u Wnat to Transfer:")
    file_to=input("Enter the full path to upload to dropbox u Wnat to Transfer:")
    transfer_data.upload_files(file_from,file_to)
    print("Files has Been Moved Successfully")
main()