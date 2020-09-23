# _Flask_Web_API_sample_SQLAlchemy

(This repository is my own self-study document
)

## リポジトリの目的

- ``Flask``の基礎学習
  - とりあえず組んで動かす
- 学習記録/自分用資料まとめ

## 主なリファレンス

- メインチュートリアル
  - **[Installation — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/installation/)**
  - **[Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/)**
  - **[Flask + SQLAlchemyプロジェクトを始める手順 - Qiita](https://qiita.com/shirakiya/items/0114d51e9c189658002e#comments)**
  - **[]()**
  - **[]()**

### **Flask**について

- GitHub : https://github.com/pallets/flask
- Official : https://flask.palletsprojects.com/en/1.1.x/

- Goコマンド
  - 原文 : https://golang.org/cmd/go/
  - 日訳 : https://godoc.org/github.com/gophersjp/go/src/cmd/go

- 文法 (The Go Programming Language Specification)
  - 原文 : https://golang.org/ref/spec

### **Python**について

- GitHub : https://github.com/python
- Official : https://www.python.org/
- Documentation :
  - General : https://www.python.org/doc/
  - Language : https://docs.python.org/ja/3/reference/index.html
  - CommandLine : https://docs.python.org/ja/3/using/cmdline.html

## 工程(参考先より適宜変更)

### [仮想環境の準備](https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments)

- 参考
  - [venv --- 仮想環境の作成 — Python 3.8.6rc1 ドキュメント](https://docs.python.org/ja/3/library/venv.html#module-venv)

- ``venv``モジュールから仮想環境を構築
  - ``$ python3 -m venv venv``

- 当該環境の有効化
  - ``$ . venv/bin/activate``

    ~~~
    (base) ***:_Flask_Web_API_sample_SQLAlchemy ***$ . venv/bin/activate
    (venv) (base) ***:_Flask_Web_API_sample_SQLAlchemy ***$ 
    ~~~

- ``Flask``等ライブラリのインストール
  - ``$ pip install flask SQLAlchemy flask-sqlalchemy PyMySQL``
    - **SQLAlchemy** :
      - GitHub : https://github.com/sqlalchemy/sqlalchemy
      - Official : https://www.sqlalchemy.org/
        - Python SQLツールキットとO／Rマッパー
    - **flask-sqlalchemy** :
      - GitHub : https://github.com/pallets/flask-sqlalchemy
      - Official : https://flask-sqlalchemy.palletsprojects.com/en/2.x/
        - FlaskアプリケーションでSQLAlchemyの機能の使用をサポートするツール
    - **PyMySQL** :
      - GitHub : https://github.com/PyMySQL/PyMySQL
      - Official : https://pymysql.readthedocs.io/en/latest/
        - Python MySQLのクライアントライブラリ

    ~~~
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

###  アプリケーションの体系を準備

- ``flask_sqlalchemy``によるDBの初期化処理
  - ``app/database.py``
    - Import
      - ``flask_sqlalchemy``

- []()
- 

### 

- ````
- ````
  - **** : 


## Tips

### 

### 

- []()


## 階層

~~~txt
_Flask_Web_API_sample_SQLAlchemy
├── 
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
