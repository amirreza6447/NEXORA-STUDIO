from PIL import Image, ImageDraw, ImageFont
import aiohttp
from io import BytesIO


BACKGROUND = "assets/rank_bg.png"


def get_font(size):
    try:
        return ImageFont.truetype(
            "arial.ttf",
            size
        )
    except:
        return ImageFont.load_default()



def circle_avatar(img, size):

    img = img.resize(
        (size,size)
    )

    mask = Image.new(
        "L",
        (size,size),
        0
    )

    d = ImageDraw.Draw(mask)

    d.ellipse(
        (0,0,size,size),
        fill=255
    )


    result = Image.new(
        "RGBA",
        (size,size)
    )

    result.paste(
        img,
        (0,0),
        mask
    )

    return result



async def create_rank_card(
    user,
    level,
    xp,
    next_xp,
    nex,
    rank
):

    img = Image.open(
        BACKGROUND
    ).convert("RGBA")


    draw = ImageDraw.Draw(img)



    # avatar

    async with aiohttp.ClientSession() as session:

        async with session.get(
            str(user.display_avatar.url)
        ) as r:

            data = await r.read()


    avatar = Image.open(
        BytesIO(data)
    ).convert("RGBA")


    avatar = circle_avatar(
        avatar,
        300
    )


    img.paste(
        avatar,
        (120,300),
        avatar
    )



    # fonts

    name_font = get_font(70)
    rank_font = get_font(45)
    info_font = get_font(42)



    # name

    draw.text(
        (520,300),
        user.name,
        font=name_font,
        fill="white"
    )



    # rank

    draw.text(
        (520,430),
        rank,
        font=rank_font,
        fill=(190,120,255)
    )



    # level

    draw.text(
        (1210,300),
        str(level),
        font=info_font,
        fill="white"
    )



    # xp

    draw.text(
        (1170,440),
        f"{xp}/{next_xp}",
        font=info_font,
        fill="white"
    )



    # nex

    draw.text(
        (1190,580),
        str(nex),
        font=info_font,
        fill=(255,210,50)
    )



    # progress

    bar_x = 220
    bar_y = 735

    width = 900
    height = 35


    progress = xp / next_xp

    if progress > 1:
        progress = 1



    draw.rounded_rectangle(
        (
            bar_x,
            bar_y,
            bar_x+width,
            bar_y+height
        ),
        radius=20,
        fill=(35,20,60)
    )


    draw.rounded_rectangle(
        (
            bar_x,
            bar_y,
            bar_x+int(width*progress),
            bar_y+height
        ),
        radius=20,
        fill=(150,50,255)
    )



    output = BytesIO()

    img.save(
        output,
        "PNG"
    )

    output.seek(0)

    return output