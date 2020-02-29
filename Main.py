
import discord
import os

from discord.ext import commands
from colorama import Fore


client = commands.Bot(command_prefix='mh:'.lower())

@client.event
async def on_ready():
	print(Fore.GREEN + "Successful login" + Fore.WHITE)
	return 'successful'


extensions = ['MsgHandler']
cmd_extn = ['CmdHandler', 'YouTube']

# TODO: Twitch live status of broadcaster •
# TODO: YouTube return random video •
# TODO: Something else I cannot think of right now

if __name__ == '__main__':

	print("Loading message handler extensions")
	sucess = 0
	failed = 0

	for msg_ext in extensions:
		print(f"loading {msg_ext}")
		try:
			client.load_extension('Messages.Handle.Comms.' + msg_ext)
			print(Fore.GREEN + f"Successfully loaded {msg_ext}!" + Fore.WHITE)
			sucess =+ 1
		except Exception as err:
			print(Fore.RED + '-'*150 + f"\n'{msg_ext}' was not able to load: {err}\n" + "-"*150 + Fore.WHITE)
			failed += 1

	print("Loading admin command messages")

	for cmd in cmd_extn:
		print(f"loading cmd file {cmd}")
		try:
			client.load_extension('Messages.Handle.Commands.' + cmd)
			print(Fore.GREEN + f"Successfully loaded {cmd}!" + Fore.WHITE)
			sucess += 1
		except Exception as err:
			print(Fore.RED + '-'*150 + f"\n'{cmd}' was not able to load: {err}\n" + "-"*150 + Fore.WHITE)
			failed += 1

	print(Fore.GREEN + f'{sucess} extensions loaded success fully. ' + Fore.RED + f'{failed} failed to load.')

	client.run('No looky')

