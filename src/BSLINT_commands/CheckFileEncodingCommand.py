import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst
import codecs


class CheckFileEncodingCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()

        try:
            # or codecs.open on Python 2
            codecs.open(params["file_path"], encoding=params["source_file_encoding"]).read()
        except:
            return error.get(ErrConst.FILE_ENCODING,
                             [params["source_file_encoding"]])


