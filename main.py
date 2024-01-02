import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = False
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='vouch')
async def vouch(ctx):
    # Check if the command is used in the correct channel
    vouch_channel_id = channelid  # Replace with your channel ID
    if ctx.channel.id != vouch_channel_id:
        await ctx.send(f"This command can only be used in <#{vouch_channel_id}>.")
        return

    # Get the vouch information
    vouch_info = ctx.message.content[len(ctx.prefix) + len(ctx.command.name):].strip()

    # Get the channel where the vouch will be posted
    vouch_channel = bot.get_channel(vouch_channel_id)

    if vouch_channel:
        # Create an embed for the vouch
        embed = discord.Embed(
            title="Vouch Given",
            description=f"+rep <@youruserid> by {ctx.author.mention} for **{vouch_info}**",
            color=0x00FFFF  # You can customize the color here
        )

        # Set the footer with username and avatar
        avatar_url = ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
        embed.set_footer(text=f"Sent by: {ctx.author.name}", icon_url=avatar_url)

        # Post the vouch as an embed in the specified channel
        await vouch_channel.send(embed=embed)

    # Delete the invoking command
    await ctx.message.delete()

# Run the bot with your token
bot.run('token')
