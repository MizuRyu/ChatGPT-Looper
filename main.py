import os
from dotenv import load_dotenv
from talkingheads import ChatGPTClient

load_dotenv()

chathead = ChatGPTClient(
    headless=False,
    incognito=False,
    verbose=True,
    skip_login=True,
    user_data_dir=os.getenv("USER_DATA_DIR"),
    driver_arguments=["--profile-directory=Profile 3"],
)

response = chathead.interact("こんにちは")
print(response)