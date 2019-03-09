// Quando l'utente scorre sotto 20px dal top della pagina, mostra il pulsante
        window.onscroll = function() {scrollFunction()};

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("myBtn").style.display = "block";
         } else {
            document.getElementById("myBtn").style.display = "none";
        }
      }

      // Quando l'utente clicca sul pulsante, scorri al top della pagina
         function topFunction() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
         }