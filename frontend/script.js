let token = '';

function signup() {
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    fetch('/signup/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    }).then(response => response.json())
      .then(data => alert(data.message));
}

function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    fetch('/token/', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: formData
    }).then(response => response.json())
      .then(data => {
          token = data.access_token;
          document.getElementById('auth').style.display = 'none';
          document.getElementById('prediction').style.display = 'block';
      });
}

function predict() {
    const humidity = parseFloat(document.getElementById('humidity').value);
    const wind_speed = parseFloat(document.getElementById('wind_speed').value);

    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify({humidity, wind_speed})
    }).then(response => response.json())
      .then(data => {
          document.getElementById('prediction-result').innerText = 'Predicted Temperature: ' + data.predicted_temperature;
      });
}
