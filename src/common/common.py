DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class Common:
    @staticmethod
    def change_status_code(status_code):
        res_status_code = 200
        # gRPC→HTTP 対応表dict
        dict_status_code = {
            "0": 200,
            "1": 499,
            "2": 500,
            "3": 400,
            "4": 504,
            "5": 404,
            "6": 409,
            "7": 403,
            "8": 429,
            "9": 400,
            "10": 409,
            "11": 400,
            "12": 501,
            "13": 500,
            "14": 503,
            "15": 500,
            "16": 401,
        }
        if status_code in dict_status_code.keys():
            res_status_code = dict_status_code[status_code]

        return res_status_code
