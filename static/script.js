document.addEventListener('DOMContentLoaded', () => {
    // Fetch current puzzle letters from backend
    fetch('/api/puzzle')
        .then(res => res.json())
        .then(data => {
            // Populate each side: array of 3 letters, join with spaces
            document.getElementById('side-top').textContent = data.top.join(' ');
            document.getElementById('side-right').textContent = data.right.join(' ');
            document.getElementById('side-bottom').textContent = data.bottom.join(' ');
            document.getElementById('side-left').textContent = data.left.join(' ');
        })
        .catch(err => console.error('Error loading puzzle:', err));

    // Handle button click for generating solution
    document.getElementById('generate-btn').addEventListener('click', () => {
        // Determine selected number of words
        const count = document.querySelector('input[name="wordcount"]:checked').value;
        fetch(`/api/solve?words=${count}`)
            .then(res => res.json())
            .then(result => {
                const out = document.getElementById('solution-output');
                if (result.solutions && result.solutions.length > 0) {
                    out.innerHTML = result.solutions.map(s => `<div>${s}</div>`).join('');
                } else {
                    out.textContent = 'No solution found.';
                }
            })
            .catch(err => {
                console.error('Error getting solution:', err);
            });
    });
});
