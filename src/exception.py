import sys
import logging


def error_message_details(error, error_detail:sys ):
    _,_,exception_traceback = error_detail.exc_info()
    file_name = exception_traceback.tb_frame.f_code.co_filename
    line_num = exception_traceback.tb_lineno
    error_message = f'Error occured in python script name {file_name} line number {line_num} with error message {error}'

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)


    def __str__(self) -> str:
        return self.error_message
    


