const searchBar = document.getElementById('search-bar');
const gameList = document.getElementById('game-list');

searchBar.addEventListener('input', () => {
    const searchTerm = searchBar.value.toLowerCase();

    if (searchTerm.length > 0) {
        // Fetch game data from Steam API
        fetch(`https://api.steampowered.com/ISteamApps/GetAppList/v0/?key=YOUR_STEAM_API_KEY&q=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                gameList.innerHTML = '';

                if (data.applist.apps.length > 0) {
                    data.applist.apps.forEach(game => {
                        const gameItem = document.createElement('div');
                        gameItem.classList.add('game-item');

                        const gameTitle = document.createElement('h3');
                        gameTitle.classList.add('game-title');
                        gameTitle.textContent = game.name;

                        const gameImage = document.createElement('img');
                        gameImage.classList.add('game-image');
                        gameImage.src = game.img_icon_url;

                        gameItem.appendChild(gameTitle);
                        gameItem.appendChild(gameImage);

                        gameList.appendChild(gameItem);
                    });
                } else {
                    gameList.innerHTML = '<p>No games found.</p>';
                }
            });
    } else {
        gameList.innerHTML = '';
    }
});
