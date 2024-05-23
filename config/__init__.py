import os

class Config:
    API_ID = int( os.getenv("api_id","24339011") )
    API_HASH = os.getenv("api_hash","a85d1d917af0d4d02811a9a007b8dcda")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1002193727359") )
    CHANNEL_USERNAME = os.getenv("channel_username","MergelogItachi")
    TOKEN = os.getenv("token","6990344734:AAHbfsLefdj-7I2TW6A10XWYfGkUVV89IWo")
    DOMAIN  = os.getenv("domain","https://itachixstream-1b0460f7986a.herokuapp.com/")
