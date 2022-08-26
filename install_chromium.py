import platform
import tarfile
import zipfile
import wget
import lzma
import os

OsLIST = {
    "windows": "https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/1039242/chrome-win.zip",
    "darwin": "https://storage.googleapis.com/chromium-browser-snapshots/Mac/1039233/chrome-mac.zip",
    "ubuntu": "https://github.com/macchrome/linchrome/releases/download/v104.0.5112.101-r1012729-portable-ungoogled-Lin64/ungoogled-chromium_104.0.5112.101_1.vaapi_linux.tar.xz",
    "unknown": "https://github.com/macchrome/linchrome/releases/download/v104.0.5112.101-r1012729-portable-ungoogled-Lin64/ungoogled-chromium_104.0.5112.101_1.vaapi_linux.tar.xz",
}


def _checkOsSendUrl() -> str:
    nameOs: str = platform.system().lower()
    return OsLIST.get(nameOs, None) or OsLIST.get("unknown")


def _downloadFile(url: str, file: str) -> bool:
    try:
        wget.download(url, file)
        return True
    except Exception as err:
        print(err)
        return False


def _unzipFile(file: str) -> bool:
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall("./")
            return True
    except Exception as err:
        print(err)
        return False


def _extractTarFile(file: str) -> bool:
    with lzma.open(file) as fd:
        with tarfile.open(fileobj=fd) as tar:
            tar.extractall('./')


def _removeFile(name: str) -> None:
    try:
        os.remove(name)
    except:
        pass


def FindChromeFolder() -> str:
    for dirpath, _, filenames in os.walk("./"):
        for filename in filenames:
            if filename == "chrome.exe":
                return os.path.join(dirpath, filename)
    return ""


def DownloadFileChromium() -> str:
    url: str = _checkOsSendUrl()
    suffix: str = ".zip" if url.endswith(".zip") else ".tar.xz"
    nameFile: str = "./Chromium" + suffix

    assert _downloadFile(url, nameFile), ConnectionError(
        "can't download file!")

    print("extract files!")
    if suffix == ".tar.xz":
        assert _extractTarFile(nameFile), ValueError("Can't export file!")
    else:
        assert _unzipFile(nameFile), ValueError("Can't export file!")

    _removeFile(nameFile)
    print("Download Complete!")

    return FindChromeFolder()
