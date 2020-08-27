import os

from tobrot import DOWNLOAD_LOCATION

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image


async def save_thumb_nail(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOCATION,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴")
    if message.reply_to_message is not None:
        if not os.path.isdir(thumbnail_location):
            os.makedirs(thumbnail_location)
        download_location = thumbnail_location + "/"
        downloaded_file_name = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(downloaded_file_name)
        metadata = extractMetadata(createParser(downloaded_file_name))
        height = 0
        if metadata.has("height"):
            height = metadata.get("height")
        # resize image
        # ref: https://t.me/PyrogramChat/44663
        img = Image.open(downloaded_file_name)
        # https://stackoverflow.com/a/37631799/4723940
        # img.thumbnail((320, 320))
        img.resize((320, height))
        img.save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await ismgs.edit(
            "𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗦𝗮𝘃𝗲𝗱 ...✅" + \
            "𝗧𝗵𝗶𝘀 𝗶𝗺𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝘂𝘀𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝘂𝗽𝗹𝗼𝗮𝗱, 𝗧𝗼 𝗖𝗹𝗲𝗮𝗿 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗨𝘀𝗲 /clearthumbnail."
        )
    else:
        await message.edit("𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 🖼 𝘁𝗼 𝘀𝗮𝘃𝗲 𝗰𝘂𝘀𝘁𝗼𝗺 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹")


async def clear_thumb_nail(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOCATION,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴")
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
    await ismgs.edit("✅ 𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.")
