from telethon import TelegramClient
from telethon.tl.types import PeerUser
from telethon import events
import re
from bestconfig import Config

config = Config("config.yaml")
api_id = config.API_ID
api_hash = config.API_HASH
session_name = config.session_name
client = TelegramClient(session_name, api_id, api_hash)

ahahah_pattern = re.compile(config.ahahah_regex)
archimedes_file = config.archimedes_file
with open(archimedes_file, mode='rb') as f:
    archimedes_bin = f.read()

with client:
    @client.on(events.NewMessage())
    async def normal_handler(event):
        msg = event.message
        peer_id = msg.peer_id
        from_id = msg.from_id
        print()
        if type(peer_id) is PeerUser \
                and type(from_id) is PeerUser \
                and ahahah_pattern.match(msg.message):
            peer_entity = await client.get_entity(peer_id.user_id)
            await client.send_file(entity=peer_entity, reply_to=msg.id, file=archimedes_bin)
    client.run_until_disconnected()
