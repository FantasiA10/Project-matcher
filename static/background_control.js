const background = document.querySelector('header');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  const backgroundSize = 120 - scrollPosition/80;
  background.style.backgroundSize = `${backgroundSize}%`;
});