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

const aboutUsBackground = document.querySelector('about-background-container');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  const backgroundTop = scrollPosition;
  aboutUsBackground.style.top = scrollPosition/3 +"px";
});

const tableOpacity = document.querySelectorAll('table-opacity');

const tableObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
    }
  });
});

tableOpacity.forEach(element => {
  tableObserver.observe(element);
});

const displayArea = document.querySelectorAll(".margin-left-bot-container");
const secondDisplayArea = displayArea.item(1)
displayArea.forEach(function(displayArea){
  displayArea.addEventListener("mouseover", () => {
    displayArea.lastElementChild.style.opacity = 1;
  });
  displayArea.addEventListener("mouseout", () => {
    displayArea.lastElementChild.style.opacity = 0;
  });
  displayArea.addEventListener("click", () => {
    if(displayArea==secondDisplayArea){
      window.location.href = "add_project";}
    else{
      window.location.href = "apply";};
  });
});