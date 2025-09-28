/* First Javascript File - EL */
/* Applying changes only to the home page for this initial js file */

window.addEventListener('DOMContentLoaded', init, false);

function init() {
  if (window.location.pathname.endsWith('index.html')) {
    alert('Welcome to evSite 400 - Revitalized with JavaScript Capabilities!');
  }

  const links = document.querySelectorAll(".nav-link");
  links.forEach(link => {
    link.style.padding = "10px 5px";
    link.style.display = "inline-block";

    link.addEventListener("mouseover", function() {
      this.style.backgroundColor = "lightgreen";
    });

    link.addEventListener("mouseout", function() {
      this.style.backgroundColor = "";
    });
  });

  const quizLink = document.getElementById('quizBox');
  if (quizLink) {
    quizLink.addEventListener('click', function(event) {
      event.preventDefault();

      const answer = prompt("What is 3 to the power of 3?");
      if (answer === '27' || answer === 'twenty-seven' || answer === 'Twenty Seven' || answer === 'twenty seven' || answer === 'Twenty-Seven') {
        alert("Nicely done.");
      } else {
        alert("Good attempt (maybe)! Try again.");
      }
    });
  }

  const style = document.createElement('style');
  style.textContent = `
    .yellowGlow {
      box-shadow: 0 0 15px 5px yellow;
      transition: box-shadow 0.3s ease;
    }
  `;
  document.head.appendChild(style);

  const figures = document.querySelectorAll('img');
  figures.forEach(figure => {
    figure.addEventListener('mouseenter', () => {
      figure.classList.add('yellowGlow');
    });
    figure.addEventListener('mouseleave', () => {
      figure.classList.remove('yellowGlow');
    });
  });

  /*   const paragraphs = document.querySelectorAll('h1');
  paragraphs.forEach(p => {
    p.style.opacity = 0;
    p.style.transition = 'opacity 2s ease'; 
    setTimeout(() => {
      p.style.opacity = 1;
    }, 300);
  });
   */
}
