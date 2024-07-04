from telethon import TelegramClient
from telethon.tl.types import PeerUser
from telethon import events
import re
from collections import namedtuple
from bestconfig import Config

Match = namedtuple('Match', ['name', 'regex', 'filename'])
config = Config("config.yaml")
api_id = config.API_ID
api_hash = config.API_HASH
session_name = config.session_name
client = TelegramClient(session_name, api_id, api_hash)

matches = []
for match_config in config.matches:
    uploaded_photo = client.upload_file(match_config['filename'])
    matches.append(
        Match(
            name=match_config['name'],
            regex=re.compile(match_config['regex']),
            filename=match_config['filename']
        )
    )

with client:
    @client.on(events.NewMessage())
    async def normal_handler(event):
        msg = event.message
        peer_id = msg.peer_id
        from_id = msg.from_id
        if type(peer_id) is PeerUser and type(from_id) is PeerUser:
            for match in matches:
                if match.regex.match(msg.message):
                    peer_entity = await client.get_entity(peer_id.user_id)
                    await client.send_file(
                        entity=peer_entity,
                        reply_to=msg.id,
                        file=match.filename
                    )
    client.run_until_disconnected()
