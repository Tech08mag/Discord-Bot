from interactions import Client, Intents, listen, slash_command, SlashContext, Permissions
# from interactions import
import os
import json
import debug

cwd = os.path.realpath(os.path.dirname(__file__))

# Load token and other sensible data from credentials file to start bot
with open(cwd + "/credentials.json") as fo:
    credentials = json.load(fo)

# create bot instance
bot = Client(intents=Intents.ALL)


@listen()
async def on_ready():
    debug.info("Dein Bot wurde gestartet")

@slash_command(
        name="test_command",
        description="Teste, ob dein Bot antwortet",
        default_member_permissions=Permissions.SEND_MESSAGES,
        scopes=credentials["scopes"],
        options=[]
)

async def test_command(ctx: SlashContext):
    await ctx.send("Test")


bot.start(credentials["token"])