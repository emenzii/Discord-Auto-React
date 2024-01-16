Very simple bot which automatically adds reactions to new messages for set Channel IDs with set emojis.

In order to run:

In *main.py* replace *0* with the Channel ID, as well as it's corresponding emoji beside.

In order to add additional channels and emojis look into the following section of the code:

CHANNEL_EMOJIS = {
  0: '🤑',  # Emoji for Channel 1
  0: '🔥',  # Emoji for Channel 2
}

Add an extra line in the same format as above, see below example:

CHANNEL_EMOJIS = {
  0: '🤑',  # Emoji for Channel 1
  0: '🔥',  # Emoji for Channel 2
  *0: '😂', # Emoji for Channel 3*
}

