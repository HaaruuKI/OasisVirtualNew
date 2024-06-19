const list = document.getElementById("list"),
    listings = list.getElementsByClassName("list-items")[0],
    listing = listings.getElementsByClassName("list-item")[0];

const items = [{
    img: "https://wallpapers.com/images/hd/rick-and-morty-in-gazorpazorp-9f49a0dchqwp8nfa.webp",
    title: "Rick And Morty: The Game",
    price: "$69.99",
    rating: "68%",
    tags: ["Weird", "Space"]
}, {
    img: "https://wallpapers.com/images/high/2560x1440-pubg-halloween-skin-kt330lwosx7pyjiz.webp",
    title: "The Mummy Returns",
    price: "$9.99",
    rating: "91%",
    tags: ["Mummy", "Toilet Paper"]
}, {
    img: "https://wallpapers.com/images/high/fortnite-john-wick-1080p-gaming-gsumbav8abex0nte.webp",
    title: "John Wick 4",
    price: "$9.99",
    rating: "47%",
    tags: ["FPS", "Action", "Multiplayer"]
}, {
    img: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8bWVkaWV2YWx8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    title: "Harry Potter - Tell Tale Series",
    price: "$19.99",
    rating: "79%",
    tags: ["RPG", "Farming", "Magic"]
}, {
    img: "https://images.unsplash.com/photo-1624125278860-381b6acd3b44?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNvd2JveXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
    title: "Back To The Ranch (Dr. Phil Edition)",
    price: "$4.99",
    rating: "93%",
    tags: ["Open World", "Horses"]
}];

const addTags = (clone, tags) => {
    const wrapper = clone.getElementsByClassName("tags")[0];

    wrapper.innerHTML = "";

    tags.map((tag, index) => {
        const item = document.createElement("span"),
            dot = document.createElement("span");

        item.className = "tag";
        dot.className = "dot";

        item.innerText = tag;
        dot.innerText = "·";

        wrapper.appendChild(item);

        if (index < tags.length - 1) {
            wrapper.appendChild(dot);
        }
    });
}

for (let i = 0; i < 5; i++) {
    const clone = listing.cloneNode(true),
        image = clone.getElementsByClassName("list-item-image")[0],
        title = clone.getElementsByClassName("title")[0],
        price = clone.getElementsByClassName("price")[0],
        rating = clone.getElementsByClassName("rating")[0],
        item = items[i];

    image.src = item.img;
    title.innerText = item.title;
    price.innerText = item.price;
    rating.innerText = item.rating;

    addTags(clone, item.tags);

    listings.appendChild(clone);
}