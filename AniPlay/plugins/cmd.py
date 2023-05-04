from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.stats import day, over


@app.on_message(filters.command(['start', 'ping', 'help', 'alive']))
async def start(_, message: Message):
    try:
        await message.reply_text('Hello, I am a Bot which you can use to watch anime Online, without any hassle and ofcourse without any ads... \nYou can Search for Animes Using /search or /s\nEg - /search One Piece   or   /s One Piece\n\n You can Join our Main Channel - @allanimesschannel for Direct Anime Files (You will find most of the Animes here)...')
    except:
        return


QUERY = '**Search Results:** `{}`'


@app.on_message(filters.command(['search', 's']))
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = ' '.join(message.command[1:])
        if query == '':
            return await message.reply_text('Write the Anime Name after /search or /s to search ✿✿')
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(QUERY.format(query), reply_markup=button)
    except Exception as e:
        try:
            return await message.reply_text('**Did not find anything related to your search query...**\n\nProbably Incorrect Name, Check the spellings or Try again')
        except:
            return


@app.on_message(filters.command('stats'))
async def stats(_, message: Message):
    try:
        await message.reply_text('Use /stats1 For Day Wise Stats\nAnd /stats2 For Overall Stats')
    except:
        return


@app.on_message(filters.command('stats1'))
async def stats1(_, message: Message):
    try:
        img = day()
        await message.reply_photo(img, caption='**AnimeDex | Day Wise Stats**')
    except:
        return


@app.on_message(filters.command('stats2'))
async def stats2(_, message: Message):
    try:
        img = over()
        await message.reply_photo(img, caption='**AnimeDex | Overall Stats**')
    except:
        return
