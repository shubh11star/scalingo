import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5522358046:AAFGyLOEpJFluvzkHe_m6NcrSm19tGty9es")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHwBu2IP6RhEiTWBRpHYp2mvXqe2rDU_t6uvJFKaKItSSZnzUtr4WyH_V8mQRSA91bE-xNK7jEmoGTtCIBhlmL69aSatmZCjtMKbVA8W7Gtj-_w3mPuOQ4s4NO-AZ1980-gHn3LaUxCamlpdQ68f6RrC_MocOZ7efEy6Fh90YWmxqYrKbT-Z7M56VdMb3MWu9Lcsmqizh29xMKtWDotioIlzSGjoxkwHcBsSzRPNAQYhqVdTJY1KkzkJXNSI5RQxPCRFwF4YD04SBl-uv3nnjxH_hJceeQRbY5cQrqYX7spelixMNWhfTvQlM6ypvbNpg3CMhlVKbo5Klka9nRhRSMaShjA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Asdhjklbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5691601913")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
