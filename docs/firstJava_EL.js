/* JavaScript 01 - EL */

window.addEventListener('DOMContentLoaded', init, false);

function init() {

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

      const answer1 = prompt("What year is it?");
      if (!answer1 || answer1.trim().toLowerCase() !== '2025') {
      document.getElementById('incorrectSound').currentTime = 0;
      document.getElementById('incorrectSound').play();
        alert("Nope! Try again.");
        return;
      }

      document.getElementById('correctSound').currentTime = 0;
      document.getElementById('correctSound').play();
      
      const answer2 = prompt("What is the capital of Pennsylvania?");
      if (!answer2 || answer2.trim().toLowerCase() !== 'harrisburg') {
      document.getElementById('incorrectSound').currentTime = 0;
      document.getElementById('incorrectSound').play();
        alert("Nope! Try again.");
        return;
      }
      
      document.getElementById('correctSound').currentTime = 0;
      document.getElementById('correctSound').play();
      
      const answer3 = prompt("How do caterpillars turn into butterflies?");
      if (!answer3 || answer3.trim().toLowerCase() !== 'metamorphosis') {
      document.getElementById('incorrectSound').currentTime = 0;
      document.getElementById('incorrectSound').play();
        alert("Nope! Try again.");
        return;
      }
      
      document.getElementById('correctSound').currentTime = 0;
      document.getElementById('correctSound').play();
      alert("You got them all right! Enjoy.");
      
      setTimeout(() => {
        window.location.href = "https://youtu.be/od_PmtmMDV0?si=OM-3iKSDAaxlP0bH";
      }, 1000);
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

const paragraphs = document.querySelectorAll('p');
paragraphs.forEach(p => {
  p.style.opacity = '0';
  p.style.transition = 'opacity 2s ease';
});
setTimeout(() => {
  paragraphs.forEach(p => {
    p.style.opacity = '1';
  });
}, 200);

    const divs = document.querySelectorAll('div');
    divs.forEach(div => {
        div.style.opacity = '0';
        div.style.transition = 'opacity 2s ease';
    });
    setTimeout(() => {
        divs.forEach(div => {
            div.style.opacity = '1';
        });
    }, 200);

    const secs = document.querySelectorAll('section');
    secs.forEach(section => {
        section.style.opacity = '0';
        section.style.transition = 'opacity 2s ease';
    });
    setTimeout(() => {
        secs.forEach(section => {
            section.style.opacity = '1';
        });
    }, 200);


function rollDice(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const rollButton20 = document.getElementById('d20'); 
if (rollButton20) {
  const diceImage20 = rollButton20.querySelector('img[src="images/1d20.png"]');
  let angle = 0; 

  rollButton20.addEventListener('click', () => {
    const result = rollDice(20);
    const message = `You rolled ... ${result}!`;

    angle += 360; 
    diceImage20.style.transition = 'transform 1s ease';
    diceImage20.style.transform = `rotate(${angle}deg)`;

    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}

const rollButton12 = document.getElementById('d12'); 
if (rollButton12) {
const diceImage12 = rollButton12.querySelector('img[src="images/1d12.png"]');
  let angle = 0; 
  rollButton12.addEventListener('click', () => {
    const result = rollDice(12);
    const message = `You rolled ... ${result}!`;
    
    angle -= 360; 
    diceImage12.style.transition = 'transform 1s ease';
    diceImage12.style.transform = `rotate(${angle}deg)`;
    
    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}
const rollButton10 = document.getElementById('d10'); 
if (rollButton10) {
const diceImage10 = rollButton10.querySelector('img[src="images/1d10.png"]');
  let angle = 0; 
  rollButton10.addEventListener('click', () => {
    const result = rollDice(10);
    const message = `You rolled ... ${result}!`;
    
    angle += 360; 
    diceImage10.style.transition = 'transform 1s ease';
    diceImage10.style.transform = `rotate(${angle}deg)`;
    
    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}
const rollButton8 = document.getElementById('d8'); 
if (rollButton8) {
const diceImage8 = rollButton8.querySelector('img[src="images/1d8.png"]');
  let angle = 0; 
  rollButton8.addEventListener('click', () => {
    const result = rollDice(8);
    const message = `You rolled ... ${result}!`;
    
    angle -= 360; 
    diceImage8.style.transition = 'transform 1s ease';
    diceImage8.style.transform = `rotate(${angle}deg)`;
    
    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}
const rollButton6 = document.getElementById('d6'); 
if (rollButton6) {
const diceImage6 = rollButton6.querySelector('img[src="images/1d6.png"]');
  let angle = 0; 
  rollButton6.addEventListener('click', () => {
    const result = rollDice(6);
    const message = `You rolled ... ${result}!`;
    
    angle += 360; 
    diceImage6.style.transition = 'transform 1s ease';
    diceImage6.style.transform = `rotate(${angle}deg)`;
    
    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}
const rollButton4 = document.getElementById('d4'); 
if (rollButton4) {
const diceImage4 = rollButton4.querySelector('img[src="images/1d4.png"]');
  let angle = 0; 
  rollButton4.addEventListener('click', () => {
    const result = rollDice(4);
    const message = `You rolled ... ${result}!`;
    
    angle -= 360; 
    diceImage4.style.transition = 'transform 1s ease';
    diceImage4.style.transform = `rotate(${angle}deg)`;
    
    setTimeout(() => {
      alert(message);
    }, 1000);
  });
}
const rollButton2 = document.getElementById('d2'); 
if (rollButton2) {
   const diceImage2 = rollButton2.querySelector('img[src="images/1d2.png"]');
  rollButton2.addEventListener('click', () => {
    const result = rollDice(2);
    let message;
    if (result === 1) {
      message = "Heads!";
      diceImage2.src = "images/1d2.png";
    } else {
      message = "Tails!";
      diceImage2.src = "images/1d2tails.png";
    }
    setTimeout(() => {
      alert(message);
    }, 100);
  });
}
}
