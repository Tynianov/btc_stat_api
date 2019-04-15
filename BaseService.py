from flask import Flask, make_response, Response
from flask_caching import Cache
from ApiCallService import ApiCallService
from datetime import datetime,timedelta
from DataBaseService import DataBaseService

class BaseService:

    def __init__(self):
        self.api_call = ApiCallService()
        self.db_service = DataBaseService()

    def get_mined_blocks(self):
        blocks  = self.api_call.makeApiCall()

        return len(blocks)

    def get_av_time(self):
        blocks = self.api_call.makeApiCall()
        av_time = 0.0

        for i in range(len(blocks) - 1):
            block1_time = datetime.strptime(blocks[i]['time'], '%Y-%m-%d %H:%M:%S').timestamp()
            block2_time = datetime.strptime(blocks[i + 1]['time'], '%Y-%m-%d %H:%M:%S').timestamp()
            av_time += (block1_time - block2_time)

        av_time /= len(blocks)
        av_time /= 60

        return av_time

    def get_tx_count(self):
        blocks = self.api_call.makeApiCall()
        tx_amount = 0

        for i in range(len(blocks) - 1):
            tx_amount += blocks[i]['transaction_count']

        return tx_amount

    def get_fee_count(self):
        blocks = self.api_call.makeApiCall()
        fees_amount = 0

        for i in range(len(blocks) - 1):
            fees_amount += blocks[i]['fee_total']

        return fees_amount

    def get_input_count(self):
        blocks = self.api_call.makeApiCall()
        input_amount = 0

        for i in range(len(blocks) - 1):
            input_amount += blocks[i]['input_count']

        return input_amount

    def get_output_count(self):
        blocks = self.api_call.makeApiCall()
        output_amount = 0

        for i in range(len(blocks) - 1):
            output_amount += blocks[i]['output_count']

        return output_amount
