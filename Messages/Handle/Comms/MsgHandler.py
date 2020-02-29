#  Copyright (c) 2019.

import discord
import requests
import random

twitch_head = {'Client-ID': 'lul'}

from discord.ext import commands

class MsgHandler(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def hello(self, msg):
		# send_message() is not deprecated use send() instead
		# arguments for send(): content=None, *, wait=False, username=None, avatar_url=None, tts=False,
		#                                     file=None, files=None, embed=None, embeds=None

		sender = msg.author
		from_channel = msg.channel

		return await msg.send(f"Hello, @{sender} !")

	@commands.command(pass_context = True)
	async def Twitch(self, msg, *args):
		'''
		: Will only check if broadcaster is live. AB::Twitch -l BroadCasterGoesHere
		arguments/parameter:
		-l -L -live -Live   retrieves if said user is live
		'''
		
		on_msgs = ['Yeah, baby!', 'OMG! OMG! OMG!', 'I hear', 'My mom also loves watching this stream!', 'Ooooh!', 'Pro gamer', 'Grandmaster', 'Bronze', 'Stream \'n chill.', 'You love this streamer? Well, today is your lucky day!', 'The magic 8 ball says that', 'It\'s over social life!', 'Didn\'t knew who they were until they put on the mask.', 'Pray that you are not late to the stream.']
		off_msgs = ['Stream 404.', 'Oh no!', 'Tough luck!', 'We\'ll get \'em next time.', 'I can\'t believe that', 'He/She gone bro', 'Stream unreachable.', 'I find the lack of stream distrubing.', 'How saddening.', 'The magic 8 ball says that', 'Hello darkness, my old friend.', 'I refuse to believe that', 'Damn!' , 'Missed the stream or something because', 'Not my fault that', 'Pray that it\'s at least some technical issues.']

		if args[0].lower() == '-l'.lower() or args[0].lower() == '-live'.lower(): # -l -L -live -Live
			live = self._is_live(args[1])
			if live == 'live'.lower() and args[1] != 'Ninja'.lower():
				return await msg.send(f'{random.choice(on_msgs)} {args[1]} is live! https://www.twitch.tv/{args[1]}')
			elif args[1] != 'Ninja'.lower():
				return await msg.send('I thought ninja\'s didn\'t exist? Oh well, he\'s live.' if live == 'live' else 'Tough luck! He\'s off the grid.')
			else: # Offline
				return await msg.send(f'{random.choice(off_msgs)} {args[1]} is offline. :(')
			# END -l parameters
		else:
			return await msg.send(f'Unknow argument/parameter "{args[0]}". Usage: mh:Twitch -[argument] [UsernameOfBroadcasterHere]')
	
	def _is_live(self, username):
		id = self._get_twitch_id(username) if type(self._get_twitch_id(username)) != type(None) or self._get_twitch_id(username) == f'{username} does not exist' else self._get_twitch_id(username)
		if id:
			response = requests.get(f'https://api.twitch.tv/helix/streams?user_id={id}', headers = twitch_head)
			try:
				if response.json()['error']: return 'Invalid username or user does not exist. Check spelling.'
			except Exception as err:
				print(err)
			# END try except
			
			for types in response.json()['data']:
				return types['type']
	
	def _get_twitch_id(self, username): # Get a Twitch ID from the user
		response = requests.get(f'https://api.twitch.tv/helix/users?login={username}', headers = twitch_head)
		try:
			if response.json()['error']: return 'Invalid username or user does not exist. Check spelling.'
		except Exception as err:
			#print(err, "Couldn't find error in the twitch api lmao")
			op = err # useless
		
		for i in response.json()['data']:
			id = i['id']
			return id if id else f'{username} does not exist'

def setup(client):
	client.add_cog(MsgHandler(client))