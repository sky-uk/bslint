import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst
import codecs


class CheckFileEncodingCommand(object):
    @staticmethod
    def execute(params):

        try:
            codecs.open(params["file_path"], encoding=params["source_file_encoding"]).read()
        except:
            return {"error_key": ErrConst.FILE_ENCODING, "error_params": []}


