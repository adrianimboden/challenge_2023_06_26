import flask
import os

app = flask.Flask(__name__)

script_dir = os.path.abspath(os.path.dirname(__file__))


@app.route("/wYhig")
def step1():
    @flask.after_this_request
    def add_header(response):
        response.headers[
            'X-BBZW-CHALLENGE'] = 'Gratulliere. Hier geht es weiter: https://bbzwchallenge.k8s.firenet.ch/image.png'
        return response

    return "<html><head><title>Willkommen</title></head><body>Willkommen auf meiner tollen Webseite. Was sich hier wohl noch versteckt?</body></html>"


@app.route("/mszz3")
def step3():
    return flask.send_file(os.path.join(script_dir, 'step3.zip'),
                           download_name='../../COM1',
                           mimetype='image/jpeg')


#this is the target in the zip bomb
@app.route("/R52W")
def step4():
    return """
    <html>
        <head>
        </head>
        <body>
        <textarea cols="120" rows="50">
#include <stdio.h>

#define A 0x68
#define B 0x74
#define C 0x74
#define D 0x70
#define E 0x73
#define F 0x3a
#define G 0x2f
#define H 0x2f
#define I 0x62
#define J 0x62
#define K 0x7a
#define L 0x77
#define M 0x63
#define N 0x68
#define O 0x61
#define P 0x6c
#define Q 0x6c
#define R 0x65
#define S 0x6e
#define T 0x65
#define U 0x74
#define V 0x2e
#define W 0x6b
#define X 0x38
#define Y 0x73
#define Z 0x2f
#define AA 0x2e
#define BB 0x66
#define CC 0x69
#define DD 0x72
#define EE 0x65
#define FF 0x6e
#define GG 0x65
#define HH 0x74
#define II 0x2e
#define JJ 0x63
#define KK 0x68
#define LL 0x2f
#define MM 0x57
#define NN 0x6b
#define OO 0x71
#define PP 0x5a
#define QQ 0x61
#define RR 0x53
#define SS 0x63

int main() {
    char link[] = {
            A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, 'g', 'e', V, W, X, Y,  AA, BB, CC, DD, EE, FF, GG, HH, II, JJ, KK, LL, MM, NN, OO, PP, QQ, RR, SS, '\0'
    };

    printf("%s\\n", link);

    return 0;
}

        </textarea>
        </body>
    </html>
    """


