"""Message templates with multilingual support (en/id/zh)."""
from config import CHANNEL_URL, VERIFY_COST, HELP_NOTION_URL

DEFAULT_LANG = "en"
SUPPORTED_LANGS = {"en", "id", "zh"}

LANG_NAMES = {
    "en": "English",
    "id": "Bahasa Indonesia",
    "zh": "中文",
}

TEXTS = {
    "welcome_intro": {
        "en": "🎉 Welcome, {name}!\nYou are registered and received 1 credit.\n",
        "id": "🎉 Selamat datang, {name}!\nAnda terdaftar dan mendapat 1 poin.\n",
        "zh": "🎉 欢迎，{name}！\n您已成功注册，获得 1 积分。\n",
    },
    "welcome_invited_note": {
        "en": "Thanks for joining via invite; the inviter earned 2 credits.\n",
        "id": "Terima kasih bergabung via undangan; pengundang mendapat 2 poin.\n",
        "zh": "感谢通过邀请链接加入，邀请人已获得 2 积分。\n",
    },
    "welcome_footer": {
        "en": (
            "\nThis bot automates SheerID verifications.\n"
            "Quick start:\n"
            "/about - About the bot\n"
            "/balance - Check credits\n"
            "/help - Full command list\n\n"
            "Get more credits:\n"
            "/qd - Daily check-in\n"
            "/invite - Invite friends\n"
            f"Join channel: {CHANNEL_URL}"
        ),
        "id": (
            "\nBot ini mengotomatisasi verifikasi SheerID.\n"
            "Mulai cepat:\n"
            "/about - Tentang bot\n"
            "/balance - Cek poin\n"
            "/help - Daftar perintah lengkap\n\n"
            "Cara tambah poin:\n"
            "/qd - Absen harian\n"
            "/invite - Undang teman\n"
            f"Gabung kanal: {CHANNEL_URL}"
        ),
        "zh": (
            "\n本机器人可自动完成 SheerID 认证。\n"
            "快速开始：\n"
            "/about - 了解机器人功能\n"
            "/balance - 查看积分余额\n"
            "/help - 查看完整命令列表\n\n"
            "获取更多积分：\n"
            "/qd - 每日签到\n"
            "/invite - 邀请好友\n"
            f"加入频道：{CHANNEL_URL}"
        ),
    },
    "about": {
        "en": (
            "🤖 SheerID auto-verification bot\n\n"
            "Features:\n"
            "- Automate SheerID student/teacher verification\n"
            "- Supports Gemini One Pro, ChatGPT Teacher K12, Spotify Student, YouTube Student, Bolt.new Teacher\n"
            "Use /help for command list."
        ),
        "id": (
            "🤖 Bot verifikasi SheerID otomatis\n\n"
            "Fitur:\n"
            "- Otomatisasi verifikasi SheerID student/teacher\n"
            "- Mendukung Gemini One Pro, ChatGPT Teacher K12, Spotify Student, YouTube Student, Bolt.new Teacher\n"
            "Gunakan /help untuk daftar perintah."
        ),
        "zh": (
            "🤖 SheerID 自动认证机器人\n\n"
            "功能:\n"
            "- 自动完成 SheerID 学生/教师认证\n"
            "- 支持 Gemini One Pro、ChatGPT Teacher K12、Spotify Student、YouTube Student、Bolt.new Teacher\n"
            "发送 /help 查看命令列表。"
        ),
    },
    "help_user": {
        "en": (
            "📖 SheerID verification bot - Help\n\n"
            "User commands:\n"
            "/start - Register\n"
            "/about - About bot\n"
            "/balance - Check credits\n"
            "/qd - Daily check-in (+1 credit)\n"
            "/invite - Invite link (+2 per signup)\n"
            "/use <code> - Redeem card code\n"
            f"/verify <link> - Gemini One Pro (-{VERIFY_COST} credit)\n"
            f"/verify2 <link> - ChatGPT Teacher K12 (-{VERIFY_COST} credit)\n"
            f"/verify3 <link> - Spotify Student (-{VERIFY_COST} credit)\n"
            f"/verify4 <link> - Bolt.new Teacher (-{VERIFY_COST} credit)\n"
            f"/verify5 <link> - YouTube Student Premium (-{VERIFY_COST} credit)\n"
            "/getV4Code <verification_id> - Get Bolt.new code\n"
            "/lang <en|id|zh> - Set language\n"
            "/help - Show this help\n"
            f"Verification troubleshooting: {HELP_NOTION_URL}\n"
        ),
        "id": (
            "📖 Bot verifikasi SheerID - Bantuan\n\n"
            "Perintah pengguna:\n"
            "/start - Daftar\n"
            "/about - Tentang bot\n"
            "/balance - Cek poin\n"
            "/qd - Absen harian (+1 poin)\n"
            "/invite - Tautan undangan (+2 per daftar)\n"
            "/use <kode> - Tukar kode kartu\n"
            f"/verify <link> - Gemini One Pro (-{VERIFY_COST} poin)\n"
            f"/verify2 <link> - ChatGPT Teacher K12 (-{VERIFY_COST} poin)\n"
            f"/verify3 <link> - Spotify Student (-{VERIFY_COST} poin)\n"
            f"/verify4 <link> - Bolt.new Teacher (-{VERIFY_COST} poin)\n"
            f"/verify5 <link> - YouTube Student Premium (-{VERIFY_COST} poin)\n"
            "/getV4Code <verification_id> - Ambil kode Bolt.new\n"
            "/lang <en|id|zh> - Atur bahasa\n"
            "/help - Tampilkan bantuan ini\n"
            f"Panduan kendala verifikasi: {HELP_NOTION_URL}\n"
        ),
        "zh": (
            "📖 SheerID 自动认证机器人 - 帮助\n\n"
            "用户命令:\n"
            "/start - 开始使用（注册）\n"
            "/about - 了解机器人功能\n"
            "/balance - 查看积分余额\n"
            "/qd - 每日签到（+1积分）\n"
            "/invite - 生成邀请链接（+2积分/人）\n"
            "/use <卡密> - 使用卡密兑换积分\n"
            f"/verify <链接> - Gemini One Pro 认证（-{VERIFY_COST}积分）\n"
            f"/verify2 <链接> - ChatGPT Teacher K12 认证（-{VERIFY_COST}积分）\n"
            f"/verify3 <链接> - Spotify Student 认证（-{VERIFY_COST}积分）\n"
            f"/verify4 <链接> - Bolt.new Teacher 认证（-{VERIFY_COST}积分）\n"
            f"/verify5 <链接> - YouTube Student Premium 认证（-{VERIFY_COST}积分）\n"
            "/getV4Code <verification_id> - 获取 Bolt.new 认证码\n"
            "/lang <en|id|zh> - 设置语言\n"
            "/help - 查看帮助信息\n"
            f"认证失败查看：{HELP_NOTION_URL}\n"
        ),
    },
    "help_admin": {
        "en": (
            "\nAdmin commands:\n"
            "/addbalance <user_id> <amount> - Add credits\n"
            "/block <user_id> - Block user\n"
            "/white <user_id> - Unblock user\n"
            "/blacklist - View blocked list\n"
            "/genkey <code> <credits> [uses] [days] - Create card code\n"
            "/listkeys - List card codes\n"
            "/broadcast <text> - Broadcast to all users\n"
        ),
        "id": (
            "\nPerintah admin:\n"
            "/addbalance <user_id> <jumlah> - Tambah poin\n"
            "/block <user_id> - Blokir pengguna\n"
            "/white <user_id> - Buka blokir\n"
            "/blacklist - Lihat daftar blokir\n"
            "/genkey <kode> <poin> [pakai] [hari] - Buat kode kartu\n"
            "/listkeys - Daftar kode kartu\n"
            "/broadcast <teks> - Siar ke semua pengguna\n"
        ),
        "zh": (
            "\n管理员命令:\n"
            "/addbalance <用户ID> <积分> - 增加用户积分\n"
            "/block <用户ID> - 拉黑用户\n"
            "/white <用户ID> - 取消拉黑\n"
            "/blacklist - 查看黑名单\n"
            "/genkey <卡密> <积分> [次数] [天数] - 生成卡密\n"
            "/listkeys - 查看卡密列表\n"
            "/broadcast <文本> - 群发通知\n"
        ),
    },
    "insufficient_balance": {
        "en": "Not enough credits! Requires {cost}, current {balance}.\nGet more: /qd, /invite, /use <code>",
        "id": "Poin tidak cukup! Butuh {cost}, sekarang {balance}.\nCara tambah: /qd, /invite, /use <kode>",
        "zh": "积分不足！需要 {cost} 积分，当前 {balance} 积分。\n获取积分：/qd /invite /use <卡密>",
    },
    "verify_usage": {
        "en": "Usage: {command} <SheerID link>\nExample:\n{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx",
        "id": "Cara pakai: {command} <tautan SheerID>\nContoh:\n{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx",
        "zh": "使用方法: {command} <SheerID链接>\n示例:\n{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx",
    },
    "blocked": {
        "en": "You are blocked and cannot use this feature.",
        "id": "Anda diblokir dan tidak bisa memakai fitur ini.",
        "zh": "您已被拉黑，无法使用此功能。",
    },
    "not_registered": {
        "en": "Please use /start to register first.",
        "id": "Silakan gunakan /start untuk mendaftar terlebih dahulu.",
        "zh": "请先使用 /start 注册。",
    },
    "start_already": {
        "en": "Welcome back, {name}!\nYou are already initialized.\nSend /help to view commands.",
        "id": "Selamat datang kembali, {name}!\nAnda sudah terdaftar.\nKirim /help untuk melihat perintah.",
        "zh": "欢迎回来，{name}！\n您已经初始化过了。\n发送 /help 查看可用命令。",
    },
    "register_failed": {
        "en": "Registration failed, please try again later.",
        "id": "Pendaftaran gagal, coba lagi nanti.",
        "zh": "注册失败，请稍后重试。",
    },
    "balance_info": {
        "en": "💰 Credits\n\nCurrent: {balance}",
        "id": "💰 Poin\n\nSaat ini: {balance}",
        "zh": "💰 积分余额\n\n当前积分：{balance} 分",
    },
    "checkin_already": {
        "en": "❌ Already checked in today. Come back tomorrow.",
        "id": "❌ Hari ini sudah absen. Coba lagi besok.",
        "zh": "❌ 今天已经签到过了，明天再来吧。",
    },
    "checkin_success": {
        "en": "✅ Check-in success! +1 credit\nCurrent: {balance}",
        "id": "✅ Absen berhasil! +1 poin\nSaat ini: {balance}",
        "zh": "✅ 签到成功！\n获得积分：+1\n当前积分：{balance} 分",
    },
    "invite_link": {
        "en": "🎁 Your invite link:\n{link}\n\nEarn 2 credits per successful signup.",
        "id": "🎁 Tautan undangan Anda:\n{link}\n\nDapat 2 poin per pendaftar.",
        "zh": "🎁 您的专属邀请链接：\n{link}\n\n每邀请 1 位成功注册，您将获得 2 积分。",
    },
    "use_usage": {
        "en": "Usage: /use <card_code>\nExample: /use examplecode",
        "id": "Cara pakai: /use <kode_kartu>\nContoh: /use contohkode",
        "zh": "使用方法: /use <卡密>\n\n示例: /use wandouyu",
    },
    "card_not_exist": {
        "en": "Card code does not exist.",
        "id": "Kode kartu tidak ada.",
        "zh": "卡密不存在，请检查后重试。",
    },
    "card_max_use": {
        "en": "Card code reached max uses.",
        "id": "Kode kartu sudah mencapai batas penggunaan.",
        "zh": "该卡密已达到使用次数上限。",
    },
    "card_expired": {
        "en": "Card code expired.",
        "id": "Kode kartu kedaluwarsa.",
        "zh": "该卡密已过期。",
    },
    "card_used": {
        "en": "You have already used this card code.",
        "id": "Anda sudah memakai kode kartu ini.",
        "zh": "您已经使用过该卡密。",
    },
    "card_success": {
        "en": "Card redeemed! Credits gained: {amount}\nCurrent: {balance}",
        "id": "Kode berhasil ditukar! Poin diperoleh: {amount}\nSaat ini: {balance}",
        "zh": "卡密使用成功！\n获得积分：{amount}\n当前积分：{balance}",
    },
    "not_admin": {
        "en": "You do not have permission to use this command.",
        "id": "Anda tidak punya izin untuk perintah ini.",
        "zh": "您没有权限使用此命令。",
    },
    "user_not_exist": {
        "en": "User does not exist.",
        "id": "Pengguna tidak ditemukan.",
        "zh": "用户不存在。",
    },
    "operation_failed": {
        "en": "Operation failed, please try again later.",
        "id": "Operasi gagal, coba lagi nanti.",
        "zh": "操作失败，请稍后重试。",
    },
    "addbalance_success": {
        "en": "✅ Added {amount} credits to user {user_id}.\nCurrent: {balance}",
        "id": "✅ Menambah {amount} poin ke pengguna {user_id}.\nSaat ini: {balance}",
        "zh": "✅ 成功为用户 {user_id} 增加 {amount} 积分。\n当前积分：{balance}",
    },
    "block_success": {
        "en": "✅ Blocked user {user_id}.",
        "id": "✅ Pengguna {user_id} diblokir.",
        "zh": "✅ 已拉黑用户 {user_id}。",
    },
    "unblock_success": {
        "en": "✅ Unblocked user {user_id}.",
        "id": "✅ Pengguna {user_id} dibuka blokirnya.",
        "zh": "✅ 已将用户 {user_id} 移出黑名单。",
    },
    "blacklist_empty": {
        "en": "Blacklist is empty.",
        "id": "Daftar blokir kosong.",
        "zh": "黑名单为空。",
    },
    "broadcast_start": {
        "en": "📢 Broadcasting to {total} users...",
        "id": "📢 Menyiarkan ke {total} pengguna...",
        "zh": "📢 开始广播，共 {total} 个用户...",
    },
    "broadcast_done": {
        "en": "✅ Broadcast done!\nSuccess: {success}\nFailed: {failed}",
        "id": "✅ Siaran selesai!\nBerhasil: {success}\nGagal: {failed}",
        "zh": "✅ 广播完成！\n成功：{success}\n失败：{failed}",
    },
    "lang_usage": {
        "en": "Usage: /lang <en|id|zh>\nCurrent language: {lang_name}",
        "id": "Cara pakai: /lang <en|id|zh>\nBahasa saat ini: {lang_name}",
        "zh": "使用方法: /lang <en|id|zh>\n当前语言: {lang_name}",
    },
    "lang_updated": {
        "en": "Language updated to {lang_name}.",
        "id": "Bahasa diubah ke {lang_name}.",
        "zh": "语言已切换为 {lang_name}。",
    },
    "invalid_sheerid_link": {
        "en": "Invalid SheerID link, please check and try again.",
        "id": "Tautan SheerID tidak valid, periksa dan coba lagi.",
        "zh": "无效的 SheerID 链接，请检查后重试。",
    },
    "deduct_fail": {
        "en": "Failed to deduct credits, please try again later.",
        "id": "Gagal mengurangi poin, coba lagi nanti.",
        "zh": "扣除积分失败，请稍后重试。",
    },
    "processing_gemini": {
        "en": (
            "Starting Gemini One Pro verification...\n"
            "Verification ID: {verification_id}\n"
            "Deducted {cost} credit(s)\n\n"
            "Please wait, this may take 1-2 minutes..."
        ),
        "id": (
            "Memulai verifikasi Gemini One Pro...\n"
            "ID verifikasi: {verification_id}\n"
            "Mengurangi {cost} poin\n\n"
            "Harap tunggu 1-2 menit..."
        ),
        "zh": (
            "开始处理 Gemini One Pro 认证...\n"
            "验证ID: {verification_id}\n"
            "已扣除 {cost} 积分\n\n"
            "请稍候，这可能需要 1-2 分钟..."
        ),
    },
    "processing_k12": {
        "en": (
            "Starting ChatGPT Teacher K12 verification...\n"
            "Verification ID: {verification_id}\n"
            "Deducted {cost} credit(s)\n\n"
            "Please wait, this may take 1-2 minutes..."
        ),
        "id": (
            "Memulai verifikasi ChatGPT Teacher K12...\n"
            "ID verifikasi: {verification_id}\n"
            "Mengurangi {cost} poin\n\n"
            "Harap tunggu 1-2 menit..."
        ),
        "zh": (
            "开始处理 ChatGPT Teacher K12 认证...\n"
            "验证ID: {verification_id}\n"
            "已扣除 {cost} 积分\n\n"
            "请稍候，这可能需要 1-2 分钟..."
        ),
    },
    "processing_spotify": {
        "en": (
            "🎵 Starting Spotify Student verification...\n"
            "Deducted {cost} credit(s)\n\n"
            "📝 Generating student info...\n"
            "🎨 Generating student ID PNG...\n"
            "📤 Submitting documents..."
        ),
        "id": (
            "🎵 Memulai verifikasi Spotify Student...\n"
            "Mengurangi {cost} poin\n\n"
            "📝 Membuat data mahasiswa...\n"
            "🎨 Membuat kartu pelajar PNG...\n"
            "📤 Mengunggah dokumen..."
        ),
        "zh": (
            "🎵 开始处理 Spotify Student 认证...\n"
            "已扣除 {cost} 积分\n\n"
            "📝 正在生成学生信息...\n"
            "🎨 正在生成学生证 PNG...\n"
            "📤 正在提交文档..."
        ),
    },
    "processing_bolt": {
        "en": (
            "🚀 Starting Bolt.new Teacher verification...\n"
            "Deducted {cost} credit(s)\n\n"
            "📤 Submitting documents..."
        ),
        "id": (
            "🚀 Memulai verifikasi Bolt.new Teacher...\n"
            "Mengurangi {cost} poin\n\n"
            "📤 Mengunggah dokumen..."
        ),
        "zh": (
            "🚀 开始处理 Bolt.new Teacher 认证...\n"
            "已扣除 {cost} 积分\n\n"
            "📤 正在提交文档..."
        ),
    },
    "processing_youtube": {
        "en": (
            "📺 Starting YouTube Student Premium verification...\n"
            "Deducted {cost} credit(s)\n\n"
            "📝 Generating student info...\n"
            "🎨 Generating student ID PNG...\n"
            "📤 Submitting documents..."
        ),
        "id": (
            "📺 Memulai verifikasi YouTube Student Premium...\n"
            "Mengurangi {cost} poin\n\n"
            "📝 Membuat data mahasiswa...\n"
            "🎨 Membuat kartu pelajar PNG...\n"
            "📤 Mengunggah dokumen..."
        ),
        "zh": (
            "📺 开始处理 YouTube Student Premium 认证...\n"
            "已扣除 {cost} 积分\n\n"
            "📝 正在生成学生信息...\n"
            "🎨 正在生成学生证 PNG...\n"
            "📤 正在提交文档..."
        ),
    },
    "verification_success": {
        "en": "✅ Verification succeeded!",
        "id": "✅ Verifikasi berhasil!",
        "zh": "✅ 认证成功！",
    },
    "verification_pending": {
        "en": "Documents submitted, awaiting review.",
        "id": "Dokumen dikirim, menunggu peninjauan.",
        "zh": "文档已提交，等待人工审核。",
    },
    "verification_redirect": {
        "en": "Redirect link:\n{redirect_url}",
        "id": "Tautan lanjut:\n{redirect_url}",
        "zh": "跳转链接：\n{redirect_url}",
    },
    "verification_failed_refund": {
        "en": "❌ Verification failed: {message}\n\nRefunded {cost} credit(s).",
        "id": "❌ Verifikasi gagal: {message}\n\n{cost} poin dikembalikan.",
        "zh": "❌ 认证失败：{message}\n\n已退回 {cost} 积分",
    },
    "verification_error_refund": {
        "en": "❌ Error during processing: {message}\n\nRefunded {cost} credit(s).",
        "id": "❌ Terjadi kesalahan: {message}\n\n{cost} poin dikembalikan.",
        "zh": "❌ 处理过程中出现错误：{message}\n\n已退回 {cost} 积分",
    },
    "bolt_submit_success": {
        "en": "✅ Documents submitted!\n📋 Verification ID: `{vid}`\n\n🔍 Auto-fetching verification code...\n(wait up to 20s)",
        "id": "✅ Dokumen terkirim!\n📋 ID verifikasi: `{vid}`\n\n🔍 Mengambil kode otomatis...\n(tunggu hingga 20d)",
        "zh": "✅ 文档已提交！\n📋 验证ID: `{vid}`\n\n🔍 正在自动获取认证码...\n（最多等待20秒）",
    },
    "bolt_submit_failed_refund": {
        "en": "❌ Document submission failed: {message}\n\nRefunded {cost} credit(s).",
        "id": "❌ Pengiriman dokumen gagal: {message}\n\n{cost} poin dikembalikan.",
        "zh": "❌ 文档提交失败：{message}\n\n已退回 {cost} 积分",
    },
    "bolt_missing_vid_refund": {
        "en": "❌ Verification ID not received.\n\nRefunded {cost} credit(s).",
        "id": "❌ ID verifikasi tidak didapat.\n\n{cost} poin dikembalikan.",
        "zh": "❌ 未获取到验证ID\n\n已退回 {cost} 积分",
    },
    "bolt_pending_message": {
        "en": (
            "✅ Documents submitted!\n\n"
            "⏳ Verification code not ready yet (may need 1-5 minutes).\n\n"
            "📋 Verification ID: `{vid}`\n\n"
            "💡 Later query with:\n`/getV4Code {vid}`\n\n"
            "Credits already deducted; querying later is free."
        ),
        "id": (
            "✅ Dokumen terkirim!\n\n"
            "⏳ Kode belum tersedia (butuh 1-5 menit).\n\n"
            "📋 ID verifikasi: `{vid}`\n\n"
            "💡 Cek nanti dengan:\n`/getV4Code {vid}`\n\n"
            "Poin sudah dipotong; pengecekan ulang gratis."
        ),
        "zh": (
            "✅ 文档已提交成功！\n\n"
            "⏳ 认证码尚未生成（可能需要1-5分钟审核）\n\n"
            "📋 验证ID: `{vid}`\n\n"
            "💡 请稍后使用以下命令查询:\n"
            "`/getV4Code {vid}`\n\n"
            "注意：积分已消耗，稍后查询无需再付费"
        ),
    },
    "bolt_success_with_code": {
        "en": (
            "🎉 Verification succeeded!\n\n"
            "✅ Documents submitted\n"
            "✅ Approved\n"
            "✅ Code retrieved\n\n"
            "🎁 Code: `{code}`"
        ),
        "id": (
            "🎉 Verifikasi berhasil!\n\n"
            "✅ Dokumen terkirim\n"
            "✅ Disetujui\n"
            "✅ Kode diperoleh\n\n"
            "🎁 Kode: `{code}`"
        ),
        "zh": (
            "🎉 认证成功！\n\n"
            "✅ 文档已提交\n"
            "✅ 审核已通过\n"
            "✅ 认证码已获取\n\n"
            "🎁 认证码: `{code}`"
        ),
    },
    "get_code_querying": {
        "en": "🔍 Querying verification code, please wait...",
        "id": "🔍 Sedang mengambil kode verifikasi, harap tunggu...",
        "zh": "🔍 正在查询认证码，请稍候...",
    },
    "get_code_status_error": {
        "en": "❌ Query failed, status code: {status}\nPlease retry or contact admin.",
        "id": "❌ Gagal mengambil, status: {status}\nSilakan coba lagi atau hubungi admin.",
        "zh": "❌ 查询失败，状态码：{status}\n请稍后重试或联系管理员。",
    },
    "get_code_success": {
        "en": "✅ Verification succeeded!\n🎉 Code: `{code}`",
        "id": "✅ Verifikasi berhasil!\n🎉 Kode: `{code}`",
        "zh": "✅ 认证成功！\n🎉 认证码：`{code}`",
    },
    "get_code_pending": {
        "en": "⏳ Still under review, please try later.\nUsually takes 1-5 minutes.",
        "id": "⏳ Masih ditinjau, coba lagi nanti.\nBiasanya 1-5 menit.",
        "zh": "⏳ 认证仍在审核中，请稍后再试。\n通常需要 1-5 分钟。",
    },
    "get_code_error_state": {
        "en": "❌ Verification failed\nErrors: {errors}",
        "id": "❌ Verifikasi gagal\nKesalahan: {errors}",
        "zh": "❌ 认证失败\n错误信息：{errors}",
    },
    "get_code_unknown": {
        "en": "⚠️ Current status: {status}\nCode not ready, please retry later.",
        "id": "⚠️ Status saat ini: {status}\nKode belum siap, coba lagi nanti.",
        "zh": "⚠️ 当前状态：{status}\n认证码尚未生成，请稍后重试。",
    },
    "get_code_error_generic": {
        "en": "❌ Error during query: {message}\nPlease retry or contact admin.",
        "id": "❌ Terjadi kesalahan saat mengambil: {message}\nSilakan coba lagi atau hubungi admin.",
        "zh": "❌ 查询过程中出现错误：{message}\n请稍后重试或联系管理员。",
    },
}

