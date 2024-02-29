import glob
import os
import unittest

from logparser.merge_logs import parse_ts_log_line, LogRecord, merge_logs


def append_data(data, file_handler) -> None:
    """
    append all rows of a file into 'data' object
    :param data: the result object
    :param file_handler: the hanlder to the current file
    :return:
    """
    for line in file_handler:
        timestamp = parse_ts_log_line(line)
        data.append(LogRecord(timestamp, line))


def get_all_data(logs_dir) -> [LogRecord]:
    """
    merged the entire data from logs one by one (read all)
    :param logs_dir: the directory of the sorted logs
    :return: list of LogRecord
    """
    all_files = glob.glob(os.path.join(logs_dir, "*.log"))

    data = []

    for filename in all_files:
        with open(filename, 'r') as f:
            append_data(data, f)

    return data


def get_merged_data(file_out: str) -> [LogRecord]:
    """
    get the data from the merged.log file
    :param file_out: output path for the result
    :return:
    """
    data = []
    with open(file_out, 'r') as f:
        append_data(data, f)
    return data


class TestLogMerger(unittest.TestCase):

    def test_original_input(self):
        """
        Test the original data of the exercise
        :return: None
        """

        logs_dir = "logs"
        file_out = f"{logs_dir}/result/result_merged.log"
        log_files = glob.glob(os.path.join(logs_dir, "*.log"))
        merge_logs(*log_files, file_out=file_out)
        data_from_multiple_logs = get_all_data(logs_dir)
        data_from_multiple_logs.sort()
        data_from_merged_log = get_merged_data(file_out)
        self.assertEqual(data_from_merged_log, data_from_multiple_logs)


if __name__ == '__main__':
    unittest.main()
