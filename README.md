# pthon-jinca-flask-api-gender-guess-project
pthon jinca flask api gender and age guess project, html templates
# Templating with jinja in flask
-	Jinja templating language
-	Kodların yazıldığı sytaxa a da jinja matkup/ templating language markup denir.
-	Server.py dosyası oluştur, env değişken olarak terminalde tanımla
-	İf __nam__ ==”__main__”: app.run() fonk ile çalıştır
-	Templates ve static klasörü oluştur framework render_template için bu klasörlere bakacak
-	Doc tempalte rendering e bak, render_template i import et
-	Rootda index dosyasını döndür
-	from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
-	jinca flask ile birlikte geliyor yüklemeye gerek yok 
-	çalıştırma syntax’ı {{}} içerisindekileri python kodu olarak algılar
-	{{ in jinca it is for single line expression
