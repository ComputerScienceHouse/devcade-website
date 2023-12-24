import React from "react";
import axios from "axios";
import '../../css/games/gamelist.css';
import '../../index.tsx.css';

function getGameList() {
    let gameList = axios.get('https://devcade.csh.rit.edu/api/games/');
}

const GameList: React.FunctionComponent = () => {
    return (
        <div id="game-grid">
            {/* Make class for a game card */}
            {/* display a card for each game received from the api */}
        </div>
    )
}