@app.route("/WkqZaSc")
def step5():
    return r"""
    <html>
        <head>
            <title>Das grosse Finale</title>
            <script>
                function the_function() {
                   const a = "R3JhdHVsaWVyZSwgZHUgaGFzdCBkYXMgUuR0c2VsIGtvbXBsZXR0IGdlc2NoYWZ0LiBCaXR0ZSBtZWxkZSBkaWNoIGJlaSBlaW5lciBkZXIgTGVocnBlcnNvbmVuIDsp";
                   document.getElementById("story").innerHTML = atob(a);
                }
            </script>
        </head>
        <body>
        <div id="story" style="width: 40em">

<p>Es war ein ganz gewöhnlicher Tag an der Berufsschule für Informatik. Die Sonne schien, die Vögel zwitscherten, und die Schüler waren voller Energie. Doch heute sollte etwas Außergewöhnliches passieren.
</p><p>Herr Schmidt, der charismatische Informatiklehrer, betrat das Klassenzimmer mit einem geheimnisvollen Lächeln im Gesicht. "Guten Morgen, meine lieben Schülerinnen und Schüler", begrüßte er sie. "Heute haben wir ein kleines Rätselwettbewerb!"
</p><p>Die Schüler sahen sich aufgeregt an und begannen, wild zu spekulieren, was sie erwarten würde. Frau Müller, die streng, aber gerecht war, trat neben Herrn Schmidt. "In diesem Wettbewerb geht es darum, wer als erstes das geheime Passwort für den virtuellen Tresor knacken kann", verkündete sie mit einem Hauch von Herausforderung in ihrer Stimme.
</p><p>Die Schüler konnten kaum ihre Vorfreude verbergen. Es war ein Wettkampf, den sie nicht verlieren wollten. Das Rätsel bestand aus einer Reihe von kniffligen Aufgaben und Hinweisen, die nur die schlauesten Köpfe der Klasse lösen konnten. Die Zeit lief, und die Schüler arbeiteten mit Hochdruck daran, die richtigen Antworten zu finden.
</p><p>Während die Schüler sich ins Zeug legten, versuchten die Lehrpersonen, ihnen gelegentlich einen Hinweis zu geben, um ihre Gedanken auf die richtige Spur zu lenken. Herr Schmidt versuchte sich an einem Wortspiel, um die Schüler zum Nachdenken anzuregen. Doch statt sie zu inspirieren, brachte er sie zum Lachen. "Warum hatte der Computer schlechte Noten in der Schule? Weil er sich nicht gut in den Tastaturkursen anschlagen konnte!" Die Schüler brachen in Gelächter aus und verloren für einen Moment den Fokus.
</p><p>Frau Müller war entschlossen, den Schülern einen ernsteren Hinweis zu geben. Sie schrieb eine Formel an die Tafel und sagte: "Denkt an die binäre Logik und die magische Zahl Phi. Kombiniert diese Konzepte, um das Passwort zu entschlüsseln." Die Schüler sahen sich verwirrt an, aber ein aufmerksamer Schüler namens Alex verstand den Hinweis sofort.
</p><p>Mit einem triumphierenden Grinsen erklärte Alex seine Lösung den anderen Schülern. "Das Passwort lautet '1010010101'. Es ist eine Kombination aus Binär- und Fibonacci-Zahlen, die auf Phi basieren!" Die Klasse war beeindruckt von Alex' Geistesblitz.
</p><p>Herr Schmidt und Frau Müller waren gleichermaßen stolz auf ihre Schüler. Es war ein hart umkämpfter Wettbewerb gewesen, aber letztendlich hatten die Schüler bewiesen, dass sie wahre Informatikexperten waren.
</p><p>Als Belohnung für ihre Leistungen luden die Lehrpersonen die Schüler zu einem gemeinsamen Ausflug in den nahegelegenen Freizeitpark ein. Die Schüler jubelten vor Freude und waren begeistert von der Idee, einen lustigen Tag zusammen zu verbringen.
</p><p>Und so endete der Tag mit einem strahlenden Sieg für die Schüler der Berufsschule für Informatik. Sie hatten nicht nur das Rätsel gelöst, sondern auch bewiesen, dass Teamarbeit und Kreativität die Schlüssel zum Erfolg waren.
</p><p>Die Schüler würden diesen Tag in Erinnerung behalten und ihre Freundschaften an der Berufsschule für Informatik noch weiter vertiefen. Und wer weiß, vielleicht würden sie in Zukunft noch viele weitere Rätsel gemeinsam lösen und ihre Informatikkenntnisse auf spielerische Weise erweitern.
</p>

        Mit lieben Grüssen, euer ChatGPT, der gerne lange Texte erstellt um euch abzulenken ;)
        </div>
        </body>
    </html>
    """


@app.route("/image.png")
def step2():
    return flask.send_file(os.path.join(script_dir, 'image.png'))


@app.route("/20eqr.svg")
def inf20e_step1_img():
    return flask.send_file(os.path.join(script_dir, '20eqr.svg'))


@app.route("/inf20e")
def inf20e_step0a():
    @flask.after_this_request
    def add_header(response):
        response.headers[
            'X-BBZW-CHALLENGE'] = 'Gratulliere. Hier geht es weiter: https://bbzwchallenge.k8s.firenet.ch/KHh6'
        return response

    return flask.redirect("/inf20e_b")


@app.route("/inf20e_b")
def inf20e_step0b():
    return flask.redirect("/inf20e")


