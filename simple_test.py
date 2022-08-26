from install_chromium import (
    _downloadFile,
    # _unzipFile,
)

import unittest

# this link choose from https://filesamples.com/formats/txt
URL_TEMP_FILE = "https://filesamples.com/samples/document/txt/sample2.txt"


class TestDownloadFile(unittest.TestCase):
    """
    Test case install chrome,   
        download file and check extract files!  
    """

    def test_Download(self) -> None:
        """Test download file if ok return True  """
        #self.assertTrue(_downloadFile(URL_TEMP_FILE, "./test.txt"))
        pass

    """ def testExtractFile(self) -> None:  
        # ! Note: this test needed temp file!  
        # self.assertTrue(_unzipFile("./temp/temp.zip"))  
        # self.assertTrue(_unzipFile("./temp/temp.tar.xz"))  
        pass """

# ? add more test if needed ;)


_downloadFile(URL_TEMP_FILE, "./sample2.txt")
if __name__ == "__name__":
    unittest.main()
