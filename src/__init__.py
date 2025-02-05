from loguru import logger

# Remove default handler
logger.remove()

# Add custom handler
logger.add("logs/powercons.log", rotation="20 MB", level="INFO")

# Export logger
__all__ = ["logger"]
