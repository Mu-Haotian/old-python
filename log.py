import logging

logging.basicConfig(filename='log.log',level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL 
def run_yes():
    logger.debug('debug:Run successfully!')

def run_normal():
    logger.info('info:Start running!')

def Character_Error_my():
    logger.error('Character_Error:Use invalid characters')

def Format_error():
    logger.error('Format_error:The path must contain a drive letter at the beginning')
def log_testing():
    # 此处进行Logging.basicConfig() 设置，后面设置无效

    logger.debug('debug，用来打印一些调试信息，级别最低')
    logger.info('info，用来打印一些正常的操作信息')
    logger.warning('waring，用来用来打印警告信息')
    logger.critical('critical，用来打印一些致命的错误信息，等级最高')
