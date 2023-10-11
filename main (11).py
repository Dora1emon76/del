from telethon.sync import TelegramClient, events

# Replace with your actual API credentials
api_id = '27327983'
api_hash = '6055fdf20578072d6bd4db34953496e2'
phone_number = '+919320615740'

client = TelegramClient('my_session', api_id, api_hash)

# Define the admin ID (replace with the actual admin ID)
admin_id = 6236332524

# Define an event handler to delete messages with # in the group
@client.on(events.NewMessage)
async def delete_messages_with_hashtag(event):
    # Check if the message is in the specified group and from an admin
    print(event.chat_id)
    if event.chat_id == -1001234567890 and event.sender_id == admin_id and "#" in event.message.text:
        # Delete the message
        await event.message.delete()

# Start the Telethon client
client.start()

# Run the event loop
client.run_until_disconnected()
      