"""用户命令处理器"""
import logging
from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_USER_ID
from database import Database
from utils.checks import reject_group_command
from utils.messages import (
    DEFAULT_LANG,
    LANG_NAMES,
    get_welcome_message,
    get_about_message,
    get_help_message,
    get_insufficient_balance_message,
    get_verify_usage_message,
    normalize_lang,
    t,
)

logger = logging.getLogger(__name__)


def _get_lang(db: Database, user_id: int) -> str:
    if db.user_exists(user_id):
        return db.get_user_language(user_id)
    return DEFAULT_LANG


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /start 命令"""
    if await reject_group_command(update):
        return

    user = update.effective_user
    user_id = user.id
    username = user.username or ""
    full_name = user.full_name or ""

    # 已初始化直接返回
    if db.user_exists(user_id):
        lang = _get_lang(db, user_id)
        await update.message.reply_text(
            t(lang, "start_already", name=full_name)
        )
        return

    # 邀请参与
    invited_by: Optional[int] = None
    if context.args:
        try:
            invited_by = int(context.args[0])
            if not db.user_exists(invited_by):
                invited_by = None
        except Exception:
            invited_by = None

    # 创建用户
    lang = DEFAULT_LANG
    if db.create_user(user_id, username, full_name, invited_by, language=lang):
        welcome_msg = get_welcome_message(full_name, bool(invited_by), lang=lang)
        await update.message.reply_text(welcome_msg)
    else:
        await update.message.reply_text(t(lang, "register_failed"))


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /about 命令"""
    if await reject_group_command(update):
        return

    lang = _get_lang(db, update.effective_user.id)
    await update.message.reply_text(get_about_message(lang=lang))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /help 命令"""
    if await reject_group_command(update):
        return

    user_id = update.effective_user.id
    is_admin = user_id == ADMIN_USER_ID
    lang = _get_lang(db, user_id)
    await update.message.reply_text(get_help_message(is_admin, lang=lang))


async def balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /balance 命令"""
    if await reject_group_command(update):
        return

    user_id = update.effective_user.id
    lang = _get_lang(db, user_id)

    if db.is_user_blocked(user_id):
        await update.message.reply_text(t(lang, "blocked"))
        return

    user = db.get_user(user_id)
    if not user:
        await update.message.reply_text(t(lang, "not_registered"))
        return

    await update.message.reply_text(
        t(lang, "balance_info", balance=user["balance"])
    )


async def checkin_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /qd 签到命令 - 临时禁用"""
    user_id = update.effective_user.id

    # 临时禁用签到功能（修复bug中）
    # await update.message.reply_text(
    #     "⚠️ 签到功能临时维护中\n\n"
    #     "由于发现bug，签到功能暂时关闭，正在修复。\n"
    #     "预计很快恢复，给您带来不便敬请谅解。\n\n"
    #     "💡 您可以通过以下方式获取积分：\n"
    #     "• 邀请好友 /invite（+2积分）\n"
    #     "• 使用卡密 /use <卡密>"
    # )
    # return
    
    # ===== 以下代码已禁用 =====
    lang = _get_lang(db, user_id)
    if db.is_user_blocked(user_id):
        await update.message.reply_text(t(lang, "blocked"))
        return

    if not db.user_exists(user_id):
        await update.message.reply_text(t(lang, "not_registered"))
        return

    # 第1层检查：在命令处理器层面检查
    if not db.can_checkin(user_id):
        await update.message.reply_text(t(lang, "checkin_already"))
        return

    # 第2层检查：在数据库层面执行（SQL原子操作）
    if db.checkin(user_id):
        user = db.get_user(user_id)
        await update.message.reply_text(
            t(lang, "checkin_success", balance=user["balance"])
        )
    else:
        # 如果数据库层面返回False，说明今天已签到（双重保险）
        await update.message.reply_text(t(lang, "checkin_already"))


async def invite_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /invite 邀请命令"""
    if await reject_group_command(update):
        return

    user_id = update.effective_user.id
    lang = _get_lang(db, user_id)

    if db.is_user_blocked(user_id):
        await update.message.reply_text(t(lang, "blocked"))
        return

    if not db.user_exists(user_id):
        await update.message.reply_text(t(lang, "not_registered"))
        return

    bot_username = context.bot.username
    invite_link = f"https://t.me/{bot_username}?start={user_id}"

    await update.message.reply_text(
        t(lang, "invite_link", link=invite_link)
    )


async def use_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /use 命令 - 使用卡密"""
    if await reject_group_command(update):
        return


async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE, db: Database):
    """处理 /lang 设置语言"""
    user_id = update.effective_user.id
    current_lang = _get_lang(db, user_id)

    if not db.user_exists(user_id):
        await update.message.reply_text(t(current_lang, "not_registered"))
        return

    if not context.args:
        await update.message.reply_text(
            t(current_lang, "lang_usage", lang_name=LANG_NAMES.get(current_lang, current_lang))
        )
        return

    new_lang = normalize_lang(context.args[0])
    if new_lang not in LANG_NAMES:
        await update.message.reply_text(
            t(current_lang, "lang_usage", lang_name=LANG_NAMES.get(current_lang, current_lang))
        )
        return

    if db.set_user_language(user_id, new_lang):
        await update.message.reply_text(
            t(new_lang, "lang_updated", lang_name=LANG_NAMES[new_lang])
        )
    else:
        await update.message.reply_text(t(current_lang, "operation_failed"))

    user_id = update.effective_user.id
    lang = _get_lang(db, user_id)

    if db.is_user_blocked(user_id):
        await update.message.reply_text(t(lang, "blocked"))
        return

    if not db.user_exists(user_id):
        await update.message.reply_text(t(lang, "not_registered"))
        return

    if not context.args:
        await update.message.reply_text(t(lang, "use_usage"))
        return

    key_code = context.args[0].strip()
    result = db.use_card_key(key_code, user_id)

    if result is None:
        await update.message.reply_text(t(lang, "card_not_exist"))
    elif result == -1:
        await update.message.reply_text(t(lang, "card_max_use"))
    elif result == -2:
        await update.message.reply_text(t(lang, "card_expired"))
    elif result == -3:
        await update.message.reply_text(t(lang, "card_used"))
    else:
        user = db.get_user(user_id)
        await update.message.reply_text(
            t(lang, "card_success", amount=result, balance=user["balance"])
        )
