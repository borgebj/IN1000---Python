
import discord
import os
import time
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

# keeps the token in another file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
client = commands.Bot(command_prefix="]")
client.remove_command("help")


def read_bank():
    with open("bank.txt", "r") as f:
        lines = f.readlines()
        return int(lines[0].strip())

def read_log():
    list = []
    fil = open("log.txt", "r")
    for x in fil:
        list.append(x.strip())
    fil.close()
    return list

# bank-bot
total_cash = read_bank()
bank_log = read_log()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# sends out a help form that shows the users the various commands
@client.command()
@commands.has_role("Cottonlord")
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Help",
        description="These are the current commands for 'CottonBot'"
    )

    embed.add_field(name="Status", value="Shows the current silver in the bank")
    embed.add_field(name="Add '#'", value="Adds '#' amount of silver to the bank.")
    embed.add_field(name="Remove/Subtract/Take '#'", value="Removes '#' amount of silver from the bank")
    embed.add_field(name="Change_total '#'", value="Changes the total value in the bank to new amount")
    embed.add_field(name="log / log clear", value="views the log and recent actions with the bank. Clear to empty the log")
    embed.add_field(name="clear '#'", value="Clears '#' amount of messages from the bot")
    embed.add_field(name="purge '#'", value="Clears '#' amount of messages from all users and bots")
    await ctx.send(embed=embed)


# sends out the current status of the bank
@client.command()
@commands.has_role("Cottonlord")
async def status(ctx):
    await ctx.channel.send(f'The bank currently holds {total_cash} silver.')

# clears #x# amount of messages FROM BOT
@client.command(pass_context=True)
@commands.has_role("Cottonlord")
async def clear(ctx, x):
    messages = await ctx.channel.history(limit=100).flatten()
    messages_removed = 0
    for setning in messages:
        if setning.author.bot and messages_removed < int(x):
            await setning.delete()
            messages_removed += 1
    send = await ctx.channel.send(str(messages_removed)+" messages has been removed.")
    time.sleep(2)
    await send.delete()
    await ctx.channel.purge(limit=1)

# clears #x# amount of messages FROM ALL
@client.command()
@commands.has_role("Cottonlord")
async def purge(ctx, x):
    global time
    await ctx.channel.purge(limit=int(x)+1)
    send = await ctx.channel.send(f'Purged {x} messages.')
    time.sleep(2)
    await send.delete()


# changes the total amount of cash in the bank
@client.command()
@commands.has_role("Cottonlord")
async def change_total(ctx, amount):
    global total_cash
    try:
        amount = int(amount)
        previous = total_cash
        total_cash = amount
        await ctx.channel.send(f'Changed total amount from {previous} to {total_cash}.')
        with open("bank.txt", "w") as f:
            f.write(str(total_cash))
    except TypeError:
        await ctx.channel.send(f'{amount} is invalid.')


# clears both local and stored logs
def clear_log():
    global bank_log

    file = open("log.txt", "r+")
    file.truncate(0)
    file.close()
    bank_log.clear()


# shows an embed with most recent actions with the bank
@client.command("log")
@commands.has_role("Cottonlord")
async def log(ctx, *args):
    global bank_log, time

    replies = ["yes", "yeah", "yy", "y"]
    if len(args) > 0:
        try:
            sent = await ctx.channel.send("Are  you sure you want to clear the log?")
            msg = await client.wait_for("message", check=lambda message: message.author == ctx.author and  message.channel == ctx.channel, timeout=10)
            if msg.content.lower() in replies:
                time.sleep(1)
                await sent.delete()
                await msg.delete()
                clear_log()
                time.sleep(1)
                cleared = await ctx.channel.send("Logs are now cleared.")
                time.sleep(2)
                await cleared.delete()
            else:
                await ctx.channel.send("Will not clear the log.")
        except:
            timed = await ctx.channel.send("You got timed out, logs will not be cleared.")
            await timed.delete()
    else:

        # sender selve loggen
        embed = discord.Embed(
            title="Log",
            description="The 9 most recent actions with the bank",
            color=0xbfbfbf
        )

        if len(bank_log) <= 0:
            await ctx.channel.send("The log is empty.")
        else:
            string = ""
            for x in range(9):
                try:
                    #string += bank_log[x]+"\n"
                    linje = bank_log[x].split()
                    event = linje[0]
                    action = linje[2]+" "+linje[3]+" "+linje[4]+" "+linje[5]+" "+linje[6]+" "+linje[7]+" "+linje[8]
                    time = linje[9]+linje[10]

                    embed.add_field(name=event, value=(action+" "+time))
                except IndexError:
                    break
            await ctx.send(embed=embed)
        return


# command to add cash to bank
@client.command()
@commands.has_role("Cottonlord")
async def add(ctx, amount):
    global total_cash, bank_log
    timestamp = " ("+datetime.now().strftime("%d/%m/%Y, %H:%M:%S")+")"

    # uses try/exception to make sure "amount" is not a String
    try:
        amount = int(amount)
        if amount < 0:
            await ctx.channel.send(f'Sending negative amount is not possible.')
            return
        message = f' User {ctx.author} added {amount} silver to the bank.'
        await ctx.channel.send(message)

        bank_log.append("Added: "+message+timestamp)
        with open("log.txt", "a") as l:
            l.write(str("Added: "+message+timestamp+"\n"))

        # changing the amount
        total_cash += amount

    except TypeError:
        await ctx.channel.send(f'{amount} is invalid.')
        return
    finally:
        with open("bank.txt", "w") as f:
            f.write(str(total_cash))


# command to remove cash from the bank
@client.command(aliases=["remove", "subtract", "take"])
@commands.has_role("Cottonlord")
async def _remove(ctx, amount):
    global total_cash, bank_log
    timestamp = " ("+datetime.now().strftime("%d/%m/%Y, %H:%M:%S")+")"

    try:
        amount = int(amount)
        if amount <= 0:
            await ctx.channel.send(f'Removing {amount} is not possible.')
            return
        message = f'User {ctx.author} took {amount} silver from the bank.'
        await ctx.channel.send(message)

        bank_log.append("Took: "+message+timestamp)
        with open("log.txt", "a") as l:
            l.write(str("Took: "+message+timestamp+"\n"))

        # changing the amount
        total_cash -= amount
        if total_cash < 0: total_cash = 0

    except TypeError:
        await ctx.channel.send(f'{amount} is invalid.')
        return
    finally:
        with open("bank.txt", "w") as f:
            f.write(str(total_cash))

# used for testing
@client.command()
@commands.has_role("Cottonlord")
async def echo(ctx, *args):
    try:
        x = list(args)
        amount = int(args[0])
        x.remove(args[0])
        string = " ".join(x)

        if amount < 10:
            for r in range(amount):
                await ctx.channel.send(string)
        else:
            await ctx.channel.send("You can not echo more than 10")
    except TypeError:
        await ctx.channel.send("Invalid type.")

@client.command()
@commands.has_role("Cottonlord")
async def server(ctx):
    await ctx.channel.send("I dont do that shit, lul.")

# runs the bot
client.run(TOKEN)