def normalize_lang(lang: str) -> str:
    if not lang:
        return DEFAULT_LANG
    val = lang.lower()
    if val in SUPPORTED_LANGS:
        return val
    if val.startswith("en"):
        return "en"
    if val.startswith(("id", "in")):
        return "id"
    if val.startswith(("zh", "cn")):
        return "zh"
    return DEFAULT_LANG

def t(lang: str, key: str, **kwargs) -> str:
    lang = normalize_lang(lang)
    template = (
        TEXTS.get(key, {}).get(lang)
        or TEXTS.get(key, {}).get(DEFAULT_LANG)
        or TEXTS.get(key, {}).get("zh")
        or ""
    )
    if not template:
        return key
    return template.format(**kwargs)

def get_welcome_message(full_name: str, invited_by: bool = False, lang: str = DEFAULT_LANG) -> str:
    parts = [t(lang, "welcome_intro", name=full_name)]
    if invited_by:
        parts.append(t(lang, "welcome_invited_note"))
    parts.append(t(lang, "welcome_footer"))
    return "".join(parts)

def get_about_message(lang: str = DEFAULT_LANG) -> str:
    return t(lang, "about")

def get_help_message(is_admin: bool = False, lang: str = DEFAULT_LANG) -> str:
    msg = t(lang, "help_user")
    if is_admin:
        msg += t(lang, "help_admin")
    return msg

def get_insufficient_balance_message(current_balance: int, lang: str = DEFAULT_LANG) -> str:
    return t(lang, "insufficient_balance", cost=VERIFY_COST, balance=current_balance)

def get_verify_usage_message(command: str, service_name: str, lang: str = DEFAULT_LANG) -> str:
    # service_name kept for compatibility; not interpolated to avoid extra translations
    return t(lang, "verify_usage", command=command)
