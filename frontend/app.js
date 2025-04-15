async function startRecording() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.interimResults = false;

  const button = document.getElementById("speakButton");
  const loader = document.getElementById("loadingIndicator");

  // Show visual feedback
  button.classList.add("listening");
  loader.style.display = "block";

  recognition.onresult = async function (event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("response").innerHTML = `<strong>You said:</strong> ${transcript}`;

    try {
      const response = await fetch("http://localhost:8000/voice-command/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command: transcript })
      });

      const data = await response.json();
      document.getElementById("response").innerHTML += `<br><strong>AI Response:</strong> ${data.html}`;

      const tts = new SpeechSynthesisUtterance(data.text);
      window.speechSynthesis.speak(tts);
    } catch (error) {
      document.getElementById("response").innerHTML += `<br><strong>Error:</strong> ${error.message}`;
    }

    // Hide visual feedback
    loader.style.display = "none";
    button.classList.remove("listening");
  };

  recognition.onerror = function () {
    loader.style.display = "none";
    button.classList.remove("listening");
    alert("Voice recognition error. Try again.");
  };

  recognition.start();
}
