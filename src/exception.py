import sys

def error_message_detail(error,error_detail:sys):
    _,_,error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code_filename
    error_messages="Error occured in cript name [{0}] line number[{1}] error name[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

        return error_messages


    )

    class CustomException(Exception):
        def __init__(self,error_messages,error_detail:sys):
            super.__init__(error_messages)
            self.error_messages=error_message_detail(error_messages,error_detail=error_detail)

        
        def __str__(self):
            return self.error_messages


     

