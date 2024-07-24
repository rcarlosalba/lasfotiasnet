document.addEventListener('DOMContentLoaded', () => {
  const burger = document.getElementById('burger');
  const menu = document.getElementById('menu');
  const overlay = document.getElementById('overlay');
  const submenuLinks = document.querySelectorAll('.menu ul li a');

  burger.addEventListener('click', () => {
    burger.classList.toggle('open');
    menu.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
  });

  overlay.addEventListener('click', () => {
    burger.classList.remove('open');
    menu.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
  });

  submenuLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      const parentLi = link.parentElement;
      const submenu = parentLi.querySelector('.submenu');
      if (submenu) {
        e.preventDefault();
        submenu.classList.toggle('active');
        link.querySelector('.submenu-icon').classList.toggle('rotate-180');
      }
    });
  });
});
