from datetime import datetime

def get_timestamp():
    print(datetime.now())
    # 2023-04-30 17:06:45.916869  turn to this -->20230430170645
    # clean info datetime.now
    un_formatted_time = datetime.now()
    formatted_time = un_formatted_time.strftime("%Y%m%d%H%M%S")
    print(formatted_time)
    # 20230430171220

    return formatted_time