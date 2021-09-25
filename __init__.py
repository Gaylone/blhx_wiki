import shutil
import traceback
import urllib.parse
import aiofiles
from hoshino.typing import MessageSegment
from hoshino import Service, priv

import os

from .names import *
from .tools import *
from .AzurlaneAPI import *

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'azurapi_data'))
BACK_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'azurapi_data_bak'))
SAVE_PATH = os.path.dirname(__file__)

sv = Service('blhx_wiki')


def render_forward_msg(msg_list: list, uid=1916714922, name='小加加(VC装甲钢36D版)'):
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
            skin_name = str(args[1]).replace("_", (" "))
            ship_nickname_data = await GetIDByNickname(ship_name)
            if ship_nickname_data == -1 :
                msg = "该昵称下查不到舰船信息，请核对输入，如果想为她新增昵称请发送： blhx备注 正式船名 昵称"
                await bot.send(ev, msg, at_sender=True)
                return
            else:
                ship_id = ship_nickname_data['id']

            flag = await get_ship_skin_by_id(str(ship_id), skin_name)
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
            nickname_list = ''
            ship_name = str(args[0])
            ship_nickname_data = await GetIDByNickname(ship_name)
            ship_nickname_list = await GetAllNickname(ship_nickname_data['id'])
            for string in ship_nickname_list:
                nickname_list+=(str(string)+"\n")

            index = await format_data_into_html(await get_ship_data_by_id(ship_nickname_data['id']))
            await get_ship_weapon_by_ship_name(ship_nickname_data['standred_name'])
            print_img_ship()
            print_img_ship_weapon()
            img_process_ship_info()
            img_process_ship_weapon()
            if index == 0:
                msg = "舰船信息\n" + MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_info.png") \
                      + "\n推荐出装\n" + MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_weapon.png")+ "\n此船备注昵称有：\n"+nickname_list
            else:
                print_img_ship_retrofit()
                img_process_ship_retrofit()
                msg = "舰船信息\n" + MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_info.png") \
                      + "\n此船可改\n" + MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_retrofit.png") \
                      + "\n推荐出装\n" + MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_weapon.png")\
                      + "\n此船备注昵称有：\n"+nickname_list

            msg_list = []
            msg_list.append(msg)
            forward_msg = render_forward_msg(msg_list)
            await bot.send_group_forward_msg(group_id=ev.group_id, messages=forward_msg)
            return
        if len(args) == 0:
            await bot.send(ev, '请在命令之后提供精确舰船名称和皮肤昵称哦~', at_sender=True)
            return
    except Exception as e:
        traceback.print_exc()
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
        await bot.send(ev, '暂无信息', at_sender=True)


@sv.on_fullmatch('blhx 强制更新')
async def force_update(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, '仅限主人做这种事情~', at_sender=True)
        return
    print("命令确认，正在删除")
    try:
        await bot.send(ev, '正在更新，首先请确保网络能访问github的文件中心，否则容易出现翻车风险！', at_sender=True)
        await force_update_offline()
        os.rename(PATH, BACK_PATH)  # 备份源文件省得出意外翻车
        await force_update_offline()  # 再更新
        shutil.rmtree(BACK_PATH)  # 更新完成再删除备份
        version_info = await get_local_version()
        version = str(version_info['version-number'])
        await UpdateName()
        await bot.send(ev, '强制更新完成.强制更新内容仅在离线模式下有效，当前版本V'+version, at_sender=True)
    except:
        # 出问题赶紧回滚
        traceback.print_exc()
        await bot.send(ev, '更新失败！尝试回滚...', at_sender=True)
        try:
            os.rename(BACK_PATH, PATH)
            await bot.send(ev, '回滚成功，差点您就没了。', at_sender=True)
            return
        except:
            await bot.send(ev, '回滚失败，恭喜您翻车了！', at_sender=True)
            return


@sv.on_fullmatch('blhx 最新活动')
async def get_recently_event(bot, ev):
    msg = get_recent_event()
    if msg is None:
        await bot.send(ev, '程序开小差了~', at_sender=True)
    else:
        await bot.send(ev, '详情请看' + str(msg), at_sender=True)

@sv.on_prefix('blhx备注')
async def set_nickname(bot, ev):
    msg = ''
    try:
        args = ev.message.extract_plain_text().split()
        if len(args) == 2:
            origin_name = str(args[0])
            nick_name = str(args[1])

            result = await get_ship_data_by_name(origin_name)

            flag = await AddName(str(result['id']),nick_name)
            if flag != 0:
                msg = "查无此船，请输入正确的舰船名称"
            else:
                msg = '成功为'+origin_name+'添加一个新昵称：'+nick_name
            await bot.send(ev, str(msg), at_sender=True)
        else:
            msg = "参数错误，命令需形如: blhx备注 正式船名 昵称"
            await bot.send(ev, str(msg), at_sender=True)
        return
    except:
        msg = '处理出错，请看日志'
        traceback.print_exc()
        await bot.send(ev,str(msg), at_sender=True)
        return


@sv.on_prefix('blhx移除备注')
async def remove_nickname(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, '仅限主人做这种事情~', at_sender=True)
        return
    msg = ''
    try:
        args = ev.message.extract_plain_text().split()
        if len(args) == 2:
            origin_name = str(args[0])
            nick_name = str(args[1])

            result = await get_ship_data_by_name(origin_name)

            flag = await DelName(str(result['id']), nick_name)

            if flag != 0:
                msg = "此船无此昵称"
            else:
                msg = '成功为'+origin_name+'移除一个昵称：'+nick_name
            await bot.send(ev, str(msg), at_sender=True)
        else:
            msg = "参数错误，命令需形如: blhx移除备注 正式船名 昵称"
            await bot.send(ev, str(msg), at_sender=True)
        return
    except:
        msg = '处理出错，请看日志'
        traceback.print_exc()
        await bot.send(ev,str(msg), at_sender=True)
        return


@sv.on_prefix('blhx皮肤')
async def quick_search_skin(bot, ev):
    try:
        args = ev.message.extract_plain_text().split()
        if len(args) == 2:
            skin_index = int(args[1])
            ship_name = str(args[0])
            ship_nickname_data = await GetIDByNickname(ship_name)
            if ship_nickname_data == -1:
                msg = "该昵称下查不到舰船信息，请核对输入，如果想为她新增昵称请发送： blhx备注 正式船名 昵称"
                await bot.send(ev, msg, at_sender=True)
                return
            else:
                ship_id = ship_nickname_data['id']

            flag = await get_ship_skin_by_id_with_index(str(ship_id), skin_index)
            if flag == -1:
                msg = "她没有这个皮肤！"
                await bot.send(ev, msg, at_sender=True)
                return
            if flag == 0:
                print_img_skin()
                msg = MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_skin_mix/ship_skin.png")
                await bot.send(ev, msg, at_sender=True)
                return
    except:
        msg = '处理出错，请看日志'
        traceback.print_exc()
        await bot.send(ev, str(msg), at_sender=True)
        return