// Backend API base URL
const API_BASE_URL = "http://127.0.0.1:8000/api";

// Get references to the form, message area, and player list
const playerForm = document.getElementById("playerForm");
const message = document.getElementById("message");
const playersList = document.getElementById("playersList");


// Fetch all player ranks from the backend API
async function loadPlayers() {
    try {
        const response = await fetch(`${API_BASE_URL}/player-rank`);
        const players = await response.json();

        playersList.innerHTML = "";

        players.forEach((player) => {
            const card = document.createElement("div");
            card.className = "player-card";

            card.innerHTML = `
                <h3>${player.player_name}</h3>
                <p><strong>Level:</strong> ${player.level}</p>
                <p><strong>Rank:</strong> ${player.rank_title}</p>
                <p><strong>XP:</strong> ${player.xp}</p>
                <p><strong>XP to Next Level:</strong> ${player.xp_to_next_level}</p>
            `;

            playersList.appendChild(card);
        });

    } catch (error) {
        message.textContent = "Could not load players. Make sure the backend is running.";
    }
}


// Handle form submission
playerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const playerData = {
        player_name: document.getElementById("playerName").value,
        level: Number(document.getElementById("level").value),
        rank_title: document.getElementById("rankTitle").value,
        xp: Number(document.getElementById("xp").value),
        xp_to_next_level: Number(document.getElementById("xpToNextLevel").value)
    };

    try {
        const response = await fetch(`${API_BASE_URL}/player-rank`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(playerData)
        });

        const result = await response.json();

        if (!response.ok) {
            message.textContent = result.detail || "Something went wrong.";
            return;
        }

        message.textContent = "Player added successfully.";
        playerForm.reset();
        loadPlayers();

    } catch (error) {
        message.textContent = "Could not connect to backend API.";
    }
});


// Load players when the page first opens
loadPlayers();