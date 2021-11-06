function generateRandomColor()
        {
            var randomColor = '#'+Math.floor(Math.random()*16777215).toString(16);
            return randomColor;
        }

        var color = generateRandomColor();
        document.body.style.backgroundColor = color
        document.getElementById("text").textContent=color