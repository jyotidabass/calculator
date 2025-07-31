# Simple calculator that creates a webpage
def create_calculator():
    html = """<!DOCTYPE html>
<html>
<head>
    <title>My Python Calculator</title>
    <style>
        body { 
            font-family: Arial; 
            max-width: 400px; 
            margin: 50px auto; 
            padding: 20px; 
            background: #f5f5f5;
        }
        .calc { 
            background: white; 
            padding: 30px; 
            border-radius: 15px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 { 
            text-align: center; 
            color: #333; 
            margin-bottom: 30px;
        }
        input { 
            width: 100%; 
            padding: 15px; 
            font-size: 20px; 
            border: 2px solid #ddd; 
            border-radius: 8px; 
            margin-bottom: 20px;
            text-align: right;
        }
        button { 
            padding: 15px; 
            margin: 3px; 
            font-size: 18px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;
            transition: all 0.2s;
        }
        button:hover { 
            transform: translateY(-2px); 
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        .buttons { 
            display: grid; 
            grid-template-columns: 1fr 1fr 1fr 1fr; 
            gap: 10px; 
        }
        .number { background: #e3f2fd; color: #1976d2; }
        .operator { background: #fff3e0; color: #f57c00; }
        .equals { background: #4caf50; color: white; }
        .clear { background: #ffebee; color: #d32f2f; }
        .result { 
            background: #f0f0f0; 
            padding: 15px; 
            margin: 15px 0; 
            border-radius: 8px; 
            font-weight: bold; 
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="calc">
        <h1>🧮 My Calculator</h1>
        <input type="text" id="display" value="0" readonly>
        <div class="buttons">
            <button class="clear" onclick="clearDisplay()">C</button>
            <button class="clear" onclick="deleteLast()">⌫</button>
            <button class="operator" onclick="addToDisplay('/')">/</button>
            <button class="operator" onclick="addToDisplay('*')">×</button>
            
            <button class="number" onclick="addToDisplay('7')">7</button>
            <button class="number" onclick="addToDisplay('8')">8</button>
            <button class="number" onclick="addToDisplay('9')">9</button>
            <button class="operator" onclick="addToDisplay('-')">-</button>
            
            <button class="number" onclick="addToDisplay('4')">4</button>
            <button class="number" onclick="addToDisplay('5')">5</button>
            <button class="number" onclick="addToDisplay('6')">6</button>
            <button class="operator" onclick="addToDisplay('+')">+</button>
            
            <button class="number" onclick="addToDisplay('1')">1</button>
            <button class="number" onclick="addToDisplay('2')">2</button>
            <button class="number" onclick="addToDisplay('3')">3</button>
            <button class="equals" onclick="calculate()" style="grid-row: span 2;">=</button>
            
            <button class="number" onclick="addToDisplay('0')" style="grid-column: span 2;">0</button>
            <button class="number" onclick="addToDisplay('.')">.</button>
        </div>
        <div class="result" id="result">Ready to calculate! 🚀</div>
        <p style="text-align: center; color: #666; font-size: 14px;">
            Built with Python • Deployed with GitHub Actions
        </p>
    </div>
    <script>
        let display = document.getElementById('display');
        let result = document.getElementById('result');
        
        function addToDisplay(value) {
            if (display.value === '0' && value !== '.') {
                display.value = value;
            } else {
                display.value += value;
            }
        }
        
        function clearDisplay() {
            display.value = '0';
            result.textContent = 'Ready to calculate! 🚀';
        }
        
        function deleteLast() {
            if (display.value.length > 1) {
                display.value = display.value.slice(0, -1);
            } else {
                display.value = '0';
            }
        }
        
        function calculate() {
            try {
                // Replace × with * for calculation
                let expression = display.value.replace(/×/g, '*');
                let answer = eval(expression);
                result.textContent = '✅ Result: ' + answer;
                display.value = answer;
            } catch (error) {
                result.textContent = '❌ Error: Please check your calculation';
                display.value = '0';
            }
        }
        
        // Allow keyboard input
        document.addEventListener('keydown', function(event) {
            if (event.key >= '0' && event.key <= '9') {
                addToDisplay(event.key);
            } else if (['+', '-', '*', '/'].includes(event.key)) {
                addToDisplay(event.key);
            } else if (event.key === '.') {
                addToDisplay('.');
            } else if (event.key === 'Enter' || event.key === '=') {
                calculate();
            } else if (event.key === 'Escape' || event.key.toLowerCase() === 'c') {
                clearDisplay();
            } else if (event.key === 'Backspace') {
                deleteLast();
            }
        });
    </script>
</body>
</html>"""
    
    # Save the HTML file
    with open('index.html', 'w') as f:
        f.write(html)
    
    print("✅ Calculator created successfully!")
    print("🌐 Your calculator webpage is ready!")

if __name__ == "__main__":
    create_calculator()
