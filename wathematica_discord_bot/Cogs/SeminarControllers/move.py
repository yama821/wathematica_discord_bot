import config
import discord
import utility_methods as ut
from discord.commands import slash_command
from discord.ext import commands


class Move(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.guild_only()
    @slash_command(
        name="move",
        description=f'ゼミを{config.category_names["pending_seminars"]}から{config.category_names["ongoing_seminars"]}に移動させます',
        guild_ids=config.guilds,
    )
    async def move(self, ctx: discord.ApplicationContext):

        if ctx.channel.category.name != config.category_names["pending_seminars"]:
            embed = discord.Embed(
                title="<:x:960095353577807883> 不正な操作です",
                description=f'{config.category_names["pending_seminars"]}にあるテキストチャンネルでのみ実行可能です。',
                color=discord.Colour.red(),
            )
            await ctx.respond(embed=embed)
            return

        ongoing_seminar_category = await ut.get_category_by_category_name(
            guild=ctx.guild,
            category_name=config.category_names["ongoing_seminars"],
        )
        await ctx.channel.edit(
            category=ongoing_seminar_category, reason=f"Requested by {ctx.author.name}"
        )

        embed = discord.Embed(
            title="<:white_check_mark:960095096563466250> チャンネル移動成功",
            description=f'チャンネルを{config.category_names["ongoing_seminars"]}へ移動しました。',
            color=discord.Colour.brand_green(),
        )
        await ctx.respond(embed=embed)


def setup(bot: discord.Bot):
    bot.add_cog(Move(bot))
