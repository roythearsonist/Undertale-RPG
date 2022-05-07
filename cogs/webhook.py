import time

import topgg
from disnake.ext import commands
from utility.utils import bcolors


class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.topggpy = topgg.WebhookManager(bot).dbl_webhook("/dblwebhook", "dady2005")
        bot.topggpy.run(55111)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        vote_data = data
        voter = await self.bot.fetch_user(vote_data["user"])
        info = await self.bot.players.find_one({"_id": voter.id})
        if info is None:
            print(f"{bcolors.WARNING} This user is not registered.{bcolors.ENDC}")
            return
        info["gold"] = info["gold"] + 500
        info["standard crate"] += 1
        info["last_voted"] = time.time()
        await self.bot.players.update_one({"_id": voter.id}, {"$set": info})
        print(f"{bcolors.GREEN}Received a vote from {str(voter)}, They got their rewards successfully{bcolors.ENDC}")

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        vote_data = data
        voter = await self.bot.fetch_user(vote_data["user"])
        info = await self.bot.players.find_one({"_id": voter.id})
        info["gold"] = info["gold"] + 500
        info["standard crate"] += 1
        await self.bot.players.update_one({"_id": voter.id}, {"$set": info})
        print(f"{bcolors.GREEN}Received a vote from {str(voter)}, They got their rewards successfully{bcolors.ENDC}")

def setup(bot):
    bot.add_cog(TopGG(bot))