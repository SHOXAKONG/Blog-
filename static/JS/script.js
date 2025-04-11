function toggleInfo(clickedCard) {
    let allCards = document.querySelectorAll(".card .extra-info");

    allCards.forEach(info => {
        if (info !== clickedCard.nextElementSibling) {
            info.classList.remove("show");
        }
    });

    clickedCard.nextElementSibling.classList.toggle("show");
}

// JavaScript yordamida autofill bo'lgan inputni aniqlash

