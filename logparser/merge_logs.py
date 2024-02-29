import glob
import heapq
import os
import re
from typing import Generator
from dataclasses import dataclass


@dataclass(frozen=True)
class LogRecord:
    """
    immutable log record
    """
    timestamp: float
    line: str

    def __eq__(self, other):
        """
        imp equal operator
        """
        return self.line == other.line

    def __lt__(self, other):
        """
        imp lower than operator
        """
        return self.timestamp < other.timestamp


def parse_ts_log_line(line) -> float:
    """
    parsed the timestamp from the data
    :param line: the entire line from the log file
    :return:  (timestamp, line_data)
    """
    ts_search = re.search(r"<(\d*.\d*)>", line)
    timestamp = float(ts_search.group(1))
    return timestamp


def log_generator(log: str) -> Generator:
    """
    creates a generator of lines from the required file
    :param log: file path of the log
    :return: a generator of the file lines
    """
    with open(log, 'r') as f:
        for line in f:
            timestamp = parse_ts_log_line(line)
            yield LogRecord(timestamp, line)


def merge_logs(*logs, file_out) -> None:
    """
    merge the required log files. use heap as a data structure.
    given M - num of logs
    time complexity: get min(heap) O(logM)
    space complexity: each writing iteration load into the memory only
    the next chunk to process(a few lines only). O(M)

    :param logs: logs to process
    :param file_out: output path which the data should be written into
    :return: None
    """

    generators = [log_generator(log) for log in logs]

    # merged the sorted generators into a merged sorted list of generators!
    merged_generators = heapq.merge(*generators)

    with open(file_out, "w+") as merged_f:
        # load only the next line into memory each iteration
        for min_record in merged_generators:
            merged_f.write(min_record.line)

    print(f"Merged process ended with success. Result in: {file_out}")


if __name__ == '__main__':
    logs_dir = "logs"
    log_files = glob.glob(os.path.join(logs_dir, "*.log"))
    merge_logs(*log_files, file_out="merged_logs_original.log")
