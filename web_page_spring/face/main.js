const video = document.getElementById("video");
const loginBtn = document.getElementById("login-btn");

// Access the user's media device (camera)
async function setupCamera() {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  video.srcObject = stream;
}

// Capture a video frame
async function captureFrame() {
  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  return canvas.toDataURL("image/jpeg");
}

// Login button event
loginBtn.addEventListener("click", async () => {
  const imageData = await captureFrame();
  faceRecognitionLogin(imageData);
});

// Face recognition login
async function faceRecognitionLogin(imageData) {
  const response = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: imageData }),
  });

  const result = await response.json();

  if (result.success) {
    alert("Login successful, welcome " + result.user.name);
    // Redirect to the dashboard page after login, e.g., window.location.href = "/dashboard";
  } else {
    alert("Login failed, please try again");
  }
}

// Initialize the camera
setupCamera();
