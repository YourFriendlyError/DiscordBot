#  Copyright (c) 2019.

import discord

from discord.ext import commands

class CmdHandler(commands.Cog):
	def __init__(self, client):
		self.client = client

	async def helpf(self):
		return await self.client.send("fffffffff")

def setup(client):
	client.add_cog(CmdHandler(client))

