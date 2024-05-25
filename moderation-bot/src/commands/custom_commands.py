# File: custom_commands.py

# Import necessary packages
import discord
from discord.ext import commands

# Define a class for custom commands
class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Define a command to greet users
    @commands.command(name='hello', help='Responds with a greeting message')
    async def hello(self, ctx):
        await ctx.send('Hello! Welcome to our Discord server.')

    # Define a command to kick a user
    @commands.command(name='kick', help='Kicks a specified user from the server')
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.send(f'{member.mention} has been kicked from the server.')

    # Define a command to ban a user
    @commands.command(name='ban', help='Bans a specified user from the server')
    async def ban(self, ctx, member: discord.Member):
        await member.ban()
        await ctx.send(f'{member.mention} has been banned from the server.')

    # Define a command to clear messages
    @commands.command(name='clear', help='Clears a specified number of messages from the channel')
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} messages cleared.')

# Setup function to add the cog to the bot
def setup(bot):
    bot.add_cog(CustomCommands(bot))