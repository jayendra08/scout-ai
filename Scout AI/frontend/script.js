document.addEventListener("DOMContentLoaded", () => {

    const analyzeBtn = document.getElementById("analyzeBtn");

    analyzeBtn.addEventListener("click", analyzeResume);

    async function analyzeResume() {

        const file = document.getElementById("resumeFile").files[0];

        if (!file) {
            alert("Please upload a PDF resume.");
            return;
        }

        document.getElementById("loading").innerHTML =
            "<p><b>Analyzing Resume...</b></p>";

        document.getElementById("results").innerHTML = "";

        try {

            const formData = new FormData();

            formData.append("file", file);

            const response = await fetch("http://127.0.0.1:8080/analyze", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {

                const err = await response.json().catch(() => ({}));

                throw new Error(err.detail || "Backend returned an error.");

            }

            const data = await response.json();

            let html = "";

            html += "<h2>Top Job Matches</h2>";

            data.recommendations.forEach(job => {

                html += `
                <div class="job">

                    <h3>${job.job_title}</h3>

                    <p><strong>Category:</strong> ${job.category}</p>

                    <p><strong>Match Score:</strong> ${(job.match_score * 100).toFixed(2)}%</p>

                    <p><strong>Matched Skills</strong></p>

                    <ul>
                        ${job.matched_skills.map(skill => `<li>${skill}</li>`).join("")}
                    </ul>

                    <p><strong>Missing Skills</strong></p>

                    <ul>
                        ${job.missing_skills.map(skill => `<li>${skill}</li>`).join("")}
                    </ul>

                </div>
                `;

            });

            html += "<hr>";

            html += "<h2>Interview Questions</h2>";

            data.interview_questions.forEach((q, i) => {

                html += `
                <div class="question">

                    <h3>Q${i + 1}. ${q.question}</h3>

                    <p><strong>Answer:</strong></p>

                    <p>${q.answer}</p>

                    <p>
                        <b>${q.category}</b> | ${q.difficulty}
                    </p>

                </div>
                `;

            });

            document.getElementById("loading").innerHTML = "";

            document.getElementById("results").innerHTML = html;

        }
        catch (err) {

            document.getElementById("loading").innerHTML = "";

            document.getElementById("results").innerHTML =
                `<p style="color:red;"><b>${err.message}</b></p>`;

        }

    }

});