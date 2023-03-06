const bg = document.header.style.backgroundSize;
document.addEventListener("scroll", () => {
  const scroll = window.scrollY / 5;
  document.header.style.backgroundSize = `calc(${bg} + ${scroll}px)`;
});