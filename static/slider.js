
// Odlicza czas do wykonania zadania
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

// Klasa slidera
class Slider {
	constructor(listaSlajdow, domena="") {
		this.slides = listaSlajdow;
		this.nrSlajdu = 0;
		this.domena = domena
	}

	setSlide() {
		var slider = document.getElementById("slider-img");
		slider.style.opacity = 0.01;
		sleep(500).then(() => {
			slider.src = this.domena+this.slides[this.nrSlajdu]
			slider.style.opacity = 1;
		});
	}

	slideup() {
		// Zmiana slajdu
		if (this.slides.length == this.nrSlajdu+1) {
			this.nrSlajdu = 0;
		} else {
			this.nrSlajdu += 1;
		}

		// Funkcja
		this.setSlide()
	}

  slidedown() {
		// Zmiana slajdu
		if (this.nrSlajdu == 0) {
			this.nrSlajdu = this.slides.length-1;
		} else {
			this.nrSlajdu -= 1;
		}

		// Funkcja
		this.setSlide()
	}
}

// Definicje 
let slajder_produkty = new Slider(["static/slide_1.png", "static/slide_2.png"]);
let slajder_kontrybucje = new Slider(["static/slide_p_1.png", "static/slide_p_2.png", "static/slide_p_3.png", "static/slide_p_4.png"]);
let slajder_sabaka = new Slider([""], domena="http://127.0.0.1:5000")