<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz Test</title>
</head>
<body>
    <h2 id="question">Loading...</h2>
    <div id="options"></div>
    <button onclick="nextQuestion()">Next</button>
    <h3 id="score" style="display:none;"></h3>

    <script>
        const quizData = [
            {question: "What is 2 + 2?", options: ["3","4","5","6"], answer: 1}
        ];

        let current = 0;
        let score = 0;
        let selected = null;

        function loadQuestion() {
            const q = quizData[current];
            document.getElementById("question").innerText = q.question;
            const optionsDiv = document.getElementById("options");
            optionsDiv.innerHTML = "";
            q.options.forEach((opt,index)=>{
                const div = document.createElement("div");
                div.innerText = opt;
                div.style.padding = "8px";
                div.style.border = "1px solid #000";
                div.style.margin = "4px 0";
                div.onclick = function(){ selected=index; highlightSelection(index); };
                optionsDiv.appendChild(div);
            });
        }

        function highlightSelection(index){
            const options = document.getElementById("options").children;
            for(let i=0;i<options.length;i++){
                options[i].style.background = i===index?"#b3d1ff":"#fff";
            }
        }

        function nextQuestion(){
            if(selected === quizData[current].answer) score++;
            selected = null;
            current++;
            if(current >= quizData.length){
                document.getElementById("question").style.display="none";
                document.getElementById("options").style.display="none";
                document.querySelector("button").style.display="none";
                const scoreBox = document.getElementById("score");
                scoreBox.style.display="block";
                scoreBox.innerText = "Your Score: " + score + "/" + quizData.length;
            } else {
                loadQuestion();
            }
        }

        loadQuestion();
    </script>
</body>
</html>
