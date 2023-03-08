const background = document.querySelector('header');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  const backgroundSize = 120 - scrollPosition/80;
  background.style.backgroundSize = `${backgroundSize}%`;
});

const elements = document.querySelectorAll('icon');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
    }
  });
});

elements.forEach(element => {
  observer.observe(element);
});
