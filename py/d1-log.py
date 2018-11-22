import logging

# 输出日志 控制台默认输出warning及以上级别的日志
# 等级权重 DEBUG < INFO < WARNING < ERROR < CRITICAL
# logging.debug("this is a debug log")
#
# logging.info("this is a info log")
#
# logging.warning("this is a warning log")
#
# logging.error("this is a error log")
#
# logging.critical("this is a critical log")
#
# logging.log(logging.WARNING, 'tis is a error log from logging.log')
import sys

"""
修改logging默认配置方法 logging.basicConfig(**kwargs)
参数
    filename 指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
    filemode 指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
    format   指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。
    datefmt  指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
    level    指定日志的级别
    stream   指定日志输出目标的stream 如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
    style    Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
    handlers Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。
"""

#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# logging.basicConfig(filename='./log.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

"""
logging 四大组件
    Logger  日志器 提供了应用程序可一直使用的接口
        获取一个日志器 logging.getLogger("name")
        增加一个handler logging.addHandler()
        移除一个handler logging.removeHandler()
        增加一个filter  logging.addFilter()
        移除一个filter  logging.removeHandler()
        
    Handler 处理器 将logger创建的日志记录发送到合适的目的输出
        StreamHandler 将日志消息发送到输出到Stream,如std.out,std.err
        FileHandler   将日志消息发送到磁盘文件，默认文件大小会无限增长
        TimeRotatingFileHandler 将日志消息发送到磁盘文件，并支持日志文件按时间切割
        setLevel 设置处理级别
        setFormatter 设置输出格式
        addFilter 绑定过滤器
        removeFilter 移除过滤器
    Filter  过滤器 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
    Formatter 格式器 决定日志记录的最终输出格式
"""
logger = logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG)

rf_handler = logging.StreamHandler(sys.stderr)
rf_handler.setLevel(logging.DEBUG)
rf_format = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
rf_handler.setFormatter(rf_format)


f_handler = logging.FileHandler('log.log')
f_handler.setLevel(logging.DEBUG)

logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.debug("1fdsfsaf")
logger.debug("2ffdasdsfsaf")
logger.debug("3fdsffasdsaf")
logger.debug("4fdfadssfsaf")
logger.removeHandler(rf_handler)
logger.debug("这一条不会输出到控制台")