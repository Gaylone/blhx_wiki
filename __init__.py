import traceback

from hoshino.typing import MessageSegment
from hoshino import Service, priv

import os
from .tools import *
from .AzurlaneAPI import *

SAVE_PATH = os.path.dirname(__file__)

sv = Service('blhx_wiki')


def render_forward_msg(msg_list: list, uid=10007, name='马化腾'):
    forward_msg = []
    for msg in msg_list:
        forward_msg.append({
            "type": "node",
            "data": {
                "name": str(name),
                "uin": str(uid),
                "content": msg
            }
        })
    return forward_msg


@sv.on_prefix('blhx')
async def send_ship_skin_or_info(bot, ev):
    try:
        args = ev.message.extract_plain_text().split()
        if len(args) == 2:
            ship_name = str(args[0])
            skin_name = str(args[1]).replace("_",(" "))
            flag = get_ship_skin_by_name(ship_name, skin_name)
            if flag == 4:
                msg = "她没有这个皮肤！"
                await bot.send(ev, msg, at_sender=True)
                return
            if flag == 0:
                print_img_skin()
                msg = MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_skin_mix/ship_skin.png")
                await bot.send(ev, msg, at_sender=True)
                return
            if flag == 1:
                msg = "她只有原皮！"
                await bot.send(ev, msg, at_sender=True)
                return
        if len(args) == 1:
            ship_name = str(args[0])
            format_data_into_html(get_ship_data_by_name(ship_name))
            get_ship_weapon_by_ship_name(ship_name)
            print_img_ship()
            print_img_ship_weapon()
            img_process_ship_info()
            img_process_ship_weapon()
            msg = "舰船信息\n"+MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_info.png")\
                  +"推荐出装\n"+MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_weapon.png")
            msg_list = []
            msg_list.append(msg)
            forward_msg = render_forward_msg(msg_list)
            await bot.send_group_forward_msg(group_id=ev.group_id, messages=forward_msg)
            return
        if len(args) == 0:
            await bot.send(ev, '请在命令之后提供精确舰船名称和皮肤昵称哦~', at_sender=True)
            return
    except Exception as e:
        print(e)
        await bot.send(ev, "查询出错", at_sender=True)
        return


@sv.on_fullmatch('blhx 过场')
async def send_random_gallery(bot, ev):
    msg = MessageSegment.image("file:///" + SAVE_PATH + "/ship_html/images/gallery/" + get_random_gallery())
    await bot.send(ev, msg, at_sender=True)


@sv.on_fullmatch('blhx 帮助')
async def send_random_gallery(bot, ev):
    msg = "1.查询舰船信息命令：”blhx 无需和谐的中文船名“\n" \
          "2.查询舰船皮肤命令：”blhx 无需和谐的中文船名 皮肤名“ 皮肤名为”原皮”则查询原皮，为“婚纱”则查询婚纱，如果皮肤名有空格则用_替代\n" \
          "3.查询加载时的过场动画：“blhx 过场”" \
          "4.查询强度榜：“blhx 强度榜”"
    await bot.send(ev, msg, at_sender=True)


@sv.on_fullmatch('blhx 强度榜')
async def send_pve_recommendation(bot, ev):
    div_list = get_pve_recommendation()
    div_text = ["强度标准\n", "强度榜\n", "冷无缺榜\n", "强度副榜\n", "联动强度榜\n", "科研船过度阶段强度\n"]
    msg = "仅代表个人观点，完全不等于绝对客观，可能存在各种主观评判或者真爱加成，不过目标是努力去进行符合环境需求的客观评定\n"
    msg_list = []
    if len(div_list) != 0:
        for i in range(0, len(div_list)):
            msg += (div_text[i] + MessageSegment.image(file=str(div_list[i].find('img')['src'])) + "\n")
        msg_list.append(msg)
        forward_msg = render_forward_msg(msg_list)
        await bot.send_group_forward_msg(group_id=ev.group_id, messages=forward_msg)
    else:
        await bot.send(ev, '暂无信息')
