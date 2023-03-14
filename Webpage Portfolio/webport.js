// Toggle Icon Navigation Bar
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
  menuIcon.classList.toggle('bx-x');
  navbar.classList.toggle('active');
}

// Scroll Sections Active Link
let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
  section.forEach(sec => {
    let top = window.scrollY;
    let offset = sec.offsetTop - 150;
    let height = sec.offsetHeight;
    let id = sec.getAttribute('id');

    if(top <= offset && top < offset + height) {
        navLinks.forEach(links => {
            links.classList.remove('active');
            document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
      });
    };
  });

//   // Sticky Navigation Bar
let header = document.querySelector('header');

header.classList.toggle('sticky', window.scrollY > 100);

// Remove Toggle Icon and Navbar, When Link is Cicked (scroll)
  menuIcon.classList.remove('bx x');
  navbar.classList.remove('active')
};



// Show and Hide Section
const toggleButton = document.querySelector('#toggle-button');
const hiddenText = document.querySelector('#hidden-text');

toggleButton.addEventListener('click', () => {
  if (hiddenText.style.display === 'none') {
    hiddenText.style.display = 'block';
  } else {
    hiddenText.style.display = 'none';
  }
});

