from flask import Flask, render_template, request

app = Flask(__name__)


""" Strony główne """

# Strona główna
@app.route("/")
def home_view():
	return render_template("strona_główna.html")

# Strona z wyborem kategorii produktu
@app.route("/produkty")
def products_view():
	return render_template("produkty.html")

# Strona rozwiązań
@app.route("/rozwiązania")
def solutions_view():
	return render_template("rozwiązania.html")

# Strona kontrybucji
@app.route("/kontrybucje")
def contribution_view():
	return render_template("kontrybucje.html")

# Strona akcji
@app.route("/akcje")
def akcje_view():
	return render_template("akcje.html")


""" Strony związane z pracą w Pik'u """
stanowiska = {}

class Stanowsiko:
	""" Klasa danych o stanowsku do wczytania przy stronie z CV """

	def __init__(self, 
			technologia,
			poziom_doswiadczenia, 
			miejsce_pracy,
			nazwa_stanowiska,
			opis_stanowiska,
			wymagania,
			kwalifikacje,
			benefity
		):
		""" Wczytywanie danych o stanowisku pracy """
		self.technologia = technologia
		self.poziom_doswiadczenia = poziom_doswiadczenia
		self.miejsce_pracy = miejsce_pracy
		self.nazwa_stanowiska = nazwa_stanowiska
		self.opis_stanowiska = opis_stanowiska
		self.wymagania = wymagania
		self.kwalifikacje = kwalifikacje
		self.benefity = benefity

		stanowiska[self.nazwa_stanowiska] = self

# Definiowanie stanowisk pracy
pythonist_pygame = Stanowsiko("Python", "Senior", "Szczecin", "Starszy programista Python z Pygame/PikEngine", 
	"""
	Na tym stanowsku będziesz zajmować się rozwojem naszych gier i sliników, które stanowią trzon naszej fimry.
	Jest to bardzo odpowiedzialne zadanie, przeznaczone dla programisty dobrze orientującego się w używanych przez nas
	technologiach takich jak python czy pygame.
	""",
	["Praca nad grą Pawiomen i Kobramen", "Praca nad PikEngine", "Optymalizacja kodu gry", "Tworzenie poziomów w Pik Snakestudio"],
	["Biegłej znajomości pythona i pygame", "Doświadczenia w optymalizacji kodu", "Doświadczenia w projektowaniu gier", "Znajomośc PikEngine mile widziana"],
	["Darmowy parking na terenie firmy", "Luźne godziny pracy", "Sprzęt komputerowy na miejscu", "Wygodne i dobrze wyposarzone stanowisko"]
)

pythonist_tkinter = Stanowsiko("Python", "Mid/Regular", "Szczecin", "Programista Python z tkinter i socket",
	"""
	Na tym stanowsku będziesz zajmować się rozwojem platform do dystrybucji naszych produktów, które stanowią trzon naszej fimry.
	Od czasu do czasu będziesz również tworzyć rozwiązania wewnątrzfirmowe. Od osoby na tym stanowisku wymagamy dobrej orientacji w
	bibliotekach takich jak tkinter i socket.
	""",
	["Praca nad Pik Launcher", "Praca nad oprogramowaniem autorskim do tworzenia gier", "Tworzenie interfejsów graficznych"],
	["Biegłej znajomości tkinter", "Orientowania się w programowaniu sieciowym", "Doświadczenia w projektowaniu i wdrażaniu interfejsów graficznych"],
	["Darmowy parking na terenie firmy", "Luźne godziny pracy", "Sprzęt komputerowy na miejscu", "Wygodne i dobrze wyposarzone stanowisko"]
)

