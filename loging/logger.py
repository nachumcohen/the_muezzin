import logging
from datetime import datetime

from connections.elasticsearch_connection import create_elasticsearch


class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name:str = 'logger_files', es_host=create_elasticsearch(),
                   index="logging", level=logging.DEBUG):
            if cls._logger:
                return cls._logger
            logger = logging.getLogger(name)
            logger.setLevel(level)
            if not logger.handlers:
                es = es_host
                class ESHandler(logging.Handler):
                    def emit(self, record):
                        try:
                            es.index(index=index, document={
                                "timestamp": datetime.utcnow().isoformat(),
                                "level": record.levelname,
                                "logger": record.name,
                                "message": record.getMessage(),
                                "funcName": record.funcName
                                })
                        except Exception as e:
                            print(f"ES log failed: {e}")
                logger.addHandler(ESHandler())
                logger.addHandler(logging.StreamHandler())


            cls._logger = logger
            return logger