@app.route("/KHh6")
def inf20e_step1():
    return r"""
    <html>
    <head>
    <title>Mr. QR</title>
    </head>
    <body>
        <img src="/20eqr.svg" style="display: none"></img>
    <div id="story" style="width: 31em">
    <p>Es war einmal ein junger Mann namens Max, der ein Faible für Rätsel und Geheimnisse hatte. Eines Tages entdeckte er in einem alten Buch über Magie eine rätselhafte Geschichte über einen Zauberer, der einen unglaublichen Schatz bewachte. Angeblich konnte man diesen Schatz nur finden, wenn man den richtigen QR-Code scannte, der irgendwo in der Welt versteckt war.</p>

<p>Max war fasziniert von der Vorstellung, einen verborgenen Schatz zu finden, und begann, nach Hinweisen zu suchen, die ihn zum QR-Code führen könnten. Er durchforstete Bücher und das Internet, aber keine der Informationen schien ihm weiterzuhelfen. Frustriert beschloss er, eine Pause einzulegen und spazierte durch den örtlichen Park.</p>

<p>Als Max durch den Park schlenderte, fiel ihm plötzlich ein merkwürdiges Wandgemälde auf, das er noch nie zuvor bemerkt hatte. Das Gemälde zeigte einen majestätischen Zauberer, der einen geheimnisvollen QR-Code in den Händen hielt. Max fühlte eine seltsame Verbindung zu dem Bild und beschloss, den QR-Code zu scannen. Er holte sein Smartphone heraus, öffnete die QR-Code-Scanner-App und richtete die Kamera auf den Code.</p>

<p>Kaum hatte Max den Code gescannt, als ein gleißend helles Licht aus seinem Smartphone strahlte. Er musste die Augen schließen, um sich vor der Helligkeit zu schützen. Als er sie wieder öffnete, befand er sich in einem magischen Garten. Überall um ihn herum blühten wunderschöne Blumen, und ein sanfter Wind strich durch seine Haare.</p>

<p>Plötzlich hörte Max eine Stimme, die sagte: "Willkommen, Max, in meiner magischen Welt. Ich bin der große Zauberer Arkanus, der Hüter des verborgenen Schatzes." Max sah sich um und entdeckte den Zauberer, der ihm aus dem Gemälde bekannt vorkam. "Du hast den QR-Code gefunden, der dich zu mir geführt hat. Nur diejenigen mit einem wahren Sinn für Abenteuer und einer Leidenschaft für Rätsel können meinen Schatz finden."</p>

<p>Max war begeistert und fragte den Zauberer, wie er den Schatz finden könne. Arkanus lächelte und sagte: "Du musst eine Reihe von Aufgaben und Rätseln lösen, um die magischen Schlüssel zu bekommen, die dich zum Schatz führen. Aber sei gewarnt, Max, der Weg ist voller Herausforderungen und Gefahren."</p>

<p>Max war entschlossen und begann seine Reise durch den magischen Garten, um die Aufgaben des Zauberers zu lösen. Jede Aufgabe führte ihn zu einem weiteren Hinweis, der ihn dem Schatz näherbrachte. Mit jedem Rätsel wuchs Max' Begeisterung und Faszination für die Magie.</p>

<p>Und so setzte Max seine Reise fort, begleitet von der Magie des Zauberers Arkanus und dem Geheimnis des verborgenen Schatzes, der nur darauf wartete, entdeckt zu werden.</p>
<p>
Ende der Geschichte. Autor: ChatGPT, der Ablenkungsmechanismus.
</p>

    </div>
    </body>
    </html>
    """


@app.route("/gLdgHb")
def inf20e_step2():
    return r"""
    <html>
        <head>
            <title>Mr. 64</title>
        </head>
        <body>
        <pre>
        Vm0weE5HRXlVWGhWV0doVlYwZDRWRmxVU205V01XeFZVMnBTV0ZKdGVEQlpNM0JIWVZVeFYyTklhRlppVkVaSVZrUkdZV1JHVm5WalJtUlRUVEJLVVZZeFdsWmxSbVJYVW01S2FsSnRVbkJWYWtaTFpWWmtWMVp0UmxSaVZrWTBWMnRvUjFkSFNsWlhiRkpYWWtaS1dGVnNXbXRYUjFKSVpFWldUbEpHV2xsV1Z6QXhVekpHUjFOWVpGaGlSM2hYV1d0YVMxZEdjRlpYYlhSWFRWWndNRnBGV2s5VWJVVjZVV3h3VjJKSFVYZFdWRVpTWlVaT1dXSkdXbWxTVkZab1YxZDBhMVZ0Vm5OalJWWlRZbTFTVkZscmFFTlRSbGw1VFZWa1ZXSlZjRWhaYWs1clZqSktWVkZZYUZaV1JWcDZWbTF6ZUZkV1VuTmFSMnhYVW14d1lWWXhXbE5UTVZWNVZtNU9hVk5GY0doVmJGSlhZekZhZEdWSVpGaFdiVko1VmpKNGEyRkdXbk5qUm1oYVRVZG9kbFl3V21Gak1XUjFWMnhhYkdFelFsRldWM0JMVW0xV2RGTnJhR2hTYXpWVVZteG9RMVJXV25OYVNHUlZUVlZXTlZaR2FHOWhiRXBYWTBjNVZrMUhVbFJXUkVaWFl6RndSVlZzVGs1V2JHOTNWa1phVTFFeVJrZFRiazVZWWtkNFZsUlZXa3RsVmxaSFVsUnNVVlZVTURrPQ==
        </pre>
        </body>
    </html>
    """
