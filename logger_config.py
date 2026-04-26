import logging

# Logging සැකසුම් - Emojis සඳහා utf-8 භාවිතා කර ඇත
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs.txt", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Educational_MAS")