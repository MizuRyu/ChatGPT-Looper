## ChatGPT-Looper
ChatGPT のブラウザを利用して、自動対話を実現する

* TalkingHeads の Fork↓
```
https://github.com/MizuRyu/ChatGPT-Looper.git
```

### dev
```
python3.11 -m venv venv
source venv/bin/activate
pip install -e .
pip install python-dotenv
```

### 注意
* User Profile Data (user_data_dir) は共有不可のため、コピーして作成する必要がある。
* 実行時、chrome のプロセスをすべてkillする必要がある
    * `pkill -f "Google Chrome"`