from nonebot import on_command, permission, CommandSession
from .crawler import get_rank


@on_command('rank', aliases=('排名'), only_to_me=False, permission=permission.EVERYBODY)
async def rank(session: CommandSession):
    if session.ctx.get('preprocessed'):
        # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
        ruler = session.get('ruler', prompt='你想查询哪个分区呢？')
        # 获取城市的天气预报
        rank_report = await get_rank(ruler)

        # 向用户发送天气预报
        await session.send(rank_report)


@rank.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['ruler'] = stripped_arg
        return

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