java_sql = Stanowsiko("Java/SQL", "Junior", "Szczecin", "Programista Java z MySQL",
	"""
	Na tym stanowsku będziesz zajmować się utrzymywaniem i rozwijaniem systemów baz danych dla naszych gier i systemów
	zarządzania. Otrzymasz również możliwość pracy nad tworzeniem nowych rozwiązań w języku Java. Od osoby na tym stanowisku
	oczekujemy znajomości języka Java i SQL. Warto by kandydat potrafił również  programować sieciowo.
	""",
	["Praca z bazami danych", "Utrzymywanie systemów zarządzania i magazynowania danych", "Rozwój oprogramowania związanego z bazami danych"],
	["Przyzwoitej znajomości języka Java", "Wiedzy na temat relacyjnych baz danych", "Znajomości języka SQL"],
	["Darmowy parking na terenie firmy", "Luźne godziny pracy", "Sprzęt komputerowy na miejscu", "Wygodne i dobrze wyposarzone stanowisko", "Kursy i możliwość awansu"]
)

grafik = Stanowsiko("Programy Graficzne", "Mid/Regular", "Szczecin", "Grafik/Projektant gier",
	"""
	Na tym stanowsku będziesz zajmować się tworzeniem tekstur i szeroko rozumianej grafiki do naszych
	gier i innych produktów. Otrzymasz też możliwość projektowania plansz i poziomów w grach. Od osoby na tym
	stanowsku wymagamy dobrego orietnowania się w programach graficznych i tworzeniu tekstur.
	""",
	[],
	[],
	["Darmowy parking na terenie firmy", "Luźne godziny pracy", "Sprzęt komputerowy na miejscu"]
)

# Strona oferty pracy
@app.route("/praca", methods=["POST", "GET"])
def praca_view():
	return render_template("praca.html")

# Strona tworzenia stanowisk 						Nie skończone
@app.route("/managejob", methods=["POST", "GET"])
def praca_creator_view():
	return render_template("praca_creator.html")

@app.route("/result", methods=["POST", "GET"])
def praca_result():
	return render_template("result.html")

# Strona szczegółów pracy i wysyłania CV
@app.route("/aplikuj", methods=["POST", "GET"])
def praca_apply_view():
	wybrane_stanowisko = stanowiska[request.form['stanowisko']]
	return render_template("aplikuj.html",
		technologia=wybrane_stanowisko.technologia,
		poziom_doswiadczenia=wybrane_stanowisko.poziom_doswiadczenia,
		miejsce_pracy=wybrane_stanowisko.miejsce_pracy,
		nazwa_stanowiska=wybrane_stanowisko.nazwa_stanowiska,
		opis_stanowiska=wybrane_stanowisko.opis_stanowiska,
		wymagania=wybrane_stanowisko.wymagania,
		kwalifikacje=wybrane_stanowisko.kwalifikacje,
		benefity=wybrane_stanowisko.benefity
	)


""" Strony związane z kontem pik """
@app.route("/zaloguj")
def zaloguj():
	return render_template("zaloguj.html")


""" Strony związane z produktami """

# Strona z produktami typu PCC
@app.route("/pcc")
def pcc_view():
	return render_template("produkty_pcc.html")

# Strona z produktami typu oprogramowanie
@app.route("/oprogramowanie")
def software_view():
	return render_template("produkty_software.html")

# Strona z produktami typu peryferia
@app.route("/peryferia")
def peryferia_view():
	return render_template("produkty_peryferia.html")


# Strona z kupnem produktu software: Pik Sabaka
@app.route("/oprogramowanie/sabaka", methods=["POST", "GET"])
def software_product_view():
	return render_template("software_produkt.html", 
		domena="http://127.0.0.1:5000", 
		img_produktu="software_product_1.png",
		nazwa="Sabaka",
		cena="399,99zł",
		kompatyblinosc="PC lub PPC",
		wymagania="Procesor min. 1Ghz, 5mb pamięci",
		funkcja1="Prosta klasyfikacja psów",
		funkcja2="Wygodna wyszukiwarka",
		opis="Nasz produkt pozwala na wyjątkowo proste i szybkie zarządzanie bazą danych i wygodne wyszukiwanie istniejących danych. Wszystko to upiększa stworzony z największą starannością interfejs graficzny. ",
		slajder="slajder_sabaka"	
	)




# Strona kupowania czegoś
@app.route("/zakup", methods=["POST", "GET"])
def zakup_view():
	produkt = request.form['produkt']
	cena = request.form['cena']
	return render_template("zakup.html", produkt=produkt, cena=cena)


app.run()