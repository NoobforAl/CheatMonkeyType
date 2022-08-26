from install_chromium import (
    _downloadFile,
    _unzipFile,
)

import unittest

# this link choose from https://filesamples.com/formats/txt
URL_TEMP_FILE = "https://filesamples.com/samples/document/txt/sample2.txt"


class DownloadFile(unittest.TestCase):
    """
    Test case install chrome, 
        download file and check extract files!
    """

    def testDownload(self) -> None:
        """Test download file if ok return True"""
        self.assertTrue(_downloadFile(URL_TEMP_FILE, "./temp/a.txt"))

    def testExtractFile(self) -> None:
        # ! Note: this test needed temp file!
        # self.assertTrue(_unzipFile("./temp/temp.zip"))
        # self.assertTrue(_unzipFile("./temp/temp.tar.xz"))
        pass

# ? add more test if needed ;)


if __name__ == "__name__":
    unittest.main()