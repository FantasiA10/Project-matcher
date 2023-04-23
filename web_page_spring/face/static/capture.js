const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
const preview = document.getElementById("preview");
const imageInput = document.getElementById("image");

navigator.mediaDevices
  .getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  })
  .catch((err) => {
    console.error("Error accessing camera: ", err);
  });

const captureForm = document.getElementById("captureForm");
captureForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  // Take a snapshot and set the image input value
  context.drawImage(video, 0, 0, 640, 480);
  const dataURL = canvas.toDataURL("image/jpeg");
  preview.src = dataURL;
  imageInput.value = dataURL;

  // Perform the login or registration
  const formData = new FormData(captureForm);
  const response = await fetch(captureForm.action, {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  if (data.success) {
    if (captureForm.action.includes("login")) {
      alert(`Login successful! Welcome, ${data.name}`);
    } else {
      alert("Registration successful!");
    }
  } else {
    alert("Face not recognized. Please try again.");
  }
});
