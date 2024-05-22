import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

def main():
    params = BrainFlowInputParams()
    # params.mac_address = '00-55-da-b6-01-db'
    # params.serial_number = '4206-J4P3-01DB' 
    board = BoardShim(BoardIds.MUSE_2_BOARD, params)

    board.prepare_session()
    board.start_stream()

    time.sleep(3)

    data = board.get_board_data()

    print(data.shape)
    board.stop_stream()
    board.release_session()
    

if __name__ == '__main__':
    main()