from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Special Question 💖</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ffdde1, #ee9ca7);
            height: 100vh;
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .box {
            background: url('/static/background.jpg') no-repeat center;
            background-size: cover;
            padding: 45px;
            border-radius: 25px;
            min-height: 260px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.25);
            position: relative;
        }

        h2 {
            color: #ff4f87;
        }

        button {
            padding: 12px 28px;
            margin: 15px;
            font-size: 18px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        button:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        #yesBtn {
            background-color: #ff5f8f;
            color: white;
        }

        #noBtn {
            background-color: #555;
            color: white;
            position: absolute;
            left: 230px;
            top: 140px;
            transition: left 0.35s ease, top 0.35s ease, transform 0.35s ease;
        }

        .shake {
            animation: shake 0.35s;
        }

        @keyframes shake {
            0% { transform: rotate(0deg) scale(1); }
            25% { transform: rotate(10deg) scale(1.1); }
            50% { transform: rotate(-10deg) scale(1.1); }
            75% { transform: rotate(10deg) scale(1.1); }
            100% { transform: rotate(0deg) scale(1); }
        }

        #message {
            display: none;
            margin-top: 30px;
            animation: fadeIn 1s ease forwards;
        }

        #message h1 {
            color: #ff4f87;
        }

        #message p {
            font-size: 20px;
            line-height: 1.5;
        }

        .heart {
            position: fixed;
            color: #ff4f87;
            font-size: 24px;
            animation: floatUp 2s linear forwards;
        }

        @keyframes floatUp {
            0% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
            100% {
                opacity: 0;
                transform: translateY(-150px) scale(1.8);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
    </style>
</head>
<body>

<div class="box">
    <h2 id="question">Do you like this? 😊</h2>

    <button id="yesBtn">Yes</button>
    <button id="noBtn">No</button>

    <div id="message">
        <h1>💖 Beautiful Message 💖</h1>
        <p>
            You are amazing, special, and truly appreciated.
            Keep smiling — happiness looks beautiful on you.
        </p>
    </div>
</div>

<audio id="bgMusic" loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>

<script>
    const noBtn = document.getElementById("noBtn");
    const yesBtn = document.getElementById("yesBtn");
    const message = document.getElementById("message");
    const question = document.getElementById("question");
    const music = document.getElementById("bgMusic");

    function moveNoButton() {
        const box = document.querySelector(".box");

        const maxX = box.clientWidth - noBtn.offsetWidth - 20;
        const maxY = box.clientHeight - noBtn.offsetHeight - 20;

        const x = Math.random() * maxX;
        const y = Math.random() * maxY;

        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";

        noBtn.classList.add("shake");

        setTimeout(() => {
            noBtn.classList.remove("shake");
        }, 350);
    }

    noBtn.addEventListener("mouseover", moveNoButton);
    noBtn.addEventListener("click", moveNoButton);

    yesBtn.addEventListener("click", function() {
        question.style.display = "none";
        yesBtn.style.display = "none";
        noBtn.style.display = "none";
        message.style.display = "block";

        music.play();

        createHearts();
    });

    function createHearts() {
        setInterval(() => {
            const heart = document.createElement("div");
            heart.classList.add("heart");
            heart.innerHTML = "💖";

            heart.style.left = Math.random() * window.innerWidth + "px";
            heart.style.top = window.innerHeight + "px";

            document.body.appendChild(heart);

            setTimeout(() => {
                heart.remove();
            }, 2000);
        }, 300);
    }
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True)