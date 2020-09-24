# _Flask_Web_API_sample_SQLAlchemy

(This repository is my own self-study document
)

## リポジトリの目的

- ``Flask``の基礎学習
  - とりあえず組んで動かす
- 学習記録/自分用資料まとめ

## 主なリファレンス

### メインチュートリアル

- **[Installation — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/installation/)**
- **[Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/)**
- **[Flask + SQLAlchemyプロジェクトを始める手順 - Qiita](https://qiita.com/shirakiya/items/0114d51e9c189658002e#comments)**

### **Flask**について

- GitHub : <https://github.com/pallets/flask>
- Official : <https://flask.palletsprojects.com/en/1.1.x/>

### **Python**について

- GitHub : <https://github.com/python>
- Official : <https://www.python.org/>
- Document
  - General : <https://www.python.org/doc/>
  - Language : <https://docs.python.org/ja/3/reference/index.html>
  - CommandLine : <https://docs.python.org/ja/3/using/cmdline.html>
  - os : <https://docs.python.org/ja/3/library/os.html>
    - 雑多なオペレーティングシステムインタフェース

### **flask-sqlalchemy**について

FlaskアプリケーションでSQLAlchemyの機能の使用をサポートするツール

- GitHub : <https://github.com/pallets/flask-sqlalchemy>
- Official : <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>
- Document
  - API Reference : <https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/>

## 工程(参考先より適宜変更)

### [仮想環境の準備](https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments)

- 参考
  - [venv --- 仮想環境の作成 — Python 3.8.6rc1 ドキュメント](https://docs.python.org/ja/3/library/venv.html#module-venv)

- ``venv``モジュールから仮想環境を構築
  - ``$ python3 -m venv venv``

- 当該環境の有効化
  - ``$ . venv/bin/activate``

    ~~~log
    (base) ***:_Flask_Web_API_sample_SQLAlchemy ***$ . venv/bin/activate
    (venv) (base) ***:_Flask_Web_API_sample_SQLAlchemy ***$
    ~~~

- ``Flask``等ライブラリのインストール
  - ``$ pip install flask SQLAlchemy flask-sqlalchemy PyMySQL``
    - **SQLAlchemy**
      - GitHub : <https://github.com/sqlalchemy/sqlalchemy>
      - Official : <https://www.sqlalchemy.org/>
        - Python SQLツールキットとO／Rマッパー
    - **flask-sqlalchemy**
      - GitHub : <https://github.com/pallets/flask-sqlalchemy>
      - Official : <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>
        - FlaskアプリケーションでSQLAlchemyの機能の使用をサポートするツール
    - **PyMySQL**
      - GitHub : <https://github.com/PyMySQL/PyMySQL>
      - Official : <https://pymysql.readthedocs.io/en/latest/>
        - Python MySQLのクライアントライブラリ

    ~~~log
    flask in ./venv/lib/python3.8/site-packages (1.1.2)
    SQLAlchemy in ./venv/lib/python3.8/site-packages (1.3.19)
    flask-sqlalchemy in ./venv/lib/python3.8/site-packages (2.4.4)
    PyMySQL in ./venv/lib/python3.8/site-packages (0.10.1)
    Jinja2>=2.10.1 in ./venv/lib/python3.8/site-packages (from flask) (2.11.2)
    itsdangerous>=0.24 in ./venv/lib/python3.8/site-packages (from flask) (1.1.0)
    click>=5.1 in ./venv/lib/python3.8/site-packages (from flask) (7.1.2)
    Werkzeug>=0.15 in ./venv/lib/python3.8/site-packages (from flask) (1.0.1)
    MarkupSafe>=0.23 in ./venv/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask) (1.1.1)
    ~~~

### アプリケーションの体系を準備

- ``flask_sqlalchemy``によるDBの初期化処理
  - ``server/database.py``
    - Import
      - ``flask_sqlalchemy``
    - Method
      - [init_app(app)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy.init_app)
        - 対象のデータベース設定で使用するアプリケーションを初期化する

- 各ライブラリの設定項目を集約
  - ``server/config.py``
    - Import : ``os``
    - Method
      - [getenvb(key, default=None)](https://docs.python.org/ja/3/library/os.html#os.getenvb)
        - 環境変数の設定に用いる

- Flaskアプリケーションの初期化と、中枢となるオブジェクトの定義
  - ``server/app.py``
    - Import
      - ``flask``, ``database``
    - ``app = Flask(__name__)``
      - <https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/>
      - Flaskクラスのインスタンスを作成
        - ``__name__``については後述の**Tips**項で言及
    - ``app.config.from_object('server.config.Config')``
      - <https://flask.palletsprojects.com/en/1.1.x/api/#configuration>
      - 指定した外部のオブジェクトから設定値を適用する


### 

- ````
- ````
  - **** : 


## Tips

### [\_\_main\_\_ --- トップレベルのスクリプト環境 — Python 3.8.6rc1 ドキュメント](https://docs.python.org/ja/3/library/__main__.html)

- トップレベルのコードが実行されるスコープの名前が入る
- スクリプトとして実行されるときは``__main__``が入る
- 他のファイルからインポートして実行される場合はモジュールのファイル名が入る

### 

- []()


## 階層

~~~txt
_Flask_Web_API_sample_SQLAlchemy
├── app
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   └── 
├── 
│   └── 
├── .gitignore               // standard gitignore file
├── 
├── 
├── 
└── README.md                // simple readme file

### ├── │ └──
~~~

## Error

### 

~~~error

~~~

- 要因&対処
  - 
    